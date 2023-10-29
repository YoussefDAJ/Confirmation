names = input("Enter the names of attendees seperated by comma: \n")
for x in names.split(","):
    print(f"\n{x}")
    att = input("Is this person will came? : (yes/no)\n").lower()
    if att == "yes":
        print("Confirmed")
    else:
        print("Not confirmed")
