from scipy import mat
c=[4,-4,2]
U=([[3,-1,2],[0,1,-5],[0,0,2]])
a=0
x=[]
while a<3:
    x.append(1)
    a=a+1

n=3
i=n-1
x[n-1]=c[n-1]/U[n-1][n-1]
while i>1:
    x[i]=c[i]
    j=i+1
    while j<n-1:
        x[i]=x[i]-U[i][j]*x[j];
    x[i]=x[i]/U[i][i]
    i=i-1
print (mat(x))
