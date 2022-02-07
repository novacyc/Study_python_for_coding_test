nums = input()
count_zero, count_one = 0, 0

if nums[0] == '1':
    count_zero += 1
else:
    count_one += 1
    
for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        if nums[i+1] == '1':
            count_zero += 1
        else:
            count_one += 1
            
print(min(count_zero, count_one))
    
    

        
