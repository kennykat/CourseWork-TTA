date = "11/12/2013"

## where there is '/'
## split string
date_manip = date.split('/')

## show outcome
# print date_manip

## shows each date on indiviual line
# print date_manip[0]
# print date_manip[1]
# print date_manip[2]

## concatenates title of date along with date
# print 'Month: ' + date_manip[0]
# print 'Day: ' + date_manip[1]
# print 'Year: ' + date_manip [2]

## OR

## don't forget of adding space after 1st quote from 2nd and third
## so outputs and titles of dates don't run together
print ('Month: ' + date_manip[0] +
'. Day: ' + date_manip[1] +
'. Year: ' + date_manip [2])
