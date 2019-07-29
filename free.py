x11,y11=map(int,input().split())
z11=list(map(int,input().split()))
p=list(map(int,input().split()))
y11=""
for j in p:
    z11.append(j)
    y11=y11+str(max(z11))+" "
print(y11.strip())
