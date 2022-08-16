import json


def count_nested_json_ints(json_item, part2=False):
    """This function uses recursion to search the nested levels of the json item for ints.
    For part 2, all json objects with a property having the value 'red' are excluded (total value 0).
    Returns the sum of all valid integers in the json item."""
    int_sum = 0
    if isinstance(json_item, int):
        return json_item
    elif part2 and isinstance(json_item, dict) and "red" in json_item.values():
        return 0
    for sub_item in json_item:
        if isinstance(sub_item, int):
            int_sum += sub_item
        elif isinstance(sub_item, dict) or isinstance(sub_item, list):
            nested_count = count_nested_json_ints(sub_item, part2)
            int_sum += nested_count
        elif isinstance(sub_item, str) and isinstance(json_item, dict):
            nested_count = count_nested_json_ints(json_item[sub_item], part2)
            int_sum += nested_count
        else:
            continue
    return int_sum


if __name__ == '__main__':
    with open('./input/day12.txt') as f:
        s = f.read()

    j = json.loads(s)

    print(count_nested_json_ints(j, False))
    print(count_nested_json_ints(j, True))
