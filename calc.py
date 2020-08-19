
pi = 3.14159265359


def GCalh_to_kW(power_Gcal_h):
    return power_Gcal_h * 1163


def kW_to_GCalh(power_kW):
    return power_kW / 1163




def pipeG(Q, t1=130, t2=70):
    G = int(1000* Q / (t1 - t2))
    return G

def pipeDn(G, v = 1):
    DN = (20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300)
    dn = int(1000 * (G / 2826 / v) ** 0.5)
    i = 0
    while dn > DN[i]:
        i += 1 
    return DN[i]

def pipev(G, dn):
    v = 10**6 *(G / (dn**2) / 2826)
    return v

def kv(Gmax, dpMin):
    kv = Gmax / (dpMin ** 0.5)
    return kv

def dp(Gmax, kvs):
    return (Gmax / kvs)
    

# Q = c (t1 - t2) g  #gcal_h
# g = q / c * (t1 - t2)

# g = 1000 * 0.155 / (0.966 * 20)
# print(g)


# DN_pipe = (20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300)

# a = 50 

# print(DN_pipe[DN_pipe.index(a) + 1])