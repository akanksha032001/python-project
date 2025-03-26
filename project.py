#HOTEL MANAGEMENT SYSTEM

w=input("Did you have booked your room or not:Y/y or N/n " )
if w=="Y" or w=="y":
print("Please Tell your booking ID")
    i=int(input("Enter the booking ID"))
print(i)
elif w=="N" or w=="n":
print("Which kind of Room would you have to like sir: Delux, King or Twin Bed")
    r=input("Enter the name of type of the room: ")
if r=="Delux":
print("You have to pay Rs. 8000 per day")
elif r=="King":
print("You have to pay Rs. 5000 per day")
elif r=="Twin Bed":
print("You have to pay Rs.4000 per day")
i=input("Do you have an ID? Y/y or N/n")
if i=="Y" or i=="y":
print("You are allowed")
    a=input("Is your current address is same as in your ID? Y/y or N/n ")
if a=="Y" or a=="y":
print("Ok sir")
elif a=="N" or a=="n":
print("Please tell your current address")
add=input("Address: ")
print(add)
elif i=="N" or i=="n":
print("Sorry Sir you are not allowed")
exit()

n=int(input("Enter the number of persons: "))
print(n)
d=int(input("For how many days will you stay sir: "))
if (d>7) and (d<=10):
print("You have to pay Rs.20000 with Rs.5000 in Advance")   
elif (d>5) and (d<=7):
print("You have to pay Rs.15000 with Rs.4000 in Advance")
elif (d>3) and (d<=5):
print("You have to pay Rs.10000 with Rs.3000 in Advance")
elif (d<=3):
print("You have to pay Rs.6000 with Rs.2500 in Advance")
m=int(input("For how many times ofmealswolud you like to ahve sir 1,2,3: "))
if m==1:
print("You have to pay Rs.500 per day for meal")
elif m==2:
print("You have to pay Rs.800 per day for meal")
elif m==3:
print("You have to pay Rs.1000 per day for meal")
v=input("Would you like to have any vehicle on rent from our Hotel: Y/y or N/y")
if v=="Y" or v=="y":
print("Which one would you like to have: A bike, A 4 seater car or A 8 seater car")
    t=input("Enter the type of vehicle: ")
if t=="A Bike":
print("You have to pay Rs.1000 per day")
elif t=="A 4 seater car":
print("You have to pay Rs.2500 per day")
elif t=="A 8 seater car":
print("You have to pay Rs.4500 per day")
elif v=="N" or v=="n":
print("Ok ")
s=input("Do you like to have a mountain view facing room: Y/y or N/n")
if s=="Y" or s=="y":
print("Its cost is Rs.200 higher than normal rooms. Would you like to have?")
    y=input("Yes or No")
if y=="Yes":
print("Thankyou sir , Here is your key. Have a great trip")
elif y=="No":
print(" Thankyou sir, Here is your key .Have a great trip")
else:
print(" Thankyou sir, Here is your key .Have a great trip")




