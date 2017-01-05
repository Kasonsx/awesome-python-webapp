# -*- coding:utf-8 -*-
import aiomysql
import logging,asyncio
# 记录SQL语句
def log(sql,args=()):
	logging.info('SQL:%s' % sql)
# =================数据库操作======================
# 创建连接池（全局）
# 每个HTTP请求都可以直接从连接池中直接获取数据库连接
# 好处：不必频繁地打开和关闭数据库连接，而是能复用就尽量复用
async def create_pool(loop, **kw):
	logging.info('Create database connection pool...')
	global __pool
	# 连接池由全局变量__pool存储
	# 缺省情况下将编码设置为utf8，自动提交事务
	__pool = await aiomysql.create_pool(
		host = kw.get('host','localhost'),
		port = kw.get('port', 3306),
		user = kw['user'],
		password = kw['password'],
		db = kw['db'],
		charset = kw.get('charset','utf8'),
		autocommit = kw.get('autocommit',True),
		maxsize = kw.get('maxsize',10),
		minsize = kw.get('minsize',1),
		loop=loop
		)

#销毁连接池
async def destory_pool():
	global __pool
	if __pool is not None:
		__pool.close()
		await __pool.wait_closed()

# SELECT操作
async def select(sql,args,size=None):
	log(sql,args)
	global __pool
	# with (await __pool) as conn:
	async with __pool.get() as conn:
		#cur = await conn.cursor(aiomysql.DictCursor)
		async with conn.cursor(aiomysql.DictCursor) as cur:
		# SQL语句的占位符是?，而MySQL的占位符是%s，替换
			await cur.execute(sql.replace('?','%s'), args or ())
			if size:
				# 获取最多指定数量的记录
				rs = await cur.fetchmany(size)
			else:
				# 获取所有记录
				rs = await cur.fetchall()
		logging.info('rows returned: %s' % len(rs))
		return rs
# Insert,Update,Delete操作
async def execute(sql,args,autocommit=True):
	log(sql)
	# with (await __pool) as conn:
	async with __pool.get() as conn:
		if not autocommit:
			await conn.begin()
		try:
			# cur = await conn.cursor()
			async with conn.cursor(aiomysql.DictCursor) as cur:
				await cur.execute(sql.replace('?','%s'),args)
				affected = cur.rowcount
			if not autocommit:
				await conn.commit()
		except BaseException as e:
			if not autocommit:
				await conn.rollback()
			raise
		return affected
def create_args_string(num):
	L = []
	for n in range(num):
		L.append('?')
	return ', '.join(L)
# ===================ORM===========================
class Field(object):

	def __init__(self, name, colume_type, primary_key, default):
		self.name = name
		self.colume_type = colume_type
		self.primary_key = primary_key
		self.default = default
	# default参数可以让ORM自己填入缺省值，并且缺省值可以作为函数对象传入，在调用save()时自动计算
	def __str__(self):
		return '<%s,%s:%s>' %(self.__class__.__name__, self.colume_type, self.name)

# 映射varchar的StringField
class StringField(Field):
	def __init__(self, name=None, primary_key=False, default=None,ddl='varchar(100)'):
		super().__init__(name,ddl,primary_key,default)
# bool
class BooleanField(Field):
	def __init__(self, name=None, default=False):
		super().__init__(name,'boolean', False,default)
# int
class IntegerField(Field):
	def __init__(self, name=None, primary_key=False, default=0):
		super().__init__(name, 'bigint', primary_key, default)
# float
class FloatField(Field):
	def __init__(self, name=None, primary_key=False, default=0.0):
		super().__init__(name, 'real', primary_key, default)
# text
class TextField(Field):
	def __init__(self, name=None, default=None):
		super().__init__(name, 'text', False, default)

# 映射信息
class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		# 排除Model本身
		if name =='Model':
			return type.__new__(cls, name, bases, attrs)
		# 获取table名称
		tableName = attrs.get('__table__',None) or name
		logging.info('found model:%s (table:%s)' %(name,tableName))
		# 获取所有Field和主键名
		mappings = dict()
		fields = []
		primaryKey = None
		for k,v in attrs.items():
			if isinstance(v, Field):
				logging.info('  found mapping: %s ==> %s' %(k,v))
				mappings[k] = v
				if v.primary_key:
					# 找到主键
					if primaryKey:
						raise RuntimeError('Duplicate primary key for field: %s' % k)
					primaryKey = k
				else:
					fields.append(k)
		if not primaryKey:
			raise RuntimeError('Primary key not found.')
		for k in mappings.keys():
			attrs.pop(k)
		escaped_fields = list(map(lambda f:'`%s`' %f, fields))
		attrs['__mappings__'] = mappings # 保存属性和列的映射关系
		attrs['__table__'] = tableName
		attrs['__primary_key__'] = primaryKey #主键属性名
		attrs['__fields__'] = fields # 除主键外的属性名
		# 构造默认的SELECT, INSERT, UPDATE和DELETE语句:
		attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
		attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
		attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
		attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
		return type.__new__(cls, name, bases, attrs)

# 定义所有ORM映射的基类Model
# 继承dict，实现__getattr__和__setattr__方法可以直接↓
# >>> user['id']
# 123
# >>> user.id
# 123
class Model(dict, metaclass=ModelMetaclass):
	def __init__(self, **kw):
		super(Model,self).__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" %key)

	def __setattr__(self,key,value):
		self[key] = value

	def getValue(self,key):
		return getattr(self,key,None)

	def getValueOrDefault(self, key):
		value = getattr(self,key,None)
		if value is None:
			field = self.__mappings__[key]
			if field.default is not None:
				value = field.default() if callable(field.default) else field.default
				logging.debug('using default value for %s:%s' %(key,str(value)))
				setattr(self,key,value)
		return value

	@classmethod
	async def findAll(cls, where=None, args=None, **kw):
		' find objects by where clause. '
		sql = [cls.__select__]
		if where:
			sql.append('where')
			sql.append(where)
		if args is None:
			args = []
		orderBy = kw.get('orderBy', None)
		if orderBy:
			sql.append('order by')
			sql.append(orderBy)
		limit = kw.get('limit',None)
		if limit is not None:
			sql.append('limit')
			if isinstance(limit,int):
				sql.append('?')
				args.append(limit)
			elif isinstance(limit,tuple) and len(limit) == 2:
				sql.append('?','?')
				args.extend(limit)
			else:
				raise ValueError('Invalid limit value: %s' % str(limit))
		rs = await select(' '.join(sql),args)
		return [cls(**r) for r in rs]

	@classmethod
	async def findNumber(cls, selectField, where=None, args=None):
		' find number by select and where.'
		sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
		if where:
			sql.append('where')
			sql.append(where)
		rs = await select(' '.join(sql), args, 1)
		if len(rs) == 0:
			return None
		return rs[0]['_num_']

	@classmethod
	async def find(cls, pk):
		' find object by primary key. ' 
		rs = await select('%s where `%s`=?' %(cls.__select__, cls.__primary_key__),[pk], 1)
		if len(rs) == 0:
			return None
		return cls(**rs[0])

	async def save(self):
		args = list(map(self.getValueOrDefault, self.__fields__))
		args.append(self.getValueOrDefault(self.__primary_key__))
		rows = await execute(self.__insert__, args)
		if rows != 1:
			logging.warn('failed to insert record:affected rows:%s' % rows)
	#把一个User实例存入数据库
	# user = User(id=123, name='Michael')
	# yield from user.save()

	async def update(self):
		args = list(map(self.getValue, self.__fields__))
		args.append(self.getValue(self.__primary_key__))
		rows = await execute(self.__update__, args)
		if rows != 1:
			logging.warn('failed to update by primary key: affected rows: %s' % rows)

	async def remove(self):
		args = [self.getValue(self.__primary_key__)]
		rows = await execute(self.__delete__, args)
		if rows != 1:
			logging.warn('failed to remove by primary key: affected rows: %s' % rows)


