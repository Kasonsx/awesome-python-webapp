# -*- coding: utf-8 -*-
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def md5_format(password):
	md5 = hashlib.md5()
	md5.update(str(password).encode('utf-8'))
	return md5.hexdigest()
def checkPswd(user,password):
	if db[user] == md5_format(password):
		print('Login successfully!')
	else:
		print('Login failured.')
def md5_formatplus(username,password):
	md5 = hashlib.md5()
	md5.update(str(username+password+'a random string').encode('utf-8'))
	return md5.hexdigest()

print(md5_format('sadlskdjal'))
print(md5_format('how to use md5 in python hashlib'))

checkPswd('michael','123456')