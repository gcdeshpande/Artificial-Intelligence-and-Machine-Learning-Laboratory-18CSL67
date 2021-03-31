x1=[0,0,1,1]
x2=[0,1,0,1]
ExpectedY=[0,1,1,1]
w=[-0.2,0.4]
ActualY=[]
Error=[]
steps=[]
t=0

epoch=0
MaxEpoch=100
a=0.2

while epoch<MaxEpoch:
    ActualY=[]
    Error=[]
    for i in range(len(x1)):
        step=w[0]*x1[i]+w[1]*x2[i]
        steps.append(step)
        if step>t:
            ActualY.append(1)
        else:
            ActualY.append(0) 
        
    for i in range(len(x1)):
        if ActualY[i]==ExpectedY[i]:
            Error.append(0)
        else:
            Error.append(1)
            w[0]=w[0]+(a*x1[i]*Error[i])
            w[1]=w[1]+(a*x2[i]*Error[i])
            
    epoch=epoch+1
           
    print(epoch)    
    print(ExpectedY)
    print(ActualY)
    print(Error)
    print(w)
