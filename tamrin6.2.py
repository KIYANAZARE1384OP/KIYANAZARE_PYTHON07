#tamrin6.11
def passed_scores(scores:list):
    new_scores_list=[]
    if score in scores:
        if score>=10:
            new_scores_list.append(score)
            return new_scores_list
result=passed_scores([19,17,11,16,15,19.25,20,18])
print(result)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#tamrin6.12
def calculateor (numb1:float,numb2:float,operation:str):
    
    
    if operation=="jam":
        result=numb1+numb2
        return result
    elif operation=="menha":
        result=numb1-numb2
        return result 
    elif operation=="zarb":
        result=numb1*numb2
        return result
    elif operation=="taghsim":
        result=numb1/numb2
        return result
    else:
        None
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#tamrin6.13
def countdown (numb:int):
    for num in range (numb,-1,-1):
        print(numb)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#tamrin6.14()
def multiplication_table (numb:int):
    for zarb in range (1,20):
        print(f"{numb}*{zarb}={numb*zarb}")
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
        





















    
    
    
