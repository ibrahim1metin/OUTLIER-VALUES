import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as lreg
def outlier(args):
    args=sorted(args)
    outlist=[]
    def median(args1):
        if(len(args1)%2==1):
            return list(sorted(args1))[int((len(args1)/2)-0.5)]
        else:
            return (list(sorted(args1))[int(len(args1)/2)]+list(sorted(args1))[int(len(args1)/2)-1])/2
    def minmax(data):
        if len(data) < 2: 
            raise ValueError("Data must contain at least two values to have min and max values.")
        srt = sorted(data)
        return srt[0],srt[-1]
    min,max=minmax(args)
    if len(args)%2==1:
        q1=median(args[args.index(min):args.index(median(args)):])
        q3=median(args[args.index(median(args)):args.index(max):])
        for i in args:
            if(i<(q1-1.5*(q3-q1)) or i>(q3+1.5*(q3-q1))):
                outlist.append(i)
        return outlist
    args.append(median(args))
    args=sorted(args)
    q1=median(args[args.index(min):args.index(median(args)):])
    q3=median(args[args.index(median(args)):args.index(max):])
    for i in args:
        if(i<(q1-1.5*(q3-q1)) or i>(q3+1.5*(q3-q1))):
             outlist.append(i)
    return outlist
data=[i for i in range(1,101) if i !=53]
indexes=[i for i in range(1,101)]
data.insert(52,10000)
print(outlier(data))
plt.boxplot(data)
plt.show()
lr=lreg()
x=[]
y=[]
for k,l in zip(indexes,data):
    x.append([k])
    y.append([l])
lr.fit(x,y)
print(lr.predict([[103]]))
print(list(zip(indexes,data)))
for i , j in zip(indexes,data):
    if j in outlier(data):
        index=data.index(j)
        indexes.pop(index)
        data.pop(index)
print(list(zip(indexes,data)))
x.clear()
y.clear()
for k,l in zip(indexes,data):
    x.append([k])
    y.append([l])
lr2=lreg()
lr2.fit(x,y)
print(lr2.predict([[103]]))
