def p(matrix,m):
	r=''
	for c in m:
	    for row in matrix:
	        for column in row:
	            if c in column:
	                r+=str(row.index(column)+1)+str(matrix.index(row)+1)
	                break
	
	return r

print("start:"+p([['A','B','C','D','E'],['F','G','HI','J','K'],['L','M','N','O','P'],['Q','R','S','T','U'],['V','W','X','Y','Z']],"ABDF")+":end")

(lambda matrix,m:([[[print(str(row.index(column)+1)+str(matrix.index(row)+1)) for column in row if c in column] for row in matrix] for c in m]))([['A','B','C','D','E'],['F','G','HI','J','K'],['L','M','N','O','P'],['Q','R','S','T','U'],['V','W','X','Y','Z']],m = "ABDF")