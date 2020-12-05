#! python3

def get_row(s, rows):
    if len(s) == 0:
        return rows[0]
    elif s[0] == 'B':
        middle = int(len(rows) / 2)
        return get_row(s[1:], rows[middle:])
    elif s[0] == 'F':
        middle = int(len(rows) / 2)
        return get_row(s[1:], rows[:middle])
    else:
        pass

def get_col(s, cols):
    if len(s) == 0:
        return cols[0]
    elif s[0] == 'R':
        middle = int(len(cols) / 2)
        return get_col(s[1:], cols[middle:])
    elif s[0] == 'L':
        middle = int(len(cols) / 2)
        return get_col(s[1:], cols[:middle])
    else: pass

def main():
    with open('input.txt') as f:
        seats = f.readlines()

    seats = (seat.strip() for seat in seats)

    seat_ids = []
    for seat in seats:
        row = get_row(seat[:7], list(range(128)))
        col = get_col(seat[-3:], list(range(8)))
        id = row * 8 + col
        seat_ids.append(id)

    max_seat = max(seat_ids)
    seat_ids.sort()
    my_seat = list(set(range(min(seat_ids), max(seat_ids)+1)) - set(seat_ids))
    #print(seat_ids)
    print(f' Part one: {max_seat}.  Part two: {my_seat} ')

if __name__ == '__main__':
    main()