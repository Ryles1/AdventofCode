import collections


def parse_room(room: str):
    temp = room.split('-')
    letters: str = ''.join(temp[:-1])
    sector, checksum= temp[-1].strip(']').split('[')
    return letters, sector, checksum


def is_valid_room(letters, checksum):
    letter_counts = collections.Counter(letters)
    check = list(letter_counts.keys())
    check.sort()
    check.sort(key=lambda x: letter_counts[x], reverse=True)
    check_str = ''.join(check[:5])
    if check_str != checksum:
        return False
    return True


def decrypt_name(encrypted, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = []
    for letter in encrypted:
        if letter == '-':
            new_letter = ' '
            decrypted.append(new_letter)
            continue
        new_index = (alphabet.index(letter) + shift) % 26  # if index goes over 26, loop back to start
        new_letter = alphabet[new_index]
        decrypted.append(new_letter)
    decrypted_name = ''.join(decrypted)
    return decrypted_name


def main(room_list):
    real_rooms = []
    sector_i_ds = []
    #  part 1: get real rooms and print sum of sector IDs of real rooms
    for room in room_list:
        letters, sector, checksum = parse_room(room)
        if is_valid_room(letters, checksum):
            real_rooms.append((letters, int(sector), checksum))
            sector_i_ds.append(int(sector))
    sector_id_sum = sum(sector_i_ds)
    print(f'Sum of sector IDs: {sector_id_sum}')

    #  part 2: decrypt real room names

    for encrypted_name, id, chksum in real_rooms:
        shift = id % 26  # 26 shifts takes you back to starting letter, so only shift remainder
        decrypted_name = decrypt_name(encrypted_name, shift)
        if 'pole' in decrypted_name:
            print(f'{decrypted_name} {id}')
        with open('day4names.txt', 'a') as f:
            f.write(f'{decrypted_name} {id}\n')
    return


if __name__ == '__main__':
    with open('./input/day4.txt') as f:
        lines = f.read().strip().split('\n')
    print(main(lines))

