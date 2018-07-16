# ref: https://github.com/FoxHub/Google-FooBar/blob/master/decrypter.py
# ref: https://gist.github.com/jacquerie/cfb8a56636e2b9e12f51

import base64

MESSAGE = '''
HV4EEwINHBYEQk5cWVABEwsYEVBJTkEaGAoNCxgCAgBJRkNXQQQdDQASCAsCXltGRgsfAxgXGhVe
V1xBSRALFBcLAhAVCgRJVUVQBA0OEBIQBAMcCwNCTlxZUBMPAhYGHAAKQVVXQRMPGwceER1BWU1G
Rh0YAxJCQkZeEQkOSVlfV0IZDxdWQRw=
'''

KEY = 'fywfanyewen' # your username

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)
