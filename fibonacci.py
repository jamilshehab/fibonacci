number=int(input("enter your number : "))
firstvariable=0
secondvariable=1
 
for i in range(0,number):
     print(firstvariable) 
     previous_variable=firstvariable
     firstvariable=secondvariable
     secondvariable=previous_variable + secondvariable    

#note I will try my best to explain the code :     

#explanation of this code : first we declared a variable which stores a user input and then we declared 2 variables of values 0 and 1 
#we looped from 0 to the user input 
#the loop explanation we first print the first variable which is assigned by default to 0 
#we declared a variable called previous_variable that stores the first  variable  which is zero by default 
#we updated the first variable which is zero and assigned it into the second variable which is 1 firstvariable=secondvariable
#we apply the second variable which consist of    the previous variable stored as zero and the secondvariable which is one by default
#we re apply the loop and the first variable becomes 1 because before updating the second variable the second variable was by default 1 so it displays 2 times in the compiler
#the first time is by default and the second time is by 0 + 1 and the loops continue through n 
  