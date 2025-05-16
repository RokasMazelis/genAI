user_imput = input ("Iveskite atstuma kilometrais ")

if user_imput.isdigit():
    user_imput = int(user_imput)
    kilometers = user_imput
    miles = kilometers / 1.60934
    print (f"{user_imput} kilometrai atitinka {miles} myles")

else:
    print ("Ivesk skaiciu, ne teksta")
    