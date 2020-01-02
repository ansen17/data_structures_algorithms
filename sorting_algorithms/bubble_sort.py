# Implementation of Bubble Sort
# Author: Anurag Sen 
# Date Revised: 31DEC2019

# Key Learnings:
#       Best Case Time Complexity: O(n)           -- array is already sorted
#       Worst Case Time Complexity: O(n^2)        -- array is in reverse sorted order
#       Sorting in place 
#       Space Complexity: O(1)
# You can cut down iterations in a double loop by limiting the inner loop to search between 0 and n - i
# The search becomes like this if i = 5:
# 0 1 2 3 4    run 1       
# 0 1 2 3 X    run 2
# 0 1 2 X X    run 3
# 0 1 X X X    run 4
# 0 X X X X    run 5
# X X X X X    run 6     
# 
# instead of    
# 
# 0 1 2 3 4    run 1     
# 0 1 2 3 4    run 2 
# 0 1 2 3 4    run 3 
# 0 1 2 3 4    run 4 
# 0 1 2 3 4    run 5 
# 0 1 2 3 4    run 6 
   
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

    # Alternatively: data[index_original], data[index_new] = data[index_new], holder
    return(data)

def bubble_sort(data):
    
    # To implement bubble sort, we look at two adjacent entries and check to see if they are in order
    # We do this pair wise (1 & 2, 3 & 4, etc.) until we reach the end
    # We repeat this again in the list until its all sorted
    # So outside of repeatedly swapping, we must have check on when list is entirely sorted.
    # Since we check adjacent numbers, we will push largest number all the way to the right on first pass

    swaps = True
    for i in range(len(data)):                  # range provides list default from 0 to len(data) (not inclusive of len(data))
        
        # To make it more efficient, you can stop the checks if you see no swaps after 1 cycle
        if (swaps == False):
            break
        
        # No swaps were performed at the start of the cycle
        swaps = False
        
        for j in range(0, len(data)-i-1):       # len(data)-i-1 reduces number of iterations to half of list
            if (data[j] > data[j+1]):
                swap(data, j, j+1)
                swaps = True

    return (data)


def main():
    # Create an array to sort
    data = create_array(25)

    print("------------- Original Array -------------")
    print("------------------------------------------")
    print(data)
    print("------------------------------------------")

    # Sort the given array

    sorted_data = bubble_sort(data)


    print("-------------- Sorted Array --------------")
    print("------------------------------------------")
    print(sorted_data)
    print("------------------------------------------")


if __name__== "__main__":
    main()


    
