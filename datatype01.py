#datatypes variable are store in different datatypes discuss below
""" 01 string type str
    syntax a="this is string" """


x = "Me ek achha coder hu "
print(x)

n = 'hello python bhaiya'
print(n)
str = "'surffering'"
print(str)
#string have statments in double and single quotes, it can have number too but it will treated as string

""" 02 interger type int 
    this is take numbers as data 
    syntax- x = 10 """

a = 10
b = 15
c = a + b #perform arthmentic operation here
print(a)
print(b)
print(c)
print(a*b) #perform arthmentic operation here
 # same as float type have decimal in it 

aa = 20.8
aaa = 33
print(aaa+aa)

y = ["AAM", "SEV", "PAPITA", " khajur"] 
print(y)
print(y[2]) #by indexing a perticular element can get printed

# len() and slice --later

#tuple
my_tuple = (1,2,3,4,)
my_tuple1 = ("kamra ", " rassi", "panka") # tuple once created its elements cannot change as list
print(my_tuple)
print(my_tuple1)
print(my_tuple[3])

# print(n.split) error

#dictionaray -  data store in key, value, pair

doll = {
    "name": "Tatiya Bichhu",
    "age" : 20000,
    "city": "purani haveli wale" 
}
print(doll)
print(doll["name"])
#function of dictionary
print(doll.values())


#set type-special type store values with no duplicates

set = {"Aloo", "began", "Tamator", "Kadduo"}
print(set)
set.add("Daniya")
print(set)

#functon in set - intraction and differance