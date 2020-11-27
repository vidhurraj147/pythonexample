from builtins import list

from pip._vendor.distlib.compat import raw_input

print ("Hello World!!")

if True:
    print("this is TRUE")
else:
    print("this is FALSE")

list = ['abcd',70,60.84,'john']
tinyList = ['example',100]

print (list)
print (list[0])
print (list[1:3])
print (list + tinyList)

numberIs = 100
if(numberIs == 100) :
    print ("The number is ",numberIs)
else:
    print("lets see")

enterANumber = 1

while enterANumber > 0 :
    enterANumber = raw_input("Enter a number:")
    print("Number entered is : ", enterANumber)
    enterANumber = 1
