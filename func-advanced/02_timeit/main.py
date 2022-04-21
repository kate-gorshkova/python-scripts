import timeit

res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(res)

print()

res = timeit.timeit('"-".join([str(i) for i in range(100)])', number=10000)
print(res)

print()

res = timeit.timeit("'-'.join(list(map(str, [i for i in range(100)])))", number=10000)
print(res)

# зачёт!
