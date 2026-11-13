# if-else
age = int(input("Enter age: "))

if age > 18:
 print("You can drive")
else:
 print("You can't drive")

#__________________________________________________________________________________

# if-elif-else example (Traffic Light System)
light = input("Enter traffic light color (red/yellow/green): ").lower().strip()

if light == "red":
   print("Stop")
elif light == "yellow":
   print("Slow down")
elif light == "green":
   print("Go")
else:
   print("Invalid")

print("End of program !")

#_____________________________________________________________________________________
