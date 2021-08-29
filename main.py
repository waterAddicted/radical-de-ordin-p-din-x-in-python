
def ridicare_la_putere(x,p):
    r = float(1)
    while p != 0:
        print(1)
        if p % 2 == 1:
            r = r * x
        x = x * x
        p //= 2
    return r


def radical_de_ordin_p(x,p):
    st = float(0)
    dr = float(x)
    mij = (st + dr) / 2
    pmij = float(ridicare_la_putere(mij,p))
    while abs(pmij - x) > eps:
        if pmij < x:
            st = mij
        else:
            dr = mij
        mij = (st + dr)/2
        pmij = float(ridicare_la_putere(mij,p))
    return mij

x = float(input())
p = int(input())
eps = 0.0001
print(radical_de_ordin_p(x,p))