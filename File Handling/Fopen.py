# f=open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","w")
# f.write("Hello Subhashis")
# f.close()

# f = open("demo.txt","a")
# f.write(" bro")
# f.close()

with open("demo.txt","r") as f:
    data = f.read()
    print(data)  # etate fclose() lage na