def c(a, b):
    p,r=-1,list(a)
    for i,d in enumerate(b.lower().replace(' ', '')):
        p=a.lower().find(d,p+1)
        r[:p+i*2]+='['
        r[:p+2+i*2]+=']'
    return ''.join(r).replace('][','')