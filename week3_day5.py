
# Part 1a - Function that calculates all divisors
def all_divisors(num):

    my_list = []
    
    for i in range(1,num+1):
        if num % i == 0:
            my_list.append(i)
                               
    return (my_list)

print(all_divisors(10))

# Part 1b - Function that calculates LCM
def lcm(multiple_num,max_num):

    common_list = []
   
    for i in range(0,max_num,multiple_num):
        common_list.append(i)
                               
    return (common_list)

print(lcm(5,100))

# Part 2a
def beers_left(num):

    if num == 0:
        return"No beers left"
    else:
        return"Beers left"

beers_left(1)

# Part 2b
def elsa_fans(name):

    return(name in {'Cary', 'Josh', 'Sean'})

elsa_fans('Cary')

elsa_fans('Jack')

# Part 2c

def my_sum(list_of_nums):
    
    y = 0
    for x in list_of_nums.split(','):
        y += int(x)   
    return(y)
    
my_sum('2,3,4')


# Part 2d
# used strings for this sample
def my_sum(list_of_nums):
    
    y = 0
    for x in list_of_nums.split(','):
        y *= int(x)   
    return(y)
    
my_sum('2,3,4')


# Park 2e
# Used list of numbers for this sample
def my_mult(list_of_nums):
    
    y = 1
    for x in list_of_nums:
        y *= int(x)   
    return(y)
    
my_mult([2,3,4])

# Part 2f
def find_even_numbers(list_of_nums):

    my_list = []
    
    for i in list_of_nums:
        if i % 2 == 0:
            my_list.append(i)
        
    return (my_list)

print(find_even_numbers([1,2,3,4,5,6]))

# Advanced Assignments
# 2a - count words divided by space.  Test at least 5 times
def count_words(list_of_words):
    
    my_count = 0
    
    for i in list_of_words.split(' '):
        if i != '':  # skip over words that were split but only contain a space themselves
            my_count += 1
        
    return (my_count)

print(count_words("The end of the world is near."))
print(count_words(" Test a leading space"))
print(count_words("Test a trailing space "))
print(count_words("Test  random   spaces all over"))
print(count_words("Testnospaces"))
print(count_words(""))  # Test empty string

# Advanced Assignments
# 2b - count words with a passed in delimeter

def count_words(list_of_words,delimeter=' '):
    
    my_count = 0
    
    for i in list_of_words.split(delimeter):
        if i != delimeter and i != "":  # skip over words that were split by multple delimeter
            my_count += 1
        
    return (my_count)

print(count_words("Test|delimeter|of|bar.","|"))
print(count_words(" Test-a-dash","-"))
print(count_words("Test,a,comma,2x",","))
print(count_words("Test_underscore_now","_"))
print(count_words("Testemptydelimeter",))
print(count_words(""))  # Test empty string

# Advanced Assignments
# 2c - Count the len of each word with a passed in delimeter

def word_count_lens(list_of_words,delimeter=' '):
    
    list_of_word_counts = []
    
    for i in list_of_words.split(delimeter):
        if i != delimeter and i != "":  # skip over words that were split by multple delimeter
            my_count = 0
            for j in i:
                my_count += 1
            list_of_word_counts.append(my_count)
        
    return (list_of_word_counts)

print(word_count_lens("Test|delimeter|of|bar.","|"))
print(word_count_lens(" Test-a-dash","-"))
print(word_count_lens("Test,a,comma,2x",","))
print(word_count_lens("Test_underscore_now","_"))
print(word_count_lens("Testemptydelimeter",))
print(word_count_lens(""))  # Test empty string

# Advanced Assignments
# 2d - Count the len of each word with a passed in delimeter
        
def calc_prime(up_to_num):

    if up_to_num == 2:
        return(2)

    prime_list = []
  
    for i in range(1,up_to_num,2): # Prime can only be even except for the number 2
        if up_to_num % i == 0:
            prime_list.append(i)
          
    return(prime_list)

print(calc_prime(55))
print(calc_prime(0))
print(calc_prime(-20))
print(calc_prime(2))
print(calc_prime(1))
print(calc_prime(1000))

# Advanced Assignments
# 2e - Determine if a list of numbers can be divided by a passed in parm

def list_to_divide_by(list_of_nums,num_to_divide_by):
    
    if num_to_divide_by == 0:
        return("Sorry can't divide by 0")
    
    dividable_results = []
    
    for i in list_of_nums:
        if i != 0:
            if i % num_to_divide_by == 0:
                dividable_results.append("yes")
            else:
                dividable_results.append("no")
        else:
            dividable_results.append("n/a")
        
    return (dividable_results)

print(list_to_divide_by([10, 25, 36, 12, 20],5))
print(list_to_divide_by([10, 25, 36, 12, 20],0))
print(list_to_divide_by([0, 25, 36, 12, 20],5))
print(list_to_divide_by([4],4))
print(list_to_divide_by([10,20,30],1000))

# Advanced Assignments
# 2f - Check to see if a list of words ends with a specific character

def check_for_a_char_at_end(list_of_words,char_to_look_for):

    result_list = []
    
    for i in list_of_words:
        if str(i).endswith(char_to_look_for):
            result_list.append(i)
            
    return(result_list)

print(check_for_a_char_at_end(['I','am','in','love','with','python'],'n'))
print(check_for_a_char_at_end(['I','will','back','back','with'],'l'))
print(check_for_a_char_at_end(['The','end','is','near'],'z'))
print(check_for_a_char_at_end(['x','y','z','z','z'],'z'))
print(check_for_a_char_at_end([''],'n'))


# Advanced Assignments
# 2g - Check to see if a list of words ends with a specific string. Return position

def check_for_a_char_at_end(list_of_words,char_to_look_for):

    result_list = []
    
    for en, i in enumerate(list_of_words):
        if str(i).endswith(char_to_look_for):
            result_list.append(en)
            
    return(result_list)

print(check_for_a_char_at_end(['I','am','in','love','with','python'],'in'))
print(check_for_a_char_at_end(['I','will','back','back','with'],'l'))
print(check_for_a_char_at_end(['The','end','is','near'],'z'))
print(check_for_a_char_at_end(['x','y','z','z','z'],'z'))
print(check_for_a_char_at_end([''],'n'))

        