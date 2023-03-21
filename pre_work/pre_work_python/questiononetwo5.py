#q1
def hello_name(user_name):
    print("Hello" +  user_name.upper() + "!")
    
hello_name(" Chuck")  


#q2



def odd_numbers():
    numbers = list(range(0,101))
    for number in numbers:
        if number % 2 != 0:
            print(number)
            
odd_numbers()
 




#q3 

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num
test = max_num_in_list([2,3,5,8,9])
print(max_num_in_list([2,3,5,8,9]))  




#q4
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False  
        print(f'{a_year}') 
   
is_leap_year(2023)  
         
             
      
#q5


def is_consecutive(a_list):
    i=0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else :
              status = False
              break
    print(status)
    
   
    
            

        
             

                 