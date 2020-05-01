"""
CTEC 121
Matthew Bly
Programming assignment 2
code for programming assignment 2
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
import math

def main():
    
    #section 1 demo assignment statements
    print("\nSection 1: demo assignment statements")
    print("-----------")

    # create variables of several types
    MyInt = 5
    MyFloat = 3.1
    MyString = "Hello"

    # print out their values
    print("\tMyInt:", MyInt)
    print("\tMyFloat:", MyFloat)
    print("\tMyString:", MyString)

    #section 2 demo end and sep in print statements
    print("\nSection 2: demo end and sep in print statements")
    print("-----------")

    # print end and sep statements
    print('Hello', 'Matthew', sep=' - ')
    print('Hello', end='class')
    
    #section 3 demo use of escape characters
    print("\nSection 3: demo use of escape characters")
    print("-----------")

    # tab escape character
    print('\tgood morning')

    # quote escape character
    print('matthew said \"hello\" ')

    # backlash escape character
    print('\\good morning')

    #section 4 demo getting input from the user and printing value type
    print("\nSection 4: demo getting input from the user")
    print("-----------")

    # string input and value type
    aString = input("Enter a string of characters:")
    print(aString)
    aString = 'goodbye'
    print(type(aString))
    #an invalid input here would be a number 

    # integar input and value type
    aInt = int(input('Enter a number:'))
    print(aInt)
    aInt = 24
    print(type(aInt))
    # an invalid input here would be a string of words

    # float input and value type 
    aFloat = float(input('enter a number(decimals are okay):'))
    print(aFloat)
    aFloat = 7.8
    print(type(aFloat))
    # an invalid input here would be a string of words

    # eval input and value type
    aEval = eval(input('enter a number or numeric expression:'))
    print(aEval)
    aEval = 3 + 8
    print(type(aEval))


    #section 5 demo simultaneous assignment
    print("\nSection 5: demo simultaneous assignment")
    print("-----------")

    # simultaneous assignment using assignment statement
    sum = 7 + 10
    print(sum)

    # simultaneous assignment using input
    x, y = input("provide two values: ").split()
    print(x, y)

    #section 6 demo integar arithmatic
    print("\nSection 6: demo integar arithmatic")
    print("-----------")
    
    # output of quotient
    print(5//2)

    # output of remainder
    print(5 % 2)
    
    #section 7 demo definite loops
    print("\nSection 7: demo definite loops")
    print("-----------")
    
 
    #definite loop using list
    for i in [11, 14, 21, 90]:
        print(i)
    print()

    #definite loop using range
    for count in range(8):
        print(count)  
    print()

    #output for every 3rd number starting at 11 for 5 iterations 
    for i in range(11,26,3):
        print(i)
    
    #section 8 demo math library functions
    print("\nSection 8: demo math library functions")
    print("-----------")

    # value of pi
    print(math.pi)

    # squre root function
    print(math.sqrt(25))

    # ceil function
    print(math.ceil(9.532)) 

    # floor function
    print(math.floor(9.532))

    # squre a value
    print(8**2)
    print("eight squared is sixty four")

    # cube a value
    print(8**3)
    print('eight cubed is five hundred and 12')

    #section 8 demo accumulator pattern
    print("\nSection 9: demo accumulator pattern")
    print("-----------")

    # accumlator pattern using sum of values
    sum = 0
    for i in [40, 34, 77, 52]:
        print(i)
        sum = sum + i
    print("----")
    print(sum)

    # accumulator pattern using sum of squared values
    sum = 0
    for i in [40**2, 34**2, 77**2, 52**2]:
        print(i)
        sum = sum + i
    print("----")
    print(sum)

main()    