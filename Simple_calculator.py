#Declare a class, class is equivalent to Sprite
class Jumbo:
  #__init__ is a method which is called automatically
  def __init__(self):
    # Initialise all the variables inside the class to zero
    self.res1=0						
    self.res2=0
    self.res3=0
    self.res4=0
    
  # declare a method called "add" inside the class Jumbo 
  # add method takes two inputs that is written as a and b
  def add(self,a,b):	
    # adds two numbers and stores the result into class variable res1
    self.res1 = a + b
    # display res1
    print("The sum of ",a," + ",b," is ",self.res1)
    
	# declare a method called "subtract" inside the class Jumbo
  # subtrtact method takes two inputs that is written as a and b
  def subtract(self,a,b):	
    # subtracts and stores the result into class variable res2
    self.res2 = a - b	
    print("The difference of ",a," - ",b," is ",self.res2)
    
  # declare a method called "multiply" inside the class Jumbo
  # multiply method takes two inputs that is written as a and b
  def multiply(self,a,b):
    # multiplies the 2 numbers and stores the result into class variable res3
    self.res3 = a * b
    print(a," multiplied by ",b," is equal to ",self.res3)
  
  # declare a method called "divide" inside the class Jumbo
  # divide method takes two inputs that is written as a and b
  def divide(self,a,b):
    #divide the 2 numbers and stores the result into class variable res4
    self.res4 = a / b
    print(a," divided by ",b," is equal to ",self.res4)
  
# the variables declared here are only accessible to the below code not by the class
x=0
y=0
# Displays Mr. Jumbo's conversations
print("Welcome to UXL Code Academy")
print("Hello! I'm Jumbo the calculator")
print("We shall do simple calculations with 2 numbers of your choice")
#Ask user to enter the numbers for computation
x = int(input("Enter the first number : "))
y = int(input("Enter the second  number : "))
#Jumbo_can_do is an object of class Jumbo
Jumbo_can_do = Jumbo()
#call the methods using Jumbo_can_do
Jumbo_can_do.add(x,y)
Jumbo_can_do.subtract(x,y)
Jumbo_can_do.multiply(x,y)
Jumbo_can_do.divide(x,y)
