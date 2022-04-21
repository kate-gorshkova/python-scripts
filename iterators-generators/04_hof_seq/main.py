from collections.abc import Iterable


def q_hofstadter(count_num: int, any_seq: list) -> Iterable[int]:
    if any_seq == [1, 2]:
        return
    num = 0
    while num < count_num:
        if num <= 1:
            yield any_seq[num]
        else:
            q = any_seq[-any_seq[-1]] + any_seq[-any_seq[-2]]
            any_seq.append(q)
            yield q
        num += 1


seq = [1, 1]
qq = q_hofstadter(15, seq)
for i_q in qq:
    print(i_q, end=" ")

# зачёт!
