nums = [1,4,9,16,25,36,49,64,81,100]
x = int(input("Enter the number you want to search: "))
idx =0 
for ele in nums:
    if(ele==x):
        print("Number found at index ",nums.index(ele))
    idx +=1
    