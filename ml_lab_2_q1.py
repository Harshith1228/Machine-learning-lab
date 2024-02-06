import numpy as np

x1=int(input("enter the x coord of first point :"))
y1=int(input("enter the y coord of first point :"))

x2=int(input("enter the x coord of first point :"))
y2=int(input("enter the y coord of second point :"))
p1=[x1,y1]
p2=[x2,y2]


def euclideandistance(p1,p2):
    dist=np.sqrt(pow(p2[0]-p1[0],2)+pow(p2[1]-p1[1],2))
    return dist

def manhattandistance(p1,p2):
    dist=((p2[0]-p1[0])+(p2[1]-p1[1]))
    return dist


mdist=manhattandistance(p1,p2)
edist=euclideandistance(p1,p2)
print("the euclidean distance is :",edist)
print("the manhattan distance is :",mdist)
