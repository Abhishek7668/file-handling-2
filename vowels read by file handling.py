f = open("C:\\Users\\Lenovo\\Desktop\\shek\\abhi.txt","r")
out=f.read()
vowels=0
consonent=0
upper=0
lower=0
for i in out:
   if i in ["a","e","i","o","u"]:
    vowels=vowels+1
   elif i.isalpha():
       consonent=consonent+1
   elif i . isupper():
       upper=upper+1 
   elif i . islower():
        lower+=1
print("vowels",vowels)
print("consonent",consonent)
print("upper_case",upper)
print("lower_case",lower)

f.close()

