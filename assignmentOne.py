a = 60 / 2 ** 2 + 2 * 100 - 114.75
print(a)
b = 4 * (6 + 5)
b1 = 4 * 6 + 5
b2 = 4 + 6 * 5
print(b, b1, b2)

s = "hello"
print(s[::-1])
b="mattias"
print(b[::-1])
newlist=[]
newlist.append(0)
newlist.append(0)
newlist.append(0)
print(newlist)
mylist = [0]*3
print(mylist)
d = {'k1':{'k2':'hello'}}

print(d["k1"].values())
print(d["k1"]["k2"])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d["k1"][0]['nest_key'][1][0])
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d["k1"][2]["k2"][1]["tough"][2][0])

list5 = [1, 2, 2, 33, 4, 4, 11, 3, 3, 2]
print(set(list5))

a = 2>3
print(a)
b=3<=2
print(b)
c=3==2.0
print(c)
d=3.0==3
print(d)
e=4**0.5 !=2
print(e)
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1']

