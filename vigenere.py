def v_enc(k,m):
	r=""
	k*=int(len(m) / len(k)) + (len(m) % len(k) > 0)
	for i,c in enumerate(m):
		if 'A'<=c<='Z' or 'a'<=c<='z':
			if ord('z')-ord(c.lower()) >= ord(k[i].lower())-ord('a'):
				r+=chr(ord(c.lower())+ord(k[i])-ord('a'))
			else:
				#r+=chr((((ord(c)-ord('a'))+(ord(k[i])-ord('a')))%26)+ord('a')) alternative
				r+=chr(ord('a')-1+(ord(k[i])-ord('a'))-(ord('z')-ord(c.lower())))
		else:
			r+=c 
	return r

def v_dec(k,t):
	r=""
	k*=int(len(t) / len(k)) + (len(t) % len(k) > 0)
	for i,c in enumerate(t):
		if 'A'<=c<='Z' or 'a'<=c<='z':
			if ord(c.lower())-ord('a')-(ord(k[i].lower())-ord('a'))>=0:
				r+=chr(ord(c)-(ord(k[i])-ord('a')))
			else:
				r+=chr(ord('z')+(ord(c)-ord('a')-(ord(k[i])-ord('a')))+1)
		else:
			r+=c
	return r

#encrypt
print("start:"+v_enc("xyqxzplikywopr","lmuuimmujopj")+":end")
print((lambda k,m:'start:'+''.join([c,[chr(ord('a')-1+(ord((k*(int(len(m) / len(k)) + (len(m) % len(k) > 0)))[i])-ord('a'))-(ord('z')-ord(c.lower()))),chr(ord(c.lower())+ord((k*(int(len(m) / len(k)) + (len(m) % len(k) > 0)))[i])-ord('a'))][ord('z')-ord(c.lower()) >= ord((k*(int(len(m) / len(k)) + (len(m) % len(k) > 0)))[i].lower())-ord('a')]]['A'<=c<='Z' or 'a'<=c<='z'] for i,c in enumerate(m))+':end')('xyqxzplikywopr','lmuuimmujopj'))

#decrypt
print("start:"+v_dec("xyqxzplikywopr","ikkrhbxctmlx")+":end")
print((lambda k,t:'start:'+''.join([c,[chr(ord('z')+(ord(c)-ord('a')-(ord((k*(int(len(t) / len(k)) + (len(t) % len(k) > 0)))[i])-ord('a')))+1),chr(ord(c)-(ord((k*(int(len(t) / len(k)) + (len(t) % len(k) > 0)))[i])-ord('a')))][ord(c.lower())-ord('a')-(ord((k*(int(len(t) / len(k)) + (len(t) % len(k) > 0)))[i].lower())-ord('a'))>=0]]['A'<=c<='Z' or 'a'<=c<='z'] for i,c in enumerate(t))+':end')('xyqxzplikywopr','ikkrhbxctmlx'))
