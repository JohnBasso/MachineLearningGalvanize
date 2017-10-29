import numpy as np

# Normalize np array
def nomalize_np_array1(array):
        
    return ((array - [array.mean()])/[array.std()])   
    
my_array = np.arange(0,100)          # Create list of nums 1 to 100
print(nomalize_np_array1(my_array))  # Print out values of normalize array


# Normalize 2D np array
def nomalize_np_array2(array):
    
    new_array = array.astype(np.float)
       
    new_array[:,0] = (array[:,0] - [array[:,0].mean()])/[array[:,0].std()]
    new_array[:,1] = (array[:,1] - [array[:,1].mean()])/[array[:,1].std()]
    
    return (new_array)
    
print(nomalize_np_array2(np.array([[1,10],[2,954],[3,4300]])))

# Write a function that creates a numpy array of an inputted shape, filled with an inputted number. 
# Your function should have three parameters - num_cols, num_rows, and fill_value. As an example, 
# if I called your function with num_cols=4, num_rows=3, and fill_value=2, 
# then your function should output a 3 by 4 array of 2s. Return the newly created array.

def make_np_array(num_rows,num_cols,fill_value):
    
    return(np.full((num_rows,num_cols),fill_value))

print(make_np_array(4,3,2))

# Write a function that takes in a one-dimensional numpy array, an int, and a mathematical operator (either +, -, /, or *)
# as a string, and then performs the indicated operation on each element of the array, using the inputted int. 
# For example, if I inputted a numpy array, 2, and '*', you should multiply each element of the array by 2. 
# If I inputted a numpy array, 5, and '-', then you should subtract 5 from every element in the array. 
# Return the resulting array.

def my_array_calc(my_array,a_int,an_operator):
    
    #print(eval(an_operator))
    if an_operator == '+':
        my_array = my_array + a_int
    elif an_operator == '-':
        my_array = my_array - a_int
    elif an_operator == '/':
        my_array = my_array / a_int
    elif an_operator == '*':
        my_array = my_array * a_int
        
    return(my_array)
    
    
my_array = np.array([[1,2,3,4,5],[10,20,30,40,50]])

print(my_array_calc(my_array,4,"*"))

# Write a function that takes in one argument, an int, and creates a one-dimensional array
# that is the inputted number of elements long. Make the one-dimensional array full of random floating point
# numbers between 0 and 1 (Hint: Check out numpy.random.random()). Return the resulting array.

def make_np_array(an_int):
    
    return(np.random.rand(an_int,1))
    
print (make_np_array(6))

# Now, alter your solution to 5 to take in two parameters that will denote the final shape of your array of
# random floating point numbers (so now you will potentially end up with a two-dimensional array).
# Name these parameters num_rows and num_cols. Return the resulting array.

def make_np_array(rows,cols):
    
    return(np.random.rand(rows,cols))
    
print (make_np_array(10,5))

# Write a function that will take in a one-dimensional numpy array, as well as an int, and randomly sample the 
# inputted integer number of elements from the inputted array (Hint: Check out numpy.random.choice()).
# Return the randomly sampled elements.


def sample_array(my_array,samples):
    
    sample_array = np.random.choice(my_array,samples)  
    return(sample_array)
      
    
my_array = np.random.rand(20)  

print(sample_array(my_array,5))

# Write a function that will take in a one-dimensional 
# numpy array and replace the maximum element in it with a 0. Return the resulting array.


def replace_max(my_array):
    
    element = np.max(my_array)
    print("High value",element)
    element_pos = np.argmax(my_array)
    
    my_array[element_pos] = 0
    return(my_array)

    
my_array = np.random.rand(20)  

print(replace_max(my_array))

# Write a function that takes in an int, creates a one-dimensional numpy array of the numbers from 0 up to int, 
# and then returns the cumulative sum of all those numbers.

def count_for_john(max_num):
    
    array = np.arange(1,max_num)
    the_sum = np.sum(array)
    return(array,the_sum)
    
print(count_for_john(25))

# Write a function that takes in two two-dimensional numpy arrays and performs matrix multiplication, the dot product,
# between the two. You should construct it such that the first array is multiplied by the second 
# (i.e. the number of columns of the first has to equal the number of rows of the second;
# you can assume that your inputs will meet this criteria). Return the result of the multiplication.

def array_mult(array1, array2):
    mult_array = np.dot(array1,array2)
    return (mult_array)
    
array1 = np.array([[1,2],[1,1]])
array2 = np.array([[10,20],[10,10]])

print(array_mult(array1, array2))

# Write a function that takes in two two-dimensional numpy arrays and performs 
# element-wise multiplication between the two. You can assume that the two arrays are of the same size.
# Return the array resulting from the multiplication.

def array_mult(array1, array2):
    mult_array = np.multiply(array1,array2)
    return (mult_array)
    
array1 = np.array([[1,2,3],[1,1,3]])
array2 = np.array([[10,20,30],[10,10,10]])

print(array_mult(array1, array2))

# Write a function that takes in a one-dimensional numpy array and returns 
# the top 5 elements (you can assume it's an array of numbers).

def top_5(array):
    
    my_array = array[0:5]
    return (my_array)
                     
array = np.random.rand(10,1)
print("orginal array", array)
print("Top 5",top_5(array))

# Write a function that takes in a two-dimensional numpy array and returns the smallest 5 elements of each column
# (Hint: The axis parameter on the numpy function you use might come in handy here).

def smallest_values(array):
    
    array.sort(axis=0)
    print("Sorted array",array)
    my_array = array[0:5]
    return (my_array)
                     
array = np.random.rand(10,2)
print("orginal array", array)
print("Small elements in each column",smallest_values(array))