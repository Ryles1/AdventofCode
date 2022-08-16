import pytest
import json
import day12


@pytest.mark.parametrize("examples2, answers2", [
    (json.loads("[1,2,3]"), 6),
    (json.loads('[1,{"c":"red","b":2},3]'), 4),
    (json.loads('{"d":"red","e":[1,2,3,4],"f":5}'), 0),
    (json.loads('[1,"red",5]'), 6)
])
def test_decompress2(examples2, answers2):
    assert day12.count_nested_json_ints(examples2, True) == answers2


@pytest.mark.parametrize("examples1, answers1", [
    (json.loads("[1,2,3]"), 6),
    (json.loads('{"a":2,"b":4}'), 6),
    (json.loads("[[[3]]]"), 3),
    (json.loads('{"a":{"b":4},"c":-1}'), 3),
    (json.loads('{"a":[-1,1]}'), 0),
    (json.loads('[-1,{"a":1}]'), 0),
    (json.loads("[]"), 0),
    (json.loads("{}"), 0),
])
def test_decompress1(examples1, answers1):
    assert day12.count_nested_json_ints(examples1) == answers1

