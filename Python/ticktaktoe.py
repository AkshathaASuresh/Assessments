import
l=[[1,2,3],[4,5,6],[7,8,9]]
dic={}
flag=0
for x in range(1,10):
    dic[x]=x
# print(dic)
def disp(l):
    for x in l:
        for t in x:
            print(t,end='   ')
        print("\n")

def conditions(dictionary,a):
    listt,lis=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]],[]
    # print(dictionary,a)
    for i in listt:
        for x,y in dictionary.items():
            if x in i and y==a:
                lis.append(x)
                # print(lis)
                if len(lis)==3:
                    # print(lis)
                    if a=="x":
                        disp(l)
                        print("game over,player 2 has won")
                        flag=1
                    else:
                        disp(l)
                        print("go home player 2")
                        flag=1

                    exit()

        lis.clear()


for x in l:
    for t in x:
        print(t,end='   ')
    # print(" ".join(str(x)))
    print("\n")
n=9
while(n>0):
    if(n%2==0):
        a='x'
        i = int(input("Player 2: "))
    else:
        a='o'
        i = int(input("Player 1: "))
    n -= 1
    for x in l:
        for t in range(len(x)):
            if x[t]==i:
                x.pop(t)
                dic[i]=a
                x.insert(t,a)
    conditions(dic,a)
    if n==0 and flag==0:

        disp(l)
        print("Draw!!!!!")
    else:
        disp(l)
    # print(dic)


