# dictionaries use curly braces { } ie:
# dictionary_name = {'item_1':1, 'item_2':2, 'item_3':3 }
# to get info from dictionary:
# print dictionary_name['item_1']

epic_programmer_dict = {'Tim Berners-Lee' : 'tbl@gmail.com',
'Guido van Rossum' : 'gvr@gmail.com',
'Linus Torvalds' : 'lt@gmail.com'}

print epic_programmer_dict['Tim Berners-Lee']

# adds a different email address
epic_programmer_dict['Tim Berners-Lee'] = 'tim@gmail.com'

print 'New email for Tim: ' + epic_programmer_dict['Tim Berners-Lee']

# add a programmer and their email to the dictionary
epic_programmer_dict['Ada Lovelace'] = 'al@gmail.com'

print epic_programmer_dict

epic_programmer_dict['Kendra Iraheta'] = 'ki@gmail.com'
epic_programmer_dict['Jenna McCarter'] = 'jc@gmail.com'

print 'New email for Kendra: ' + epic_programmer_dict['Kendra Iraheta']
print 'New email for Jenna: ' + epic_programmer_dict['Jenna McCarter']

'''print 'New email for Kendra: ' + epic_programmer_dict['Kendra Iraheta'], 'New email for Jenna: ' + epic_programmer_dict['Jenna McCarter']
print 'New email for Kendra and Jenna: ' + epic_programmer_dict['Kendra Iraheta'] + epic_programmer_dict['Jenna McCarter']
'''

# delete Linus Torvalds from the dictionary
del epic_programmer_dict['Tim Berners-Lee']

print epic_programmer_dict
