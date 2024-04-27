nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the number you want to search: "))
i = 0
while i<len(nums):
    if(nums[i]==x):
        print("Number found at index ",i)
        break
    else:
        print("Finding...")    
    i+=1