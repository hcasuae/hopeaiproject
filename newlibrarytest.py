class groupthefunctions():
    def Subfield():
        lists=["Machine learning","Neural network","vision","robotics","speech processing","natural language processing"]
        for subfields in lists:
            print(subfields)
            out= subfields
        return out
    def oddeven():
        num=int(input("Enter a number = "))
        if(num%2==1):
            print(num,"is odd number")
            message=(num,"is odd number")
        else:
            print(num,"is even number")
            message=(num,"is even number")
        return message
    def EligibilityForMarriage():
        age=int(input("your age = "))
        Gender=input("your gender = ")
        if (age<=18):
            print(Gender,"Not Eligible")
            message=(Gender,"Not Eligible")
        elif(Gender=="Male"):
            if(age>=20):
                print(Gender, "Eligible")
                message=(Gender, "Eligible")
            else:
                print(Gender, "Not Eligible")
                message=(Gender, "Not Eligible")
        else:
            print(Gender, "Eligible")
            message=(Gender, "Eligible")
        return message
    def triangle():
        Height=32
        Breadth=34
        Area=(Height*Breadth)/2
        print ("Height:",Height)
        message=("Height:",Height)
        print ("Breadth:",Breadth)
        message=("Breadth:",Breadth)
        print ("Area formula: (Height*Breadth)/2")
        message=("Area formula: (Height*Breadth)/2")
        print ("Area of Triangle:",Area)
        message=("Area of Triangle:",Area)
        Height1=2
        Height2=4
        Breadth=4
        Perimeter=Height1+Height2+Breadth
        print("Height1:",Height1)
        message=("Height1:",Height1)
        print("Height2:",Height2)
        message=("Height2:",Height2)
        print("Breadth::",Breadth)
        message=("Breadth::",Breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        message=("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",Perimeter)
        message=("Perimeter of Triangle:",Perimeter)
        return message