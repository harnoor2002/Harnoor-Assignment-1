x=input("Enter radius of circle :")
r=float(x)
a=3.14*r**2
print("Area of circle is :",a)


fileName=input("Write the filename: ")
file_extns=fileName.split(".")
print("the extension is: " + repr(file_extns[-1])) 
