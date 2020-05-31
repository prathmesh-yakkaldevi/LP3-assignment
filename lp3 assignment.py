


import pandas as pd
import math
from PIL import Image




names = ['Red','Green','Blue','output']

data=pd.read_csv(r"dataset.csv",names=names)

data1=data.values



def KNN(pred,data=data1,k=6):
    distances=list()
    votes=list()
    ans={}
    if k>len(data):
        return 'k can not be less than samples'
    for feature in data:
        euclidean_distance = math.sqrt((feature[0]-pred[0])**2 + (feature[1]-pred[1])**2  
                             + (feature[2]-pred[2])**2  )
        distances.append([euclidean_distance,feature[3]])
    distances.sort()   
    votes = [i[1] for i in distances[:k]]
    for i in votes:
        if i not in ans:
            ans[i]=0
        ans[i]+=1
    max=0
    for x, y in ans.items():
        if y > max:
            max=y
            key=x
    return key




def getinput(Image_path):
    im = Image.open(Image_path)
    im = im.convert('RGB')
    px=im.load()
    pix=px[0,0]
    print(pix)
    op = KNN([pix[0],pix[1],pix[2]])
    print(op)


#check accuracy with random pixel
m={1:'r',2:'g',3:'b'}
def accuracy(l,col):
    op=None
    op=KNN(l)
    if op is m[col]:
        return 1
    else:
        return 0

color1,color2,color3=0,0,0
tcount=0
ccount=0
import random
for _ in range(600):
    i= random.randrange(0,256)
    j= random.randrange(0,256)
    k= random.randrange(0,256)
    if i>j and i>k:
        color1 = 1
    if(j>i and j>k):
        color1 = 2
    if(k>i and k>j):
        color1 = 3
    if(i == j and i>k):
        color1,color2 = 1, 2
    if(i == k and i>j):
        color1,color3 = 1, 3
    if(j == k and j>i):
        color2,color3 = 2, 3
    if (color1 != 0 and color2 == 0 and color3 == 0):
        tcount+=1
        temp=accuracy([i,j,k],color1)
        ccount+=temp   
    elif (color1 == 0):
        tcount+=2
        temp1 = accuracy([i,j,k],color2)
        temp2 = accuracy([i,j,k],color3)
        ccount +=temp1+temp2
    elif (color2 == 0):
        tcount+=2
        temp1 = accuracy([i,j,k],color1)
        temp2 = accuracy([i,j,k],color3)
        ccount +=temp1+temp2
    elif (color3 == 0):
        tcount+=2
        temp1 = accuracy([i,j,k],color2)
        temp2 = accuracy([i,j,k],color1)
        ccount +=temp1+temp2

    color1,color2,color3=0,0,0
print(' Total Count = ',tcount,'\n','Accurate Count = ',ccount,'\n','Accuracy = ',ccount/tcount)

