with open("practice.txt","r") as f:
    data = f.read()
    print(data)

    # num = ""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #         print(num)
    #         num = ""
    #     else:
    #         num+=data[i]    
    count = 0
    nums = data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
    print(count)