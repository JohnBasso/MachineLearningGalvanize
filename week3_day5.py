
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







        