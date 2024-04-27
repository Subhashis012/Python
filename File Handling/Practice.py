# with open("practice.txt","w") as f:
#     f.write("Hi everyone \n we are learning file I/O")
#     f.write("using java. \n like programming")

# with open("practice.txt","r") as f:
#     data = f.read()
#     print(data)

# new_data = data.replace("java","python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)
word = "learning"
with open("practice.txt","r") as f:
       data = f.read()   
       if(data.find(word) != -1):
            print("found")
       else:
           print("not found") 