# This is for variable length argurments

def printValues(formal_args, *var_arguments):
    print("output is")
    print(formal_args)
    for vals in var_arguments:
        print("Values in var_arguemnts ",vals)
    return;

printValues(10)
printValues(55,77,44,77,88)

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print ("---> ",var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )