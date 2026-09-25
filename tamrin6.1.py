#tamrin 6.1
def calculate_age1(year:int):
    return 2026-year
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def calculate_age2(year,date_type):
    if date_type=="shamsi":
        return1405-year
    
    elif date_type=="miladi":
        return 2026-year
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def calculate_age3(year,date_type="miladi"):
    if date_type=="shamsi":
        return 1405-year
    elif date_type=="miladi":
        return 2026-year
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def calculate_age4(year):
    if year<=1405:
        return1405-age
    else:
        return2026-year
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#tamrin 6.2
def check_even_odd(number):
    if number %2==0:
        return"even"
    else:
        return "odd"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def even_2(number):
    if number %2==0:
        return True
    else:
        return False
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
    
def posetive_negetive(number):
    if number>0:
        return"posetive"
    elif number<0:
        return "negetive"
    else:
        return "zero"
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#tamrin6.4
def nomredehi(nomre:int):
    if nomre>=90:
        return"A hastid"
    elif nomre>=60:
        return"B hstid"
    elif nomre>=40:
        return"c hastid"
    elif nomre>=20:
        return "d hastid"
    elif nomre>=0:
        return"f hastid"
     else:
           return"nomre kamtar az 0 nemitavanid vared konid"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#tamrin6.6
def check_email(email:str):

if " " in email:
     return False
elif"@"  not in email:
    return False
elif ".com" not in email:
     return False
 else:
     return True
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def find_max(number_list:list):
number-list.sort():
    return numbers_list[-1]

result= find_max([1,2,-3,80,120,50,14,-50,120,1166,2,0,-180,25])
print(result_1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
def average(scores_list:list)
tedad=0
majmoe=0
for score in scores-list:
    tedad=tedad+1
    majmoe=majmoe+score
miyangn=majmoe/tedad
return miyangin
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     
    
    
    
    
    
    
    










    
    
    
    
    
    
    
    
    
           
           
           
           
           
           
           
           
           
          
     
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    

