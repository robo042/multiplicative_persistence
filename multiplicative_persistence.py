#!/usr/bin/env python3

def baseb(n, b):
    e, q = n//b, n%b
    return n if n == 0 else n%b if e == 0 else int(str(baseb(e, b)) + str(q))

def prod(n_list, base = 10):
    return baseb(n_list[0]*(prod(n_list[1:]) if len(n_list)>1 else 1), base)

def m_persistence(n, base = 10, show_steps = True):
    if int(str(n), base)<0 or not all([x.isdigit() for x in str(n)]):
        raise ValueError("n must be a positive integer: '" + str(n) + "'")
    steps = 0
    while n and len(str(n))>1:
        if show_steps: print(n)
        n, steps = prod([int(x) for x in str(n)], base = base), steps + 1
    if show_steps: print((str(n) + '\nSteps: ' if show_steps else ''), end ='')
    return steps
