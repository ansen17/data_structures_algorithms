# Implementation of Insertion Sort
# Author: Anurag Sen 
# Date Revised: 02SEP2019

# Import Relevant Packages
import numpy as np

def create_array(size_of_array, upper_bound = 100):
    arr = np.random.randint( low=1, high=upper_bound, size = size_of_array)
    return arr

def compare_to(object_1, object_2):
    # TO-DO: Establish a function that will compare objects instead of just integers or strings
    # TO-DO: create helper function to check if the array is completely sorted or not
    return -1

def swap(data, index_original, index_new):
    holder = data[index_original]
    data[index_original] = data[index_new]
    data[index_new] = holder
    return(data)


def shell_sort(data):
    # Step 1: Create a loop to go through all the items in the loop

    length_of_data = len(data)
    for i in range(1, length_of_data):



    return (data)

def main():
    # Create an array to sort
    data = create_array(25)

    print("------------- Original Array -------------")
    print("------------------------------------------")
    print(data)
    print("------------------------------------------")

    # Sort the given array

    sorted_data = shell_sort(data)


    print("-------------- Sorted Array --------------")
    print("------------------------------------------")
    print(sorted_data)
    print("------------------------------------------")


if __name__== "__main__":
    main()


    
