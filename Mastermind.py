import  numpy as np

answer = np.array([1,4,6,4])
print(answer)
#input=[1,6,3,4]
output=np.chararray(4)
x=input("plz input")
input=list(x)
input=np.asarray(input)
input=input.astype(int)
postion=0
for i in range(0,4):
    if input[i]==answer[i]:
        output[postion]='C'
        input[i]=-1
        postion+=1

for i in  range(0,4):
    if input[i]!=-1:
        a=np.isin(input[i],answer)
        if a==True:
            output[postion]='N'
            postion += 1
            input[i]=-1
for i in range(0,4):
    if input[i]!=-1:
        output[postion] = '0'
        postion += 1
print(output)


