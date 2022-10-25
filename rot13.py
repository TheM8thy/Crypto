def r(m):
	r=""
	for c in m:
		if 'a'<=c.lower()<='m':
			r+=chr(ord(c)+13)
		elif 'n'<=c.lower()<='z':
			r+=chr(ord(c)-13)
		else:
			r+=c
	return r

print("start:"+r("VybirClgu0a")+":end")

print((lambda m:'start:'+''.join([[c,chr(ord(c)-13)]['n'<=c.lower()<='z'],chr(ord(c)+13)]['a'<=c.lower()<='m'] for c in m)+':end')("VybirClgu0a"))
