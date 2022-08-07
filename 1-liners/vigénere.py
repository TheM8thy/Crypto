m = "nnnn"
k = "nnnn"
r = ""
a=0
k*=int(len(m) / len(k)) + (len(m) % len(k) > 0)

for i,c in enumerate(m):
	print(ord('z')-ord(c.lower()),">",ord(k[i].lower())-ord('a'))
	if ord('z')-ord(c.lower()) >= ord(k[i].lower())-ord('a'): #shift forward
		print("1.",c,k[i],ord(c.lower()),ord(k[i])-ord('A'))
		r+=chr(ord(c.lower())+ord(k[i])-ord('a'))
	elif ord(c.lower())-ord('a') >= ord(k[i])-ord('a'): #shift backward
		print("2.")
		#print(c.lower(),": C-Dist to z:",ord('z')-ord(c.lower()))
		#print(k[i],": K-Dist to a:",ord(k[i])-ord('a'))
		a=(ord(k[i])-ord('a'))-(ord('z')-ord(c.lower()))
		print("Substraction:",(ord(k[i])-ord('a'))-(ord('z')-ord(c.lower())),"Letter:",chr((ord('a'))-1+a))
		r+=chr((ord('a'))-1+(ord(k[i])-ord('a'))-(ord('z')-ord(c.lower())))
	else: #dont shift
		r+=c
print("start:"+r+":end")

print((lambda k,m:'start:'+''.join([[c,chr((ord('a'))-1+(ord(k[i])-ord('a'))-(ord('z')-ord(c.lower())))][ord(c.lower())-ord('a') >= ord(k[i])-ord('a')],chr(ord(c.lower())+ord(k[i])-ord('a'))][ord('z')-ord(c.lower()) >= ord(k[i].lower())-ord('a')] for i,c in enumerate(m))+':end'('haha','aaaa'))
