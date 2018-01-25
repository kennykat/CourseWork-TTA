
# name_of_list = [list_item_1, list_item_2]

epic_programmer_list = ["Tim Berners-Lee",
"Guido Van Rossum",
"Linus Torvalds",
"Larry Page",
"Sergey Brin",]

#print to console
print "An epic programmer: " + epic_programmer_list[0]
print "An epic programmer: " + epic_programmer_list[1]
print "An epic programmer: " + epic_programmer_list[2]
print "An epic programmer: " + epic_programmer_list[3]
print "An epic programmer: " + epic_programmer_list[4]

## replacing a list item
# epic_programmer_list[4] = "Me"
# print epic_programmer_list

# add yourself to the end of the list
epic_programmer_list.append("Kendra Iraheta")

print "An epic programmer: " + epic_programmer_list[5]

# looping through each item in epic_programmer_list
for programmer in epic_programmer_list:
    # print the programmers' name to console
    # print programmer
    print "An epic programmer1: " + programmer

##########f##########
# lists with numbers

# create list of numbers
number_list = [1,2,3,4,5]
empty_number_list = []

# loop each number in number_list
for x in number_list:
    ## print each number to the power of 2 [** : exponent]
    # print x**2
    ## append each nunber to the power of 2 to the empty_number_list
    empty_number_list.append(x**2)

print empty_number_list
