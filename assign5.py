
# Veronica Kanczes
# Assignment 5


# Part I

# finds the longest word in the list and returns it
def find_longest_word(sentence):
    '''this function will take a string, break it
    into words using a space as a delimiter and return
    the longest word'''

    # set the intial word to smallest size possible
    longestWord = ""

    # create a list by splitting the string on each space
    words = sentence.split()

    # display the contents of the input/list
    print ("\nThe list of words entered are:\n", words)

    # iterate through each word to find the longest one
    for word in words:
        # check if next word is longer than the last
        if len(word) > len(longestWord):
                # set the word to be the new longest word
                longestWord = word
    # return the longest word
    return longestWord

# request input of words
reply = input("\nEnter a few words and I will find the longest:\n")
# call process to find the longest word and save result
result = find_longest_word(reply)
# display the longest word
print ("\nThe longest word in the list is: ", result)


# Part II

def allNumAvg(lst):
    '''this method takes a list add each value and return the average'''
    # set initial values
    avg = 0
    number = 0
    # iterate through each number in the list
    for i in lst:
        # add each new number
        number += i
    # get the average for the numbers in the list 
    avg = number / len(lst)
    # return the average
    return avg

def posNumAvg(lst):
    '''this method takes a list adds each positive value and return the average'''
    # set initial values
    avg = 0
    number = 0
    numbers = 0
    # iterate through each number in the list
    for i in lst:
        # add one to the count if the number is positive and keep track of numbers added
        if i > 0:
            number += i
            numbers += 1
    # find the average of the positive numbers
    avg = number / numbers

    # return the average
    return avg

def nonPosAvg(lst):
    '''this method takes a list adds each negative value and return the average'''
    # intialize the variables
    avg = 0
    number = 0
    numbers = 0
    # iterate through each number in the list
    for i in lst:
        # add one to the count if the number is negative and keep track of numbers added
        if i <= 0:
            number += i
            numbers += 1
    # find teh average of the negative numbers
    avg = number / numbers
    # return the average
    return avg

# set the variables and lists
num = 0
response = []

# continue to request new numbers until -9999 is entered to quit
while num > -9999:
    # get a number as input
    num = int(input("\nEnter a number (-9999 to end):"))

    # add the number to the list unless it is -9999 to quit
    if num > -9999:
          response.append(num)

# call each method
posAvg = posNumAvg(response)
nonPos = nonPosAvg(response)
allAvg = allNumAvg(response)

# dispaly the list
print ("\nThe list of all numbers entered is:\n", response)

# create a dictionary to store each result
newDict = {'AvgPositive': posAvg, 'AvgNonPos': nonPos, 'AvgAllNum': allAvg}

# display the results
print ("\nThe dictionary with averages is:\n", newDict)
