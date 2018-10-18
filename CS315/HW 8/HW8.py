from random import randint
import sys

#           functions to generate the input 

totalcomps = 0 #holds total for averaging (random arrays)

#backwards
def generate1(n):
    new_list = []
    for i in range(0, n-1):
        new_list.append(i+1)
    new_list.reverse()
    return new_list

#sorted
def generate2(n):
    new_list = []
    for i in range(0, n-1):
        new_list.append(i+1)
    return new_list

#swapped pairs
def generate3(n):
    new_list = []
    for i in range(0, n-1):
        new_list.append(i+1) 
    for i in range(0, n-2, 2):
        temp = new_list[i]
        new_list[i] = new_list[i+1]
        new_list[i+1] = temp
    return new_list
    
#random order
def generate4(n):
    new_list = []
    for i in range(0, n-1):
        new_list.append(randint(0, 999999))
    return new_list

#        selection sort    
    
def selection_sort(a_list):
    comps = 0
    for i in range(0, len(a_list)-1):
        min_index = i;
        for j in range(i+1, len(a_list)):
            comps += 1
            if (a_list[j] < a_list[min_index]):
                min_index = j
        comps += 1
        if (min_index != i):
            comps += 1
            temp = a_list[i]
            a_list[i] = a_list[min_index]
            a_list[min_index] = temp
    print("Sorted Array: ", a_list, "\n Comparisons: ", comps)
    
#        insertion sort

def insertion_sort(a_list):
    comps = 0
    for i in range(1, len(a_list)):
        key = a_list[i]
        position = i
        comps += 1
        while (position > 0 and a_list[position-1] > key):
            comps += 1
            a_list[position] = a_list[position-1]
            position -= 1
        a_list[position] = key
    print("Sorted Array: ", a_list, "\n Comparisons: ", comps)
    
#        random pivot quick sort

def quick_sort_rand(a_list):
    compa = [0]
    quick_sort_helper_rand(a_list, 0, len(a_list)-1, compa)
    print("Sorted Array: ", a_list, "\n Comparisons: ", compa[0])    

def quick_sort_helper_rand(a_list, left, right, compa):
    if (left<right):
        pivot = randint(left, right)
        temp = a_list[right]
        a_list[right] = a_list[pivot]
        a_list[pivot] = temp
        
        pivot = partition_rand(a_list, left, right, compa)
        quick_sort_helper_rand(a_list, left, pivot-1, compa)
        quick_sort_helper_rand(a_list, pivot+1, right, compa)    
    
def partition_rand(a_list, left, right, compa):
    pivot = randint(left, right)
    temp = a_list[right]
    a_list[right] = a_list[pivot]
    a_list[pivot] = temp
    newPivotIndex = left-1
    for index in range(left, right):
        compa[0] += 1
        if (a_list[index] < a_list[right]):
            newPivotIndex = newPivotIndex+1
            temp = a_list[newPivotIndex]
            a_list[newPivotIndex] = a_list[index]
            a_list[index] = temp
    temp = a_list[newPivotIndex+1]
    a_list[newPivotIndex+1] = a_list[right]
    a_list[right]=temp    
    
    return newPivotIndex+1

#        first element pivot quick sort
    
def quick_sort_first(a_list):
    compa = [0]
    quick_sort_helper_first(a_list, 0, len(a_list)-1, compa)
    print("Sorted Array: ", a_list, "\n Comparisons: ", compa[0])
    
def quick_sort_helper_first(a_list, first, last, compa):
    if (first < last):
        split = partition_first(a_list, first, last, compa)
        quick_sort_helper_first(a_list, first, split-1, compa)
        quick_sort_helper_first(a_list, split+1, last, compa)

def partition_first(a_list, first, last, compa):
    pivot = a_list[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while (left <= right and a_list[left] <= pivot):
            compa[0] +=1
            left += 1
        while (a_list[right] >= pivot and right >= left):
            compa[0] +=1
            right -= 1
        compa[0] +=1
        
        if (right < left):
            done = True
        else:
            temp = a_list[left]
            a_list[left] = a_list[right]
            a_list[right] = temp
    temp = a_list[first]
    a_list[first] = a_list[right]
    a_list[right] = temp     
    
    return right

#         merge sort

def merge_sort(a_list, compa):
    global totalcomps
    if (len(a_list)>1):
        mid = len(a_list)//2
        lefthalf = a_list[:mid]
        righthalf = a_list[mid:]
        merge_sort(lefthalf, compa)
        merge_sort(righthalf, compa)
        i=0
        j=0
        k=0
        while (i < len(lefthalf) and j < len(righthalf)):
            compa[0] += 1
            if (lefthalf[i] < righthalf[j]):
                a_list[k] = lefthalf[i]
                i += 1
            else:
                a_list[k]=righthalf[j]
                j += 1
            k += 1
        while (i < len(lefthalf)):
            compa[0] += 1
            a_list[k]=lefthalf[i]
            i += 1
            k += 1
        while (j < len(righthalf)):
            compa[0] += 1
            a_list[k]=righthalf[j]
            j += 1
            k += 1
            
        totalcomps += compa[0] 

#           the main

def main():
    
    global totalcomps
    sys.setrecursionlimit(10000)    #in case the recursion exceeds python's std limit
    
    done = False
    while (done == False):
        totalcomps = 0        
        
        alg_select = input("Enter the algorithm you want to test (1-5): ")
        arrayType_select = input("The type of input array (1-4): ")
        n_select = input("What value for n (any integer)? ")
            
        if (arrayType_select == "1"):
            a_list = generate1(int(n_select))
        elif (arrayType_select == "2"):
            a_list = generate2(int(n_select))   
        elif (arrayType_select == "3"):
            a_list = generate3(int(n_select))
        elif (arrayType_select == "4"):
            a_list = generate4(int(n_select))
        
        if (alg_select == "1"):
            print("Unsorted Array: ", a_list)
            selection_sort(a_list)
        elif (alg_select == "2"):
            print("Unsorted Array: ", a_list)
            insertion_sort(a_list)
        elif (alg_select == "3"):
            print("Unsorted Array: ", a_list)
            quick_sort_rand(a_list)
        elif (alg_select == "4"):
            print("Unsorted Array: ", a_list)
            quick_sort_first(a_list)
        elif (alg_select == "5"):
            print("Unsorted Array: ", a_list)
            compa = [0]
            merge_sort(a_list, compa)
            print("Sorted Array: ", a_list, "\n Comparisons: ", compa[0])
        
        input("Hit any key to continue: \n")
        
main()