s = 'Tharun'
# datastructure-name[index-position]
print(s[2])
s= "sharath"
print(s[0])
s='python'
print(s[-1])

s1="hii hello"
print(len(s1))
print(s1[3])
print(s1[5])
print(s1[2])
s2="hiitharunreddy"
print(len(s2))
print(s2[5])
a="hi hello world"
print(-len(a))
print(s1.index('h'))
print(s1.index('i'))
print(dir(tuple))
l=[20,30,'hello',[1,2,[12,3,4]]]
l[2]=30
print(l)
l[-1]=20
print(l)
del l[-1]
print(l)
l=[2.0,3.8,'hello',[4,5,[7,9,[6,2]]]]
l[1]=10
print(l)
l[2]=3.8
print(l)
del l[3]
print(l)
#3append
l=[2.0,3.8,'hello',[4,5,[7,9,[6,2]]]]
l.append('hi')
print(l) 
#3 insert
l=[2.0,3.8,'hello',[4,5,[7,9,[6,2]]]]
l.insert(2,'hi')
print(l)
b={1:'c',2:'c',"c":'e'}
print(b.keys())
print(b)
print(b.get('x'))
print(b.get('x',100))
print(b.get(2,50))
print(b)
l1=[1,2,3]
l2=l1
print(l2)
a=(1,2,3)
b=a
print(b)
n=10
sum= 0
i = 1
while i<=n:
	sum=sum+1
	i=i+1
print(sum) 