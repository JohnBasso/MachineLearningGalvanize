import time    # Used to keep track of how long functions take

# Factorial - V2 using for for loop instead of while loop
def my_factorial(var1):
    
    result = 1
      
    for i in range(var1,1,-1):    # If you go backwards in the loop you don't have +1 the end value
        result *= i

    return(result)

# Prime number - V2 using for loops instead of while loop_counter
# Determine if the number entered is a prime number 
def is_prime(var1):

    if var1 == 2:
        return(True)
  
    for i in range(1,var1,2): # Prime can only be even except for the number 2
        if var1 % i == 0:
            return(False)
          
    return(True)

# Determine how many times a character is in a string regardless of case
def count_chars(char_to_find,string_to_search):
    
    char_count = 0
    
    for i in string_to_search:
        if i.lower() == char_to_find:
            char_count += 1
         
    return(char_count)

# Determine to cap or lower case a phrase based on a ! at the end of the phrase
def shout_or_not(phrase_to_analyze):

    if phrase_to_analyze.endswith("!"):
        return(phrase_to_analyze.upper())
    else:
        return(phrase_to_analyze.lower())


# Remove all the vowels from a string 
def remove_vowels(string_to_analyze):

    vowelless_str = []

    for char_to_keep in string_to_analyze:
        if char_to_keep not in ('a','e','i','o','u','y','A','E','I','O','U','Y'):
            vowelless_str += char_to_keep
          
    return ("".join(vowelless_str))


# Cap ever other letter 
def phrase_to_cap(string_to_analyze):

    alt_str = []
    
    for i,char_to_keep, in enumerate(string_to_analyze):
        if i % 2 == 0:
            alt_str += char_to_keep.upper()
        else:
            alt_str += char_to_keep.lower()
                       
    return ("".join(alt_str))

# Find all even number up to the number 
def find_even_numbers(max_num):

    my_list = []
    
    for i in range(0,max_num+1,2):
        my_list.append(i)
                               
    return (my_list)

# Find all numbers divisible up to the number entered
def find_numbers_divisible(max_num):

    my_list = []
    
    for i in range(1,max_num+1):
        if max_num % i == 0:
            my_list.append(i)
                               
    return (my_list)

# Sort two lists
def sort_two_lists():

    list1 = [0, 3, 6, 9, 10, 2, 5]
    list2 = [2, 6, 4, 7, 8, 1, 15]
    common_list = []
   
    list1.sort()
    list2.sort()

    for i in (list1):
        if i in list2:
            common_list.append(i)
                               
    return (common_list)

def multiple_up_to_max(multiple_num,max_num):

    common_list = []
   
    for i in range(0,max_num,multiple_num):
        common_list.append(i)
                               
    return (common_list)

def sort_two_lists_custom():
    
    list1 = []
    list2 = []

    for i in range (1,8):
        var1 = int(input("Enter in a value for list 1 "))
        list1.append(var1)


    for i in range (1,8):
        var2 = int(input("Enter in a value for list 2 "))
        list2.append(var2) 

    common_list = []
   
    list1.sort()
    print (list1)
    list2.sort()
    print (list2)

    for i in (list1):
        if i in list2:
            common_list.append(i)
                               
    return (common_list)
        
         
# Main

print ("How can I help you?")
print ("")
print ("Select 1 to calculate the factorial of a number")
print ("Select 2 to see if the number is a prime number")
print ("Select 3 to find how many times a letter appears in a seriers of letters")
print ("Select 4 to see if you should shout a phase out")
print ("Select 5 to remove all vowels")
print ("Select 6 to alt between upper and lower case")
print ("Select 7 to find all even numbers up to number entered")
print ("Select 8 to find all numbers divisible up to number entered")
print ("Select 9 to sort two lists")
print ("Select 10 to find multiple of a number up to a max")
print ("Select 11 to enter two list and sort them and find common elements")


# determine what task the user wants to do

var0 = int(input('What do you want to do? ')) 

if var0 == 1:
    var1 = int(input("Please enter in the number you want to calculate the factorial of: "))
    start_time = time.time()
    for loop in range(1000):
        answer = my_factorial(var1) 
    print(answer) 
    print(time.time()-start_time)

elif var0 == 2:
    var1 = int(input("Please enter a number to determine if it is a prime: "))
    start_time = time.time()
    for loop in range(1000):
        answer = is_prime(var1) 
    print(answer) 
    print(time.time()-start_time)

elif var0 == 3:
    char_to_find = input("Please enter a single character: ")
    string_to_search = input("Please enter a seriers of charaters: ")
    start_time = time.time()
    for loop in range(1000):
        answer = count_chars(char_to_find,string_to_search) 
    print(answer) 
    print(time.time()-start_time)

elif var0 == 4:
    phrase_to_analyze = input("Please enter a word with or without a ! at the end ")
    start_time = time.time()
    for loop in range(1000):
        answer = shout_or_not(phrase_to_analyze) 
    print(answer) 
    print(time.time()-start_time)
    
elif var0 == 5:
    string_to_analyze = input("Please enter a phase to have it vowels removed ")
    start_time = time.time()
    for loop in range(1000):
        answer = remove_vowels(string_to_analyze) 
    print(answer) 
    print(time.time()-start_time)

elif var0 == 6:
    string_to_modify = input("Please enter a phase have every other letter capitalized ")
    start_time = time.time()
    for loop in range(1000):
        answer = phrase_to_cap(string_to_modify) 
    print(answer) 
    print(time.time()-start_time)

elif var0 == 7:
    max_num = int(input("Please enter a number to find even numbers up to "))
    start_time = time.time()
    for loop in range(1000):
        answer = find_even_numbers(max_num) 
    print(answer) 
    print(time.time()-start_time)
        
elif var0 == 8:
    max_num = int(input("Please enter a number to find numbers divisible up to "))
    start_time = time.time()
    for loop in range(1000):
        answer = find_numbers_divisible(max_num) 
    print(answer) 
    print(time.time()-start_time)  

elif var0 == 9:
    start_time = time.time()
    for loop in range(1000):
        answer = sort_two_lists() 
    print(answer) 
    print(time.time()-start_time) 

elif var0 == 10:
    multiple_num= int(input("Please enter a number to find multiples of "))
    max_num = int(input("Please enter a max number "))
    start_time = time.time()
    for loop in range(1000):
        answer = multiple_up_to_max(multiple_num,max_num) 
    print(answer) 
    print(time.time()-start_time) 

elif var0 == 11:
   
    answer = sort_two_lists_custom() 
    print(answer) 
    
else:
    print("Not a valid option. Please start over. ")