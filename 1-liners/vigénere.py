def v_enc(k,m):
	r=""
	k*=int(len(m) / len(k)) + (len(m) % len(k) > 0)
	for i,c in enumerate(m):
		if ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z'):
			print(c)
			if ord('z')-ord(c.lower()) >= ord(k[i].lower())-ord('a'): #shift forward
				print("1.")
				r+=chr(ord(c.lower())+ord(k[i])-ord('a'))
			elif ord(c.lower())-ord('a') >= ord(k[i])-ord('a'): #shift backward
				print("2.")
				r+=chr((ord('a'))-1+(ord(k[i])-ord('a'))-(ord('z')-ord(c.lower())))
		else: #dont shift
			r+=c
	return r

print("start:"+v_enc("n","444")+":end")

print((lambda k,m:'start:'+''.join([c,[[c,chr((ord('a'))-1+(ord((k*(int(len(m) / len(k)) + (len(m) % len(k) > 0)))[i])-ord('a'))-(ord('z')-ord(c.lower())))][ord(c.lower())-ord('a') >= ord((k*(int(len(m) / len(k)) + (len(m) % len(k) > 0)))[i])-ord('a')],chr(ord(c.lower())+ord((k*(int(len(m) / len(k)) + (len(m) % len(k) > 0)))[i])-ord('a'))][ord('z')-ord(c.lower()) >= ord((k*(int(len(m) / len(k)) + (len(m) % len(k) > 0)))[i].lower())-ord('a')]][ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z')] for i,c in enumerate(m))+(':end'))('abc','444'))
