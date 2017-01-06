# -*- coding: utf-8 -*-
from datetime import datetime
now = datetime.now()
print(now)

dt = datetime(2016, 2, 2, 11, 12,56)
print(dt)
ts = dt.timestamp()
print(ts)
tdt = datetime.fromtimestamp(ts)
print(tdt)

#str to datetime
cday = datetime.strptime('2014-6-1 13:43:32', '%Y-%m-%d %H:%M:%S')
print(cday)
#datetime to str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

#加减时间
from datetime import timedelta
now = datetime.now()
print(now)
print(now + timedelta(hours=2))
print(now - timedelta(days=1))
print(now + timedelta(days=4,hours=12))

from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))

import re
def to_timestamp(dt_str,tz_str):
	dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

	re_tz = re.compile(r'^UTC([\+\-])(0[0-9]|[0-9]|1[0-2])\:00$')
	m = re_tz.match(tz_str)
	#m = re.match(r'^UTC([\+\-])(\d{1,2})\:(\d{1,2})$', tz_str)
	print(m.groups())
	tz_local = timezone(timedelta(hours=int(m.group(1)+m.group(2))))
	dt = dt.replace(tzinfo=tz_local)
	return dt.timestamp()
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
print(t1)
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print(t2)
