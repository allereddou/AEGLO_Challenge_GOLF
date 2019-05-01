alpha = 'She believed'
beta = 'he lived'

alpha1 = 'helo wlorldo'
beta1 = 'helllo'

alpha2 = 'allo'
beta2 = 'all'

alpha3 = ' '
beta3 = ''


# Working
# def challenge(a, b):
#     offset, position, last_position, ret = 0, 0, -1, list(a)
#     for i in b:
#         position = a.find(i, last_position + 1)
#         last_position = position
#         ret.insert(position + offset, '[')
#         ret.insert(position + 2 + offset, ']')
#         offset += 2
#     return ''.join(ret).replace('][', '')

# Working too
# def challenge(a, b):
#     position, last_position, ret = 0, -1, list(a)
#     for index, item in enumerate(b):
#         position = a.find(item, last_position + 1)
#         last_position = position
#         ret.insert(position + index * 2, '[')
#         ret.insert(position + 2 + index * 2, ']')
#     return ''.join(ret).replace('][', '')


def c(a, b):
    p,r=-1,list(a)
    for i,d in enumerate(b.replace(' ', "")):
        p=a.find(d,p+1)
        r.insert(p+i*2,'[')
        r.insert(p+2+i*2,']')
    return ''.join(r).replace('][','')



ret = c(alpha, beta)

print(ret)
