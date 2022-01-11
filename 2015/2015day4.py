import hashlib
import time


KEY = 'iwrupvqb'
ZEROES = '000000'

number = 0
start = time.time()
while True:
    key_str = KEY + str(number)
    key_encoded = key_str.encode()
    md5_hash = hashlib.md5(key_encoded)
    hex = md5_hash.hexdigest()

    if hex[0:6] == ZEROES:
        break

    current_time = time.time()
    if current_time - start > 60:
        print('Time exceeded')
        break

    number += 1

print(number)


