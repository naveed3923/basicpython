def array_front9(nums):
    end=len(nums)
    if end>4:
        end=4
    for i in range(0,end):
        if nums[i]==9:
            return True
        else:
            return False
