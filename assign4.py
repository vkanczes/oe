
# Veronica Kanczes
# Assignment 4

# PART I

# Part 1 - Repeating 0-9 10 times

# iterate through each line 
for h in range(10):
    
    # iterate through each value of i
    for i in range(10):

        # add each value on the same line
        print (i, end = " ")

    # print a new line
    print ("\n")

# printing an extra line just for readability
print ("\n")

# Part 2 - Printing 10 lines each repeating the same value per line and increasing value by 1 each line

# set x to 0 to use as a repeating value
x = 0

# iterate through each line 
for h in range(10):
    # loop through i and print each value of x
    for i in range(10):

        # print the value of x to repeat same number for the entire line
        print (x, end = " ")

    # increase the value of x so a new value is printed during the next iteration
    x += 1

    # after printing each number, start a new line
    print ("\n")

# Part 3 - Printing increasing numbers up to 10 lines and increasing by 1 number each line

# set x to 0
x = 0

# iterate through each line 
for h in range(10):
    # loop through i and print each number
    for i in range(10):
        
        # add each value on the same line
        print (i, end = " ")

        # stop printing if you reach the same value
        if (i == x):
            # stop this iteration
            break

    # increase the value of x for the next loop
    x += 1

    # after printing each number, start a new line
    print ("\n")

# Part 4 - Printing increasing number up to 10 lines starting at 10 and increasing by 1 number each line
# set starting variables
x = 0
m = 10

# iterate through each line 
for h in range(10):
    
    # loop through i and print each number
    for i in range(10):
        
        # print the value of m and add on to this
        print (m, end = " ")
        m = m + 1
        # stop this iteration
        if (i == x):
            
            break

    # increase the value of x so you don't go through endless loop
    x += 1

    # after printing each number, start a new line
    print ("\n")
    


# PART II

# will take a message and encrypt it
def encryptMessage(key, message):

    encodedMsg = ""
  
    for origChar in message:

        toNum = ord(origChar)

        if (toNum + key > 126):
            encChar = ((toNum + key) -127) + 32
        else:
            encChar = (toNum + key)

        # now change back to a letter
        encodedMsg = encodedMsg + chr(encChar)

    # return the encrypted message
    return encodedMsg

# will take an encrypted message and decrypt it
def decryptMessage(key, encMsg):

    decodedMsg = ""
  
    for encChar in encMsg:

        toNum = ord(encChar)

        # make sure it is a positive number...
        if (toNum - key < 32):
            dChar = ((toNum - key) +127) - 32
        else:
            dChar = (toNum - key)

        # now change back to a letter
        decodedMsg = decodedMsg + chr(dChar)

    # return the decoded message
    return decodedMsg


# request a message to encrypt
plainMsg = input("Enter a message to encode: \n")

# request the code to use for encryption
code = input("Ener a key value (between 0 and 100) for encoding: \n")
code = int(code)

# encrypt the message
encryptedMessage = encryptMessage(code, plainMsg)

# display the message, plain and encrypted
print ("Message:  ", plainMsg)
print ("The encoded message is: ", encryptedMessage)


# ask the user for an encrypted message
encMsg = input("Enter an encrypted message to decode:  \n")

# go through each key between 1-100 and to determine message
for i in range(100):
    decMsg = decryptMessage(i, encMsg)

    # print each message to scan through to find the 'real' message
    print ("Key:  ", i, "-> Decoded Message:  ", decMsg)

        
