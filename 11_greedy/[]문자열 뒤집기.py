nums = input()
count = [0] * (2)

if nums[0] == '1':
    count[0] += 1
else:
    count[1] += 1
    
for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        if nums[i+1] == '1':
            count[0] += 1
        else:
            count[1] += 1
            
print(min(count))
    
    

        
