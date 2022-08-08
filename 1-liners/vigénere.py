def v_enc(k,m):
	r=""
	k*=int(len(m) / len(k)) + (len(m) % len(k) > 0)
	for i,c in enumerate(m):
		if 'A'<=c<='Z' or 'a'<=c<='z':
			if ord('z')-ord(c.lower()) >= ord(k[i].lower())-ord('a'): #shift forward
				r+=chr(ord(c.lower())+ord(k[i])-ord('a'))
			else: #shift backward
				#r+=chr((((ord(c)-ord('a'))+(ord(k[i])-ord('a')))%26)+ord('a')) alternative
				r+=chr((ord('a'))-1+(ord(k[i])-ord('a'))-(ord('z')-ord(c.lower())))
		else: #dont shift
			r+=c 
	return r

print("start:"+v_enc("xyqxzplikywopr","lmuuimmujopj")+":end")

#encrypt
print((lambda k,m:'start:'+''.join([c,[chr((ord('a'))-1+(ord((k*(int(len(m) / len(k)) + (len(m) % len(k) > 0)))[i])-ord('a'))-(ord('z')-ord(c.lower()))),chr(ord(c.lower())+ord((k*(int(len(m) / len(k)) + (len(m) % len(k) > 0)))[i])-ord('a'))][ord('z')-ord(c.lower()) >= ord((k*(int(len(m) / len(k)) + (len(m) % len(k) > 0)))[i].lower())-ord('a')]]['A'<=c<='Z' or 'a'<=c<='z'] for i,c in enumerate(m))+':end')('xyqxzplikywopr','lmuuimmujopj'))
