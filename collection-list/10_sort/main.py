N = [1, 4, -3, 0, 10, -127]
for i in range(len(N) - 1):
    for j in range(len(N) - i - 1):
        if N[j] > N[j + 1]:
            N[j], N[j + 1] = N[j + 1], N[j]
print(N)

# зачёт!
