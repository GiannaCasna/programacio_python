#RO_Pag038_for_01

n= int(input("n= "))
s= 0

for i in range (1, n):
    k = (2 * i) - 1
    s = s + k
    
if s == n **2 :
    print ("verdader")
    
else:
    print ("fals")

#ara amb while

n= 10
s= 0
i= 1
while i <= n:
    k = (2 * i) - 1
    s = s + k
    print ("s= ", s)

print ("i= ", i)
    
    
