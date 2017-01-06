# -*- coding: utf-8 -*-
import base64
print(base64.b64encode(b'binary\x00String'))
print(len(b'binary\x00String'))
print(base64.b64decode(b'YmluYXJ5AFN0cmluZw=='))
print(len(b'YmluYXJ5AFN0cmluZw=='))

print(base64.b64encode(b'abcd'))
print(len(b'abcd'))
print(base64.b64decode(b'YWJjZA=='))
print(len(b'YWJjZA=='))



