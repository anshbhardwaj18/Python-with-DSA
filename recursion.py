# BASIC OF RECURSION
# def fun(n):
#     if n == 0: #BASE CASE
#         return 
#     print(n)
#     fun(n -1) #RECURSIVE CASE
# fun(5)

# MERGE SORTED ARRAY(USING TWO POINTER APPROACH)
def merge(nums1, m, nums2, n):

    i = m - 1
    j = n - 1
    k = m + n -1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1

        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

merge(nums1, 3, nums2, 3)
print(nums1)

# REMOVE ELEMENT (TWO POINTERS APPROACH)
def remove(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [3, 2, 2, 3]
k = remove(nums, 2)
print(k)
print(nums)

# REMOVE DUPLICATE FROM AN ARRAY(TWO POINTER APPROACH)
def removeduplicate(nums):
    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k += 1

    return k

nums = [0, 1, 1, 2, 2, 3, 4, 5]

k = removeduplicate(nums)
print(nums[:k])