'''
Given an integer, , perform the following conditional actions:

If N is odd, print Weird
If N is even and in the inclusive range of 2 to 5, print Not Weird
If N is even and in the inclusive range of 6 to 20, print Weird
If N is even and greater than 20, print Not Weird
'''
number = int(raw_input())

if not number % 2 and (number < 6 or number > 20):
    print 'Not',
print 'Weird'