# Part 1

my_str = input("List numbers separated by commas (ie '1,2,3,4'): ")

my_list = [int(x) for x in my_str.split(",")]
print(tuple(zip(my_list[::2],my_list[1::2])))


# Part 2a

my_str = input("List numbers separated by dashes (ie '1 - 2 - 3 -4'): ")
my_dict = {int(x):int(x)**2 for x in my_str.split("-")}
print (my_dict)


# Part 2b

state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                       'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                       'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}
    
find_state = input("Enter in a state and I will return the capital: ")

if not list(value for key,value in state_dictionary.items() if key == find_state):
    print( "Capital unknown")


# Part 2b - alt way

print(state_dictionary.get(find_state,"Capital Unknown"))


# Part 2c

my_dict = {}

# Populate the dictionary
my_str = input("Please enter a coordinate-word pair in the format (x, y, word): ").split(',')
while (len(my_str[0])>0):
    my_dict[int(my_str[0]),int(my_str[1])]=my_str[2]
    my_str = input("Please enter a coordinate-word pair in the format (x, y, word): ").split(',')

# Lookup value based on 1st 2 coordinates
my_str = input("Please enter a coordinate to look up (x,y): ")

while(my_str != 'q'):
    num1,num2 = my_str.split(',')
    print (my_dict.get((int(num1),int(num2)),"Coordinate not found"))
    my_str = input("Please enter a coordinate to look up (x,y): ")
    if (my_str == 'q'):
        break


# Part 3a

my_str = input("Please enter a list of numbers: ").split(',')
my_str2 = input("Please enter a 2nd list of numbers: ").split(',')

print (",".join(set(my_str).intersection(my_str2)))


# Part 3b
my_str = input("Please enter a list of words: ").split(',')

print (",".join(set(my_str)))


# Part 3c

my_set = set()
my_set.clear

my_str = input("Please enter in words one at a time. Press V to see all words.  Press Q to quit (word): ")
while (my_str !='q'):
    if my_str == 'v':
        print(my_set)
    else:
        my_set.add(my_str)
    my_str = input(": ")




    





 





   

