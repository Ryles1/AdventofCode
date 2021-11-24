#! python3

def validate_passport(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if 7 > len(passport.keys()) or len(passport.keys()) > 8 :
        return False
    elif len(passport.keys()) == 7:
        for field in required_fields:
            if field not in passport.keys():
                return False
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

