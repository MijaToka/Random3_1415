#Various ways to do the FizzBuzz test
#Fizz buzz is a group word game for children to teach them about division.
#Players take turns to count incrementally, replacing any number divisible by three with the word "fizz", 
#and any number divisible by five with the word "buzz".
#If the number is divisible both by 3 and 5 you repace the number by "fizzbuzz"

def fizzBuzzNaive():
    for i in range(1, 100 + 1):
        if i%3 ==0 and i%5 == 0:
            print('FizzBuzz')
        if i%3 == 0:
            print('Fizz')
        if i%5 == 0:
            print('Buzz')
        else: print(i)

def fizzBuzzConditional():
    for i in range(1,100 + 1):
        output = ''
        if i%3 == 0: 
            output += 'Fizz'
        if i%5 == 0: 
            output += 'Buzz'
        if output == '':
            output = i
        print(output)

def fizzBuzzNonBranching():
    for i in range(1,100 + 1):
        print(str(i) * (i%3!=0 and i%5!=0) + 'Fizz'  * (i%3==0) + 'Buzz'   * (i%5==0))

