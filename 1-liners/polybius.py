def p_enc(matrix,m):
	r=''
	for c in m:
		for row in matrix:
			for column in row:
				if c in column:
					r+=str(row.index(column)+1)+str(matrix.index(row)+1)
					break
	return r

def p_dec(matrix,c):
	r=''
	for n in [c[i:i+2] for i,v in enumerate(c) if i%2 == 0]:
		r+=matrix[int(n[1])-1][int(n[0])-1]
	return r

print("start:"+p_enc([['A','B','C','D','E'],['F','G','H/I','J','K'],['L','M','N','O','P'],['Q','R','S','T','U'],['V','W','X','Y','Z']],"ABDF")+":end")
print("start:"+p_dec([['A','B','C','D','E'],['F','G','H/I','J','K'],['L','M','N','O','P'],['Q','R','S','T','U'],['V','W','X','Y','Z']],"11214112")+":end")

#encrypt
(lambda matrix,m:([[[print(str(row.index(column)+1)+str(matrix.index(row)+1),end='') for column in row if c in column] for row in matrix] for c in m]))([['A','B','C','D','E'],['F','G','H/I','J','K'],['L','M','N','O','P'],['Q','R','S','T','U'],['V','W','X','Y','Z']],m = "ABDF")
print()#newline
#decrypt
print("start:"+(lambda matrix,c:''.join(matrix[int(n[1])-1][int(n[0])-1] for n in [c[i:i+2] for i,v in enumerate(c) if i%2 == 0]))([['A','B','C','D','E'],['F','G','H/I','J','K'],['L','M','N','O','P'],['Q','R','S','T','U'],['V','W','X','Y','Z']],"11214112")+":end")
