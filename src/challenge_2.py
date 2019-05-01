import textwrap as t
def o(s):
    m=t.wrap(s, width=int(len(s)/2), break_long_words=False)
    s=max(len(w) for w in m)
    p = '*' * (s + 4)
    print(p)
    for word in m:
        print('* {:<{}} *'.format(word, s))
    print(p)

o("Hello World in a frame")
o("Hellooooooooooo wtf is this")
o("Wtf is this")
o("Helllllllllllllllo o")
