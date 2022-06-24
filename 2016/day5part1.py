import hashlib
import time

with open('./input/day5.txt') as f:
    door_id = f.read()

ZEROES = '00000'

number = 0
password_parts = []
start = time.time()
while len(password_parts) < 8:
    next_idx = door_id + str(number)
    idx_encoded = next_idx.encode()
    md5_hash = hashlib.md5(idx_encoded)
    hex = md5_hash.hexdigest()

    if hex[0:5] == ZEROES:
        next_char = str(hex[5])
        password_parts.append(next_char)
        print(password_parts)

    current_time = time.time()
    if current_time - start > 60:
        print('Time exceeded')
        break

    number += 1
end_time = time.time()
password = ''.join(password_parts)
print(password)
print(end_time - start)
