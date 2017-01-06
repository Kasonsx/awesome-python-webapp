# -*- coding:utf-8 -*-
import poplib

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def decode_str(s):
	value, charset = decode_header(s)[0]
	if charset:
		value = value.decode(charset)
	return value
def guess_charset(msg):
	charset = msg.get_charset()
	if charset is None:
		content_tye = msg.get('Content-Type','').lower()
		pop = content_type.find('charset=')
		if pop >=0:
			charset = content_type[pos + 8:].strip()
	return charset
#indent用于缩进显示
def print_info(msg, indent=0):
	if indent ==0:
		for header in ['From','To','Subject']:
			value = msg.get(header,'')
			if value:
				if header=='Subject':
					value = decode_str(value)
				else:
					hdr, addr = parseaddr(value)
					name = decode_str(hdr)
					value = u'%s <%s>' %(name,addr)
			print('%s%s:%s' % ('  '*indent,header,value))
	if (msg.is_multipart()):
		parts = msg.get_payload()
		for n,part in enumerate(parts):
			print('%spart %s' % ('  '* indent,n))
			print('%s-------------------'%('  '*indent))
			print_info(part,indent+1)
	else:
		content_type = msg.get_content_type()
		if content_type == 'text/plain' or content_type=='text/html':
			content = msg.get_payload(decode=True)
			charset = guess_charset(msg)
			if charset:
				content = content.decode(charset)
			print('%sText:%s' % ('  '* indent,content + '...'))
		else:
			print('%sAttachment: %s'%('  '* indent, content_type))



email = 'sxk644653293@163.com'#input('email:')
password = 'mendosai89757'#input('password:')
pop3_server = 'pop3.163.com'#input('pop3 server:')

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)

print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print('Message: %s. Size: %s' %server.stat())

resp,mails,octets = server.list()

print(mails)

index = len(mails)
resp,lines,octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)
print_info(msg)
server.quit()