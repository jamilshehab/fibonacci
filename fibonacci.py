number=int(input("enter your number : "))
firstvariable=0
secondvariable=1
 
for i in range(0,number):
     print(firstvariable) 
     previous_variable=firstvariable
     firstvariable=secondvariable
     secondvariable=previous_variable + secondvariable        

#explanation of this code : first we declared a variable which stores a user input and then we declared 2 variables of values 0 and 1 
#we looped from 0 to the user input 
#the loop explanation we first print the first variable which is assigned by default to 0 
#we declared a variable that stores the previous variable 
#we updated the previous variable which is zero and assigned it into 1 
#we assigned the second variable into previous_variable which stores the first variable which is updated into the second variable 
#we add the second variable which is the updated variable which is 1 and then the second variable which is one as well 
#the second time in the loop the first variable which is updated into 1 