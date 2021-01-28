weight = float(input("Weight: "))
option = input("(K)g or (L)bs ? ")

# m(lb) = m(kg) / 0.45359237

if option == 'k' or option == 'K' :
    lbs = weight / 0.45359237
    print("Weight in lbs "+str(lbs))
elif option == 'l' or option == 'L' : 
    kg = weight * 0.45359237
    print("Weight in kg "+str(kg))
else: 
    print("Enter valid option")

