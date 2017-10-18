# Problem #1
# Determine if a number is positive, negative or zero
def pos_neg_test ():

    var1 = int(input("Please input a whole number "))

    if var1 > 0:
        print('Positive')
    elif var1 < 0:
        print('Negative')
    else:
        print('Zero')


# Problem #2
# Determine which number is larger
def which_is_larger ():
    
    var1 = float(input("Please enter in the first number "))
    var2 = float(input("Please enter in the second number "))

    if var1 > var2:
        print("The first number is larger")
    elif var2 > var1:
        print("The second number is larger")
    else:
        print("Neither number is larger")


# Problem #3
# Sum from number entered to 0
def sum_from_input_to_zero():

    var1 = int(input("Please enter in the number you want to sum to zero "))
    current = var1
    sum_result = 0

    while current > 0:
        sum_result += current
        current -= 1
    print(sum_result)


# Problem #4
# Factorial
def my_factorial():

    var1 = int(input("Please enter in the number you want to calculate the factorial of "))
    current = var1
    fact_result = 1

    while current > 0:
        fact_result *= current
        current -= 1
    print(fact_result)


# Problem #5
# Divisor
def my_divisor():

    var1 = int(input("Please enter in the number you want determine the divisors of "))
   
    current = var1
    
    while current > 0:
        if var1 % current == 0:
            print(current)

        current -= 1
   
 
# Problem #6
# Greatest common divisor 
def greatest_common_divisor():

    var1 = int(input("Please enter in the first number you want determine the gcd of "))
    var2 = int(input("Please enter in the second number you want determine the gcd of "))
 
    if var1 > var2:      #find the largest number and start with it
        current = var2
    else:
        current = var1
    
    while current > 0:
        if var1 % current == 0 and var2 % current == 0:
            print(current)
            break   # Did this to see if the teach was looking.  Considered in bad taste to use breaks

        current -= 1

# Problem #7  
# least common multiple 
def least_common_multiple():

    var1 = int(input("Please enter in the first number you want determine the lcm of "))
    var2 = int(input("Please enter in the second number you want determine the lcm of "))

    loop_counter = 0     # Keep track of current position in loop 
    loop_limit = 100     # Fail safe in case there is no LCM.  Just in case.  Not really needed.
    lcm = 0              # Lowest common multiplier
    current_num1 = 0
    current_num2 = 0

    num1_multiplier = 1
    num2_multiplier = 1
 
    if var1 < var2:      # find the smallest number 
        init_num1 = var1
        current_num2 = var1
        init_num2 = var2
        current_num2 = var2
    else:
        init_num1 = var2
        current_num1 = var2
        init_num2 = var1
        current_num2 = var1

    while loop_counter < loop_limit:
        loop_counter += 1
        if current_num1 == current_num2:
            lcm = current_num1
            print(lcm)
            loop_counter = loop_limit  # exit loop 
        elif current_num1 < current_num2:
            num1_multiplier += 1
            current_num1 = init_num1 * num1_multiplier
        else:
            num2_multiplier += 1
            current_num2 = init_num2 * num2_multiplier
  
    if current_num2 != current_num1:        # If no solutions found
        print("No solution available within tolerance limits")


# Problem #8
# Determine if the number entered is a prime number 
def is_prime():

    var1 = int(input("Please enter a number to determine if it is a prime "))

    # check to see if positive here, if not make positive
    if var1 < 0:
        var1 *= -1
        print("Making number positive")

    loop_counter = var1 - 1 

    while loop_counter >= 1 and var1 % loop_counter != 0:
        loop_counter -= 1
          
    if loop_counter == 1:
        print("Number entered is a prime")
    else:
        print("Number entred is not a prime")


# Problem #9
# Find number in a series
def find_num_in_series():

    var1 = int(input("How far into the series do you want to calculate "))

    loop_counter = 0
    current_value = 0

    while(loop_counter < var1):
        loop_counter += 1
        current_value = 2 * current_value + 1   #fomula 

    print(current_value)
    

# Problem #10
# Solve equation
# Note: I added a list so I can check for any possible number with multiple answers.
#       Technically the homework only had one possible answer so list not needed
def solve_equation():

    var1 = int(input("Enter value to check for 1 to 6 in 6 loops uniquely solves "))

    answers = []    # This is how to define an empty list
    
    for a in range(1,7):   # Have to use 7 because 7 indicates 1 to 6
         for b in range(1,7):
            for c in range(1,7):
                for d in range(1,7):
                    for e in range(1,7):
                        for f in range(1,7):
                            
                            if ((a + (b-c) * d -e) * f) == var1:
                                # Make sure the number are unique from each other.  Sloppy but it works
                                if a not in(b,c,d,e,f) and b not in(c,d,e,f) and c not in(d,e,f) and d not in(e,f) and e != f:  
                                    if (a,b,c,d,e,f) not in answers:
                                        # Add this answer to the list
                                        answers.append([a,b,c,d,e,f])    
                                

    print(answers)
                               

    
# Main 
# Created a small case statement so the program can be run to test all the problems

print ("How can I help you?")
print ("")
print ("Select 1 to check if number is Positive, Negative or Zero")
print ("Select 2 to see which of two numbers is larger")
print ("Select 3 to sum from inputed number to zero")
print ("Select 4 to calculate the factorial of a number")
print ("Select 5 to detemine a numbers divisors") 
print ("Select 6 to determine the greatest common divisor")
print ("Select 7 to determine the least common multiple")
print ("Select 8 to determine if the number entered is a prime number")
print ("Select 9 to find number in a series")
print ("Select 10 to solve equation")

# determine what task the user wants to do

var0 = int(input('What do you want to do? ')) 
if var0 == 1:
    pos_neg_test()  
elif var0 == 2:
    which_is_larger()
elif var0 == 3:
    sum_from_input_to_zero()
elif var0 == 4:
    my_factorial()
elif var0 == 5:
    my_divisor()
elif var0 == 6:
    greatest_common_divisor()
elif var0 == 7:
    least_common_multiple()    
elif var0 == 8:
    is_prime()   
elif var0 == 9:
    find_num_in_series()
elif var0 == 10:
    solve_equation()
else:
    print("Not a valid option. Please start over. ")





