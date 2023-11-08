c='匴倀义刀㕙䌀弱䬀㝔䬀㙃䄀呟刀'
a=''
for i in range(0,len(c),2):
    e=chr(ord(c[i])>>8)
    a+=e
    a+=chr(ord(c[i])-(ord(e)<<8))
print(a)

#Alternatively
#b=''.join([c[i] for i in range(0,len(c),2)])
#a=b.encode('utf-16-be')