a=print(input("Enter your name"))
c=int(input("Enter your age"))
if c>18:
    print(input("Enter your voter id number"))  
    print("Vote your favrouite party by typing code for the party : code 1= BJP, code 2=CPI, code 3=INC , code 4=no one")
else:
    print("you are not eligble to vote")
    exit()
    
code= int(input("enter code"))

if code=='1':
    print("BJP")
elif code=='2':
    print("CPI")
elif code=='3':
    print("INC")
elif code=='4':
    print("INC")
elif code=='4':
    print("No one")
print("You are sucessfully voted ")
