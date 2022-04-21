import collections


def can_be_poly(string: str) -> bool:
    return len(list(filter(lambda x: x % 2, collections.Counter(string).values()))) < 2


print(can_be_poly('ababc'))
print(can_be_poly('abbbc'))

# зачёт!
