epic_friends_dict = {
'karen russell' : ['krussell@gmail.com', 111],
'briana barrios' : ['bbarrios@gmail.com', 222],
'damariz thomas' : ['dthomas@gmail.com', 333],
'lennie rodriguez' : ['lrod@gmail.com', 444],
'yadiel bernier' : ['ybernier@gmail.com', 555]
}

# print epic_friends_dict

## grabs eniter list of dict item
# print epic_friends_dict['Karen Russell']

friend = epic_friends_dict['briana barrios']
print friend[1]

## grabs list item
print epic_friends_dict['karen russell'][0]

personsName = raw_input('Please enter a name: ').lower()
# print personsName

personsInfo = epic_friends_dict[personsName]
# print personsName

## looks up the name in the epic dictionary
try:
    ## tries the following lines of texts, and if
    ## there are no errors, then it runs
    personsInfo = epic_friends_dict[personsName]
    print 'Name: ' + personsName.title()
    print 'Email: ' + personsInfo[0]
    print 'Number: ' + str(personsInfo[1])

except:
    ## if there are errors, then this code gets run
    print 'No information found for that name'

userWantsMore = True
while userWantsMore == True:
    ## code goes here
    userWantsMore = False

## see if user wants to search again
searchAgain = raw_input('Search again? (yes/no)')
## look at what they reply and act accordingly
if searchAgain == 'yes':
    ## userWantsMore stays as true so loop repeats
    userWantsMore = True

elif searchAgain == 'no':
    ## userWantsMore turns to False to stop loop
    userWantsMore = False

else:
    ## user inputs at invalid response, so we quit anyway
    print 'I dont understand what you mean, quitting'
    userWantsMore = False
