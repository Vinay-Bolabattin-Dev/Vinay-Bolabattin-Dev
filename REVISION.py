# 1st check pov or neg number , if it is pov then even or odd 
 
number= int(input("Enter you number to check: "))
if(number>0):
    if number % 2==0:
        print("This is a + ve & even ")
    else:
        print("This is a + ve & odd ")
elif number< 0:
    print("Negative")
else:
    print("Zero")



