import textwrap as t
def o(s):
    minWidth = max(len(w) for w in s.split())
    maxWidth = len(s)
    dictio = dict()
    for i in range(minWidth, maxWidth):
        m = t.wrap(s, width=i, break_long_words=False)
        p = 2 * (len(max(m, key=len)) + 4) + 2 * (len(m) + 2)
        dictio[p] = m
    mini = min(dictio.keys())
    liste = dictio[mini]
    s = max(len(w) for w in liste)
    p = '*' * (s + 4)
    print(p)
    for word in liste:
        print('* {:<{}} *'.format(word, s))
    print(p)

o("Hello World in a frame")
o("Hellooooooooooo wtf is this")
o("Wtf is this")
o("Helllllllllllllllo o")
