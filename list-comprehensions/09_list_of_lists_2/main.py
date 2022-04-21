nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

my_list = [num for num_list in nice_list for number_list in num_list for num in number_list]
print(my_list)

# зачёт!
