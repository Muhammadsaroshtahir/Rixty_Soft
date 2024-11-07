# important part of an web development.
# creating reading updating deleting files.

#open()

#f = open("cars.txt")
#f = open("cars.txt","rt")

#f = open("cars.txt","r")
#print(f.read())

# f = open("cars.txt","a")
# f.write("now this file have more content!")
# f.close

try:

    f=open("cars3.txt","r")
    print(f.read())
except Exception as E:
    f=open("cars3.txt","w")
    print(E)
# f = open("cars.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# f = open("cars.txt", "r")
#print(f.read())

#context manager