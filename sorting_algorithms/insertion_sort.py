# Implementation of Insertion Sort
# Author: Anurag Sen 
# Date Revised: 27AUG2019

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


def insertion_sort(data):
    # Step 1: Create a loop to go through all the items in the loop

    for i in range(1, len(data)):

        # Step 2: Create another loop to take the item (data[i]) and swap elements in the left array that is sorted
        # You will need to look at every item and compare

        # Range is from the end of the left array to 0, and we work backward until we find the best insertion spot
        for j in range(i, 0, -1):
            
            # If the item you are look at is less than the item to the left of it, you will need to swap
            # Remember at one point j equaled i. So you are slowly sliding an item from the right side to the left item by item
            if (data[j] < data[j-1]):
                data = swap(data, j, j-1)

    return (data)

def main():
    # Create an array to sort
    data = create_array(25)

    print("------------- Original Array -------------")
    print("------------------------------------------")
    print(data)
    print("------------------------------------------")

    # Sort the given array

    sorted_data = insertion_sort(data)


    print("-------------- Sorted Array --------------")
    print("------------------------------------------")
    print(sorted_data)
    print("------------------------------------------")


if __name__== "__main__":
    main()


    
