import json

f1 = open('finaldata.json')
f1 = json.load(f1)

timestamps = []
prevcounter =-1
gap = 300
print(len(f1["prices"]))
for i in range(len(f1["prices"])):


    if f1["prices"][i][0] in timestamps < prevcounter  or gap!=300:
        print(i)
        print("not sorted")
        break
    prevcounter = f1["prices"][i][0]
    if (i!=0):
        gap = f1["prices"][i][0] - f1["prices"][i-1][0]
        
print("Done")

print(f1["prices"][17567][0])
print(f1["prices"][17568][0])
print(f1["prices"][17569][0])
print(f1["prices"][17570][0])
print(f1["prices"][17571][0])

