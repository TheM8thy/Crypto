m = "yyyy"
k = "cbcb"
r = ""

for i,c in enumerate(m):
    #print(i,c,k[i])
    #print("dist z: ",ord('z')-ord(c.lower()))
    #print("dist a: ",ord(k[i])-ord('a'))
    if ord('z')-ord(c.lower()) >= ord(k[i])-ord('a'): #shift forward

        r+=chr(ord(c.lower())+ord(k[i])-ord('a'))
        print ("1.")

    elif ord(c.lower())-ord('a') >= ord(k[i])-ord('a'): #shift backward

        #r+=chr(ord(k[i])-(ord('z')-ord(c.lower())+1))
        r+=chr(ord(k[i])-(ord('z')-ord(c.lower()))+(ord(k[i])-ord('a')))
        print ("2.")

    else: #dont shift
        r+=c

print(r)

print((lambda k,m:''.join([[c,chr(ord(k[i])-(ord('z')-ord(c.lower())+1))][ord(c.lower())-ord('a') >= ord(k[i])-ord('a')],chr(ord(c.lower())+ord(k[i])-ord('a'))][ord('z')-ord(c.lower()) >= ord(k[i])-ord('a')] for i,c in enumerate(m)))("yyyy","cbcb"))
