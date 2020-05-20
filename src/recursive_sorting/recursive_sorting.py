# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    #combined length of the two arrays
    elements = len(arrA) + len(arrB) 
    # #A wiht singular 0 and times it by the length of the arrays
    merged_arr = []
    # Your code here
    i = 0
    j = 0
    while len(merged_arr) < elements:
        if i >= len(arrA):
            merged_arr.append(arrB[j])
            j+=1
        elif j >= len(arrB):
            merged_arr.append(arrA[i])
            i+=1
        elif arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i+=1
        else:
            merged_arr.append(arrB[j])
            j+=1

    # print(elements)
    # Your code here
    # for i in range(0, len(merged_arr)):
    #     if not arrA or arrA[0] > arrB[0]:
    #         merged_arr[i] = arrB.pop(0)
    #     elif not arrB or arrB[0] > arrA[0]:
    #         merged_arr[i] = arrA.pop(0)
   

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
#

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    lower = merge_sort(arr[:len(arr) // 2])
    higher = merge_sort(arr[len(arr) // 2:])

    return merge(lower, higher)

##THIS DOES IT ALL IN ONE FUNCTION
# def merge_sort(arr):
#     # Your code here
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         l = arr[:mid]
#         r = arr[mid:]

#         merge_sort(l)
#         merge_sort(r)

#         i = j = k = 0

#         while i < len(l) and j < len(r):
#             if l[i] < r[j]:
#                 arr[k] = l[i]
#                 i+=1
#             else:
#                 arr[k] = r[j]
#                 j+=1
#             k+=1
        
#         while i < len(l):
#             arr[k] = l[i]
#             i+=1
#             k+=1
        
#         while j < len(r):
#             arr[k] = r[j]
#             j+=1
#             k+=1

#     return arr


# implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    start2 = mid + 1
    #base case: if the array is already sorted
    if (arr[mid] <= arr[start2]): 
        return
    while (start <= mid and start2 <= end): #sets the pointers for the values to sort each other
        if (arr[start] <= arr[start2]): 
            start += 1
        else: 
            value = arr[start2]
            index = start2
            while (index != start): #shifts all the values over each other by 1
                arr[index] = arr[index - 1] 
                index -= 1
            arr[start] = value
            #increment the pointers to the next value
            start += 1
            mid += 1
            start2 += 1
    return arr

# def merge_in_place(arr, start, mid, end):
#     # Your code here
#     L = arr[start:mid]
#     R = arr[mid:end]
#     i = 0
#     j = 0
#     k = start
#     for l in range (k, end):
#         if j >= len(R) or (i < len(L) and L[i] < R[j]):
#             arr[l] = L[i]
#             i = i + 1
#         else: 
#             arr[l] = R[j]
#             j = j + 1

#     return arr

def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r): 
        m = l + (r - l) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)
    return arr

# def merge_sort_in_place(arr, l, r):
#     # Your code here
#     if r - l > 1: 
#         mid = int((l + r) / 2)
#         merge_sort_in_place(arr, l, mid)
#         merge_sort_in_place(arr, mid, r)
#         merge_in_place(arr, l, mid, r)

#     return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [2]
arr4 = [0, 1, 2, 3, 4, 5]
arr5 = [5, 6, 7]
arr6 = [3, 8, 4]

print("merge function", merge(arr6, arr5))
print(arr6, "arr6")
print(arr5, "arr5")