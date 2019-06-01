import textwrap as t
def o(s):
    m = max(len(w) for w in s.split())
    n = len(s)
    d = dict()
    for i in range(m, n):
        m = t.wrap(s, width=i, break_long_words=False)
        p = 2 * (len(max(m, key=len)) + 4) + 2 * (len(m) + 2)
        d[p] = m
    k = min(d.keys())
    l = d[k]
    s = max(len(w) for w in l)
    p = '*' * (s + 4)
    print(p)
    for w in l:
        print('* {:<{}} *'.format(w, s))
    print(p)