# Q1. Write python program to given condition

# 1. location = "Massachusetts"; pay = 50000 2.
# 2. location = "lowa"; pay = 50000 3.
# 3. location = "California"; pay = 50000 4 # here california comes two times that's why I replace it with europe.
# 4. location = "U.S.S. Enterprise"; pay = 1 5.
# 5. location = "California"; pay = 25000
#==============================================
# list of locations.
print("___________________________________")
print("California for press: 1 \nMassachusetts for press: 2 \nlowa for press: 3 \neurope for press: 4 \nU.S.S. Enterprise for press: 5")
print("___________________________________")
# taking input for location.
location = int( input ("Enter your Location:"))

# condition one:
if location == 1:
    print("location = California: pay = 25000")

# condition Two:
elif location == 2:
    print("location = Massachusetts: pay = 50000")

# condition Three:
elif location == 3:
    print("location = lowa pay = 50000")

# here california comes two times that's why I replace it with europe.
# condition Four:
elif location == 4:
    print("location = europe: pay = 50000 ")

# condition Five:
elif location == 5:
    print("location = U.S.S. Enterprise; pay = 1")

# if any condition false this will be run.
else: 
    print("Invalid location, \nTry again.")




