
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # edge cases: nums1 is empty, nums2 is empty

    if n == 0:
        return
    
    i = 0
    j = 0
    while i < n:
        insert_index = m + n - i - j - 1
        
        last_nums2 = nums2[n - i - 1]

        if j == m:
            nums1[insert_index] = last_nums2
            i += 1

        else:
            last_nums1 = nums1[m - j - 1]

            if last_nums2 >= last_nums1:
                nums1[insert_index] = last_nums2
                i += 1
            else:
                nums1[insert_index] = last_nums1
                j += 1



nums1 = [11, 12, 13, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3






def merge_canon(nums1, m, nums2, n):
    if n == 0:
        return

    nums1_p = m - 1
    nums2_p = n - 1
    index_p = m + n - 1

    while nums2_p >= 0:

        if nums1_p < 0:
            nums1[index_p] = nums2[nums2_p]
            nums2_p -= 1
        
        else:

            if nums2[nums2_p] >= nums1[nums1_p]:
                nums1[index_p] = nums2[nums2_p]
                nums2_p -= 1
            else:
                nums1[index_p] = nums1[nums1_p]
                nums1_p -= 1
        
        index_p -= 1


merge_canon(nums1, m, nums2, n)
print(nums1)