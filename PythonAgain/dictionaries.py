''' --- Dictionaries --- '''
# dictionary_name = {'item_1':1, 'item_2':2, 'item_3':3 }
#
# print dictionary_name['item_1']

sailor_senshi_dict = {'Sailor Moon' : 'usagi@gmail.com',
'Sailor Venus' : 'minako@gmail.com',
'Sailor Mercury' : 'ami@gmail.com'
}

# print sailor_sensi_dict
print sailor_senshi_dict['Sailor Venus']

# Change an email address
sailor_senshi_dict['Sailor Moon'] = 'usagichan@gmail.com'
print 'New email for Sailor Moon: ' + sailor_senshi_dict['Sailor Moon']

# Add Sailor Mars & Sailor Jupiter into email dictionary
sailor_senshi_dict['Sailor Mars'] = 'rei@gmail.com'
sailor_senshi_dict['Sailor Jupiter'] = 'makoto@gmail.com'

print sailor_senshi_dict

# Delete Sailor Jupiter from dictionary
del sailor_senshi_dict['Sailor Jupiter']

print sailor_senshi_dict
