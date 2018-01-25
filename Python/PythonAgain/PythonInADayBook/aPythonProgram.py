sailor_senshi_dict = {'sailor moon' : ['usagi@gmail.com', 111],
'sailor venus' : ['minako@gmail.com', 222],
'sailor mercury' : ['ami@gmail.com', 333],
'sailor mars' : ['rei@gmail.com', 444],
'sailor jupiter' : ['makoto@gmail.com', 555]
}

def searchPeople(sailorsName):
    # searches in dictionary
    try:
        sailorsInfo = sailor_senshi_dict[sailorsName]
        print 'Name: ' + sailorsName.title()
        print 'Email: ' + sailorsInfo[0]
        print 'Number: ' + str(sailorsInfo[1])
    except:
        print 'No information found for that sailor'

userWantsMore = True
while userWantsMore == True:
    sailorsName = raw_input('Please enter a name: ').lower()

    searchPeople(sailorsName)
    userWantsMore = False

    searchAgain = raw_input('Search again? (y/n)')
    if searchAgain == 'y':
        userWantsMore = True
    elif searchAgain == 'n':
        userWantsMore = False
    else:
        print "I don't understand what you mean, quitting..."
        userWantsMore = False
