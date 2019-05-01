alpha = 'She believed'
beta = 'he lived'

alpha1 = 'helo wlorldo'
beta1 = 'helllo'

alpha2 = 'allo'
beta2 = 'all'

alpha3 = ' '
beta3 = ''




def c(a, b):
    p,r=-1,list(a)
    for i,d in enumerate(b.replace(' ', "")):
        p=a.find(d,p+1)
        r.insert(p+i*2,'[')
        r.insert(p+2+i*2,']')
    return ''.join(r).replace('][','')


ret = c(alpha, beta)

print(ret)
