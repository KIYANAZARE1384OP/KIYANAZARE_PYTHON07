#q1.4
username=input("username khod ra vared konid")
password=input("passworde khod ra vared konid")

if username=="admin"and password =="1234":
  print("login ba movafaghiat anjam shod.")
else:
  print("password ya username ghalat ast")

#q2.4
product_price=int(input("gheymat kala ra vared konid"))
if product_price>=1000000:
    discount=20
    final_price=int(product_price*0.8)
elif product_pice>=500000:
    discount=15
    final_price=int(product_price*0.85)
elif product_price>0 :
    discout=10
    final_price=int (product_price*0.9)
else:
    print("gheymate vared shode motabar nemibaashad")
if product_price>0:
    print("darsade takhfif;",discount,"darsad")
    print("gheymate nahaei bad az takfif:",final_price,"toman")
    
#q3.4
products=["laptop,mouse,keybord,monitor"]
product_name=input("name mhsool ra vared konid")
if product_name in products:
    print("mahsool mojod nist.")
    
#q4.4
speed=int(input("lotfan sorat mashin khod ra vared konid"))
if speed>=120:
    print("khatarnak")
elif speed>=80:
    print("ziad")
elif speed>0:
    print("normal")
else:
    print("shoma dar halate istade hastid")
    
#q5.5
odd_numbers_list=[]

count=0

for odd-numbers_list in range (15,116,2):
    print(odd_numbers)
    odd_numbers_list.ppend(odd_number)
    count=count+1
print(odd_numbers_list)
print(count)


#q6.6
names=["kiyana,elina,sara,amir,"]
for nam in names:
    print(len(name))  





















