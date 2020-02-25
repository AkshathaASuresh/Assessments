import random

li = ["ACCELERATING","Aircraft","Consequences","ABBREVIATION","Airforce","Grandparents","Civilization","Kaleidoscope","Intelligence","Alphabet","Organization","Relationship","Bodybuilding","Backpack"]
r = random.choice(li).lower()
rl = {}
b = ""
n = len(r)
s = list(r)
ran_l = []
for i in range(6):
    c=random.randrange(0,n)
    if c not in ran_l:
        ran_l.append(c)
        rl[c] = s[c]
        x = s.pop(c)
        s.insert(c,"_")
        a = "".join(s)
print(a)
# print(rl)
# print(ran_l)
for er in range(6):
    user_inp = input()
    if user_inp.lower() == r:
        break
    for ke,va in rl.items():
        if va==user_inp:
            s.pop(ke)
            s.insert(ke,va)
            b = "".join(s)
            print(b)
            if b == r:
                print("Wow!!! You found it ")
                print("Answer : ", r)
                exit()



if b == r or user_inp.lower() == r:
    print("Wow!!! You found it ")
    print("Answer : ",r)
else:
    print("Out of chances ")
    print("Correct Answer is ", r)
