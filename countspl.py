s=input()
count=0
for i in range (0,len(s)):
	if s[i].isnumeric() or s[i].isalpha():
	    
	    count=count+1
	    a= len(s)-count
print(a)
