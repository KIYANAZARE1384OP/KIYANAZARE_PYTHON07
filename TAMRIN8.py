#Optional 1
def even_numbers(n):
    for even_num in range(2,n,2):
        yield even_num


test_even_number = even_numbers(9)

print(test_even_number) #<generator object even_numbers at 0x0000018EE9325A80>

next(test_even_number) #2

next(test_even_number) #4

next(test_even_number) #6

next(test_even_number) #8
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Optional 2
def create_profile(name,age,**extra_data):
    print("--------------------------------")
    print(f"esm: {name}")
    print(f"sen: {age}")
    
    #print(type(extra_data)) #<class 'dict'>
    count_extra = 0
    for extra_key,extra_value in extra_data.items():
        count_extra = count_extra + 1
        print(f"etelaate ezafi({count_extra}): {extra_key} - {extra_value}")
    #print(f"tedade etelaate ezafi: {len(extra_data)}")
    print(f"tedade etelaate ezafi: {count_extra}")
    
    if "email" not in extra_data:
        print("email not provided")
    
     
        
    profile = {
        "name": name,
        "age": age,
        **extra_data
    }

    return profile
    
    
    
create_profile("elen",25,city="tehran",phone="09190153108", email="elina@gmail.com")  
    
create_profile("elen",25,city="tehran",phone="09190153108")  

    
test_profile = create_profile("elen",25,city="tehran",phone="09190153108", email="elina@gmail.com")

print(test_profile)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Optional 3
def jam(numb1,numb2):
    result = numb1 + numb2
    return result

def tafrigh(numb1,numb2):
    result = numb1 - numb2
    return result

def zarb(numb1,numb2):
    result = numb1 * numb2
    return result

def taghsim(numb1,numb2):
    result = numb1 / numb2
    return result
#````````````````````````````````````````````````````````````````````````````````
#Project 1
def jam(numb1,numb2):
    result = numb1 + numb2
    return result

def tafrigh(numb1,numb2):
    result = numb1 - numb2
    return result

def zarb(numb1,numb2):
    result = numb1 * numb2
    return result

def taghsim(numb1,numb2):
    result = numb1 / numb2
    return result
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
#Project 2
from accounts.authentication import login
def get_bank_name():    print("get_bank_name checked")

login()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Project 3
from config import get_bank_name
from accounts.account import create_account
from accounts.authentication import login
from payments.payment import make_payment
from payments.fee import calculate_fee
get_bank_name()
create_account()
login()
make_payment()
calculate_fee()


















