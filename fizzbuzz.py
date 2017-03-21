"""
fizzbuzz.py
Author: Kai Darrow
Credit: http://wiki.c2.com/?FizzBuzzTest

Assignment:

Write a program that prints the numbers from 1 to 100. But for 
multiples of three print “Fizz” instead of the number and for 
the multiples of five print “Buzz”. For numbers which are multiples 
of both three and five print “FizzBuzz”.

We will use a variation of this test in which the last number of 
the series isn't necessarily 100, and the two numbers being tested 
for multiples aren't necessarily three and five. For example, your 
program should behave just like this:

How many numbers shall we print? 25
For multiples of what number shall we print 'Fizz'? 3
For multiples of what number shall we print 'Buzz'? 5
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
"""

f = input("For multiples of what number shall we print 'Fizz'? ")
b = input("For multiples of what number shall we print 'Buzz'? ")
fizz = int(f)
buzz = int(b)

"""
  if (theNumber is divisble by 3) and (theNumber is divisible by 5) then
	print "FizzBuzz"
  else if (theNumber is divisible by 3) then
	print "Fizz"
  else if (theNumber is divisible by 5) then
	print "Buzz"
  else /* theNumber is not divisible by 3 or 5 */
	print theNumber
  end if
"""

for i in range(1,101):
    if i%fizz == 0 and i%buzz == 0:
        print("FizzBuzz")
    elif i%fizz == 0:
        print("Fizz")
    elif i%buzz == 0:
        print("Buzz")
    else:
        print(i)
        
"""
I did not look at the Python examples until I had finished this challenge --
I ended up forming my code off of the BASIC-esque example provided. I found this
a lot more comfortable -- perhaps this will help me in future projects? I did 
notice that this wasn't the most efficient (though I did not have to import any commands)
but it gets the job done!
"""