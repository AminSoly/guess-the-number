from scipy.stats import entropy
import numpy as np
import mysql.connector
import random
mydb = mysql.connector.connect(
    host = "sql12.freemysqlhosting.net",
    user = "sql12738640",
    passwd = "qQcLFzEusn",
    database = 'sql12738640')
cur = mydb.cursor()



query = 'select value from numbers'
cur.execute(query)
res = cur.fetchall()
values = []
for i in res:
    values.append(i[0])

   

def cal(num):
    x = []   
    global s, m ,s2,pk
    if num == 10:
        e = even()
        s = len(e)
        m = len(values)
        s2 = m - s
    else:
        for i in values:
            if i >= num:
                x.append(i)                 
        s = len(x)
        m = len(values) 
        s2 = m - s   
 
    pk = np.array([s/m, s2/m])
    ent = float(entropy(pk, base = 2))
    return ent
   

# deleting ODD numbers from values
def even():
    global values
    e = []
    for i in values:
        if i % 2 == 0:           
            e.append(i)
    return e                  
#     print(values)


# deleting EVEN numbers from values
def odd():
    global values
    e = []
    for i in values:
        if i % 2 != 0:           
            e.append(i)
    return e                   
#     print(values)    

       

def ent():
    ent_list = []
    for i in range(1, 11): 
        ent_list.append(cal(i))
   # print("list of entropy :" + str(ent_list))  
    return ent_list 





def best_num():
    #print the highest entropy
    ent_list = ent()
    highest_ent =  max(ent_list)
    all_highest_ent = [g for g, x in enumerate(ent_list) if x == highest_ent]

    #print("highest entropy :" + str(all_highest_ent) )



    r = random.choice(all_highest_ent)
    r += 1
   # print(r)
    return r  
    
            

def deleting_num0(r):
    global values
    x = []
    if r == 10:
        x = even()
        
    else:
        for i in values:
            if i >= r:
                x.append(i)         

    values = x
   # print("value is :  " + str(values))



         
def deleting_num1(r): 
    global values
    x = []
    if r == 10:
        x = odd()
    else:
        for i in values:
            if i < r:
                x.append(i)         

    values = x
   # print("value is :  " + str(values))


def check():
    global values
    return len(values)


def give_value():
    global values
    return values[0]    
        


#for i in range (5):
    g = best_num()
    deleting_num0(g)




