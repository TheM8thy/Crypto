def c(s,m):
	r=''
	for c in m:
		if 'A'<=c<='Z' or 'a'<=c<='z':
			if 0<s:
				print([[c,ord('A'),ord(c),s,ord(c)+s,chr(ord(c)+s)],[c,ord('a'),ord(c),s,ord(c)+s,chr(ord(c)+s)]][c.lower()==c])
				if ord(c.lower())-ord('a')+s<=26:
				#if 'A'<=chr(ord(c)+s)<='Z' or 'a'<=chr(ord(c)+s)<='z':
					print("1.1")
					r+=chr(ord(c)+s)
				else:
					print("2.1")
					r+=chr(ord('a')+(s-(ord('z')-ord(c)))-1)
					#r+=chr(ord('a')+(s-(ord('z')-ord(c))-1))
			else:
				if ord(c.lower())-ord('a')+s>=0:
					print("1.2")
					r+=chr(ord(c)+s)
				else:
					print("2.2")
					r+=chr(ord('z')+(ord(c)-ord('a')+s)+1)
		else:
			print("3.")
			r+=c
	return r

print(c(13,"VybirClgu0a"))