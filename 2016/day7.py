import re


def get_lines(data):
    return data.split('\n')


def has_abba_str(str):
    for i, c in enumerate(str[:-3]):
        window = str[i: i + 4]
        if window[0] == window[3] and window [1] == window[2]:
            if window [0] != window[1]:
                return True
    return False


def get_abas(lst):
    abas = []
    for item in lst:
        for i, c in enumerate(item[:-2]):
            window = item[i: i + 3]
            if window[0] == window[2] and window[1] != window[0]:
                abas.append(window)
    return abas


def list_has_abba(lst):
    for item in lst:
        if has_abba_str(item):
            return True
    return False


def list_has_bab(lst, bab):
    item = ''.join(lst)
    if bab in item:
        return True
    return False


def main(data):
    lines = get_lines(data)
    ips_supporting_tls = 0
    ips_supporting_ssl = 0
    start_re = r'^[a-z]+'
    end_re = r'][a-z]+$'
    hypernet_re = r'\[[a-z]+]'
    mid_re = r'][a-z]+\['

    for line in lines:
        hypernets = re.findall(hypernet_re, line)
        supernets = re.findall(mid_re, line)
        supernets.append(re.search(start_re, line).group())
        supernets.append(re.search(end_re, line).group())

        # part 1
        if list_has_abba(hypernets):
            continue
        if list_has_abba(supernets):
            ips_supporting_tls += 1

        # part 2 - doesn't work, gives incorrect answer 222 instead of 231
        aba_list = get_abas(supernets)
        if len(aba_list) > 0:
            bab_list = [aba[1] + aba[0] + aba[1] for aba in aba_list]
            for bab in bab_list:
                if list_has_bab(hypernets, bab):
                    ips_supporting_ssl += 1
                    break

    return ips_supporting_tls, ips_supporting_ssl


if __name__ == '__main__':
    with open('./input/day7.txt') as f:
        data = f.read().strip()

    print(main(data))
