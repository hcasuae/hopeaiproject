class oddEven():
    def oddEven():
        num=int(input("Enter a number:"))
        if(num%2==1):
            print(num,"is Odd number")
            oddEven=(num,"is Odd number")
        else:
            print(num,"is Even number")
            oddEven=(num,"is Even number")
            return oddEven
        
class EligibilityForMarriage():
    def Eligible():
        age=int(input("Your age:"))
        gender=input("Your gender:")
        if(age<18):
            print("Not Eligible")
            Eligibility="Not Eligible"
        elif(age>21):
            print("Eligible")
            Eligibility="Eligible"
        elif(gender=="Female"):
            print("Eligible")
            Eligibility="Eligible"
        elif(gender=="Male"):
            print("Not Eligible")
            Eligibility="Not Eligible"
      

class FindPercent():
    def percentage():
        Sub1=int(input("Subject1="))
        Sub2=int(input("Subject2="))
        Sub3=int(input("Subject3="))
        Sub4=int(input("Subject4="))
        Sub5=int(input("Subject5="))
        Total=(Sub1+Sub2+Sub3+Sub4+Sub5)
        Per=(Total/5)
        print("Total:",Total)
        print("Percentage:",Per)
        Percentage="Percentage"
        return Percentage

class triangle():
    def triangle():
        Ht=int(input("Height:"))
        Bth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth/2)")
        AOT=((Ht*Bth)/2)
        print("Area of Triangle",AOT)
        Ht1=int(input("Height1:"))
        Ht2=int(input("Height2:"))
        Bth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        PT=(Ht1+Ht2+Bth)
        print("Perimeter of Triangle:",PT)
        triangle="Perimeter of Triangle:"

class SubfieldsInAI():
    lists=["Machine Learining","Neural Network","Vision","Robotics","Speech Processing","Natural Language Processing"]
    def Subfields():
        for subfield in lists:
            print(subfield)
            output=subfield
     