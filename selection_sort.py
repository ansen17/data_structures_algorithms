# Implementation of Selection Sort
# Author: Anurag Sen 
# Date Revised: 27AUG2019

# Import Relevant Packages
import numpy as np

def create_array(size_of_array, upper_bound = 100):
    arr = np.random.randint( low=1, high=upper_bound, size = size_of_array)
    return arr

def compare_to(object_1, object_2):
    # TO-DO: Establish a function that will compare objects instead of just integers or strings
    return -1

def swap(data, index_original, index_new):
    holder = data[index_original]
    data[index_original] = data[index_new]
    data[index_new] = holder
    return(data)


def selection_sort(data):
    for index in range(len(data)):
        min_index = index

        for checking_index in range (index+1, len(data)):
            if (data[checking_index] < data[min_index]):
                min_index = checking_index
        data = swap(data, index, min_index)
    return(data)


def main():
    # Create an array to sort
    data = create_array(25)

    print("------------- Original Array -------------")
    print("------------------------------------------")
    print(data)
    print("------------------------------------------")

    # Sort the given array

    sorted_data = selection_sort(data)


    print("-------------- Sorted Array --------------")
    print("------------------------------------------")
    print(sorted_data)
    print("------------------------------------------")


if __name__== "__main__":
    main()


    