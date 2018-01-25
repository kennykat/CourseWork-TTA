epic_programmer_dict = {
'tim berners-lee' : ['tbl@gmail.com', 111],
'guido van rossum' : ['gvr@gmail.com', 222],
'linus torvalds' : ['lt@gmail.com', 333],
'larry page' : ['lp@gmail.com', 444],
'sergey brin' : ['sb@gmail.com', 555]
}

def searchPeople(personsName):
    # looks up the name in the dictionary
    try:
        # tries the following lines of texts,
        # and if there aren't any errors, it runs
        personsInfo = epic_programmer_dict[personsName]
        print 'Name: ' + personsName.title()
        print 'Email: ' + personsInfo[0]
        print 'Number: ' + str(personsInfo[1])

    except:
        # if there are errors, then this code gets run
        print 'No information found for that name'
userWantsMore = True
while userWantsMore == True:
    # asks user to input person name
    personsName = raw_input('Please enter a name: ').lower()
    # run our new function searchPeople with what was typed in
    searchPeople(personsName)
    userWantsMore = False

    # see if user wants to search again
    searchAgain = raw_input('Search again? (y/n)')

    # look at what they reply and act accordingly
    if searchAgain == 'y':
        # userWantsMore stays as true so loop repeats
        userWantsMore = True

    elif searchAgain == 'n':
        # userWantsMore turns to False to stop loop
        userWantsMore = False

    else:
        # user inputs an invalid response, so we quit anyway
        print "I don't understand what you mean, quitting"
        userWantsMore = False
