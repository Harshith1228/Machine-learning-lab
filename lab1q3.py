a=[1,2,3,4,5,6,7,8,9]
b=[11,12,3,45,56,7,66,8,10]


def sim(a,b):
    common=0
    c=[]
    for i in a:
        if i in b:
            common+=1
            c.append(i)
    return common,c

result=sim(a,b)
print("number of similar elements in the lists are",result)