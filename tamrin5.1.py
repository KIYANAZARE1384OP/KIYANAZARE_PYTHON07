scores=[20,17,9,13,720,18,3,1,14]
for score in scores:
    if score >=10:
        print(score,":passed")
    else:
        print(score,":failed")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
studants=["ali","vahid","sara","hamid","reza",'elham',"mohsen","zahra","paniz","parmida"]
scores=[20,17,9,13,7,20,18,3,1,14]
passed=[]
r=[]
for names,s in zip (studants,scores):
    if s>=10:
        passed.append("name")
        r.append(s)
print('ghabl az ranking')
print(passed)
print(r)
o=0
o1=0
for i in range (len(r)):
    a=r[i]
    for j in range (len (r)):
        if a>r[j]:
            o=r[i]
            r[i]=r[j]
            r[j]=o
            o1=passed[i]
            passed[i]=passed[j]
            passed[j]=o1
print("bad az ranking")
print(passed)
print(r)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
products=[]
while True:
    name=input("inter product:")
    if name=="exit":
        break
products.append(name)
print(products)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:
    menu=["mojodi","variz","bardasht","khoroji","amaliyate digar"]
    print(menu)
user=input("amaliyat morede nazar ra entekhab konid")
if user not in menu:
    print("entekhb namotabar mibahad")
    if user== "mojodi":
        print("amaliyat mojodi entekhab shod")
     elif user== "bardasht"
     print ("amaliyat bardasht entekhab shod")
 elif user ==" amaliyate digar ""
     continue
 elif user"khoroj"
 print("khoroj ba movaghiyat")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
username="admin" 
password=1234
while True:
    user_name=input("esmetan ra vared konid")
    user_password=int(input("passwordetan ra vared konid"))
     if user_name!=username or user_password!=password:
      print("password ya user name vared shode nadorost ast")   
      continue
  else:
      print("ba movafaghiyat vared shodid") 
      break
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      
         
         
         
     
        
     
        
     
        
     
        
     
        
     
        
     
        
    
    
        






















