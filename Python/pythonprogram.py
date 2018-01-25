sailor_senshi_dict = {'sailor moon' : ['usagi@gmail.com', 111],
'sailor venus' : ['minako@gmail.com', 222],
'sailor mercury' : ['ami@gmail.com', 333],
'sailor mars' : ['rei@gmail.com', 444],
'sailor jupiter' : ['makoto@gmail.com', 555]}

print sailor_senshi_dict
print sailor_senshi_dict['sailor venus']
print sailor_senshi_dict['sailor mercury'][0]

senshi = sailor_senshi_dict['sailor jupiter']
print senshi[1]

''' ---  raw_input() function --- '''

sailorsName = raw_input('Please enter a name: ').lower()
print sailorsName

# sailorsInfo = sailor_senshi_dict[sailorsName]
# print sailorsInfo

# # Looks up the name in the epic dictionary
# try:
#     # tries the next lines; if no errors will run
#     sailorsInfo = sailor_senshi_dict[sailorsName]
#     print sailorsInfo
# except:
#     # if errors exist; this code runs
#     print 'No information found for that sailor'

''' - - - '''

try:
    # tries the next lines; if no errors will run
    sailorsInfo = sailor_senshi_dict[sailorsName]
    print 'Name: ' + sailorsName.title()
    print 'Email: ' + sailorsInfo[0]
    print 'Number: ' + str(sailorsInfo[1])
except:
    # if errors exist; this code runs
    print 'No information found for that sailor'

userWantsMore = True

while userWantsMore == True:
    userWantsMore = False
