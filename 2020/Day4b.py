#! python3

def validate_passport(passport):
    required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    eye_colors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    if 7 > len(passport.keys()) or len(passport.keys()) > 8 :
        return False
    elif not set(passport.keys()) == required_fields:
        return False
    elif not 1920 <= int(passport['byr']) <= 2002:
        return False
    elif not 2010 <= int(passport['iyr']) <= 2020:
        return False
    elif not 2020 <= int(passport['eyr']) <= 2030:
        return False
    elif passport['ecl'] not in eye_colors:
        return False
    elif len((passport['pid'])) != 9 or not passport['pid'].isnumeric():
        return False
    elif not passport['hcl'].startswith('#') or not passport['hcl'][1:].isalnum():
        return False
    elif not ((passport['hgt'].endswith('cm') and 150 <= int(passport['hgt'][:-2]) <= 193) \
              or (passport['hgt'].endswith('in') and 59 <= int(passport['hgt'][:-2]))) <= 76:
        return False
    else:
        pass
    return True

with open('input.txt') as f:
    text = f.read()

groups = text.strip().split('\n\n')
passport_strings = []

#could optimize this by skipping the passport_strings step and going straight to dicts
for group in groups:
    temp = group.replace('\n', ',')
    temp = temp.replace(' ', ',')
    passport_strings.append(temp.split(','))

passport_dicts = []
for passport in passport_strings:
    passport_dicts.append(dict(map(lambda s: s.split(':'), passport)))

count = 0
for passport in passport_dicts:
    count += 1 if validate_passport(passport) else 0

print(count)

