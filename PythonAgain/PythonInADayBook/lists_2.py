''' --- lists with numbers --- '''

# list of numbers
number_list = [1,2,3,4,5]
empty_number_list = []

# # each number loops in number_list
# for x in number_list:
#     # print each number to the power of 2
#     print x**2

# each number loops in number_list
for x in number_list:
    # append each number to the power of 2 to the empty_number_list
    empty_number_list.append(x**2)

print empty_number_list
