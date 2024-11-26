weight = float(input("Enter Your Weight :"))
height = float(input("Enter Your Height :"))
BMI = weight  / (height **2)

if (BMI > 18.5):
    print("You Are A Healthy Person")

else:
     print("You Are Under Weight")

if (BMI > 24.5):
    print("You Are Obese")

else:
     print("You Are Over Weight")  