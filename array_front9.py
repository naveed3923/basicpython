#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


def array_front9(nums):
    end=len(nums)
    if end>4:
        end=4
    for i in range(0,end):
        if nums[i]==9:
            return True
        else:
            return False
