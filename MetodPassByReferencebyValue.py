
def appedList(myList):
    print("*************************************")
    myList.append([1,2,3,4,5])
    print("Later--> ",myList)
    print("*************************************")
    return;

def modifyList(mylist):
    print("*************************************")
    myList = [55,66,77,44,55,33]
    forLoopCall(myList)
    print("*************************************")
    return;

def forLoopCall(myList):
    print("*************************************")
    print("In the foor loop")
    for value in myList:
        print(value)
    print("*************************************")
    return;

def detailsList(name,age = 100):
    #print("Name is %s, persons age is %d" %(name,age))
    print("Name is %s" % (name))
    print("Persons age is %d" % (age))
    return;

myList = [];
print("Initial--> ",myList)
appedList(myList);
myList = [11,12,13,14,15]
appedList(myList);

#for value in myList:
#    print(value)

forLoopCall(myList)
modifyList(myList);
forLoopCall(myList)
detailsList(age= 55, name="Daniel")
detailsList(name="Daniel")