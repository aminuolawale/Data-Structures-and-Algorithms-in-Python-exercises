def p_norm(V, p):
    return sum(v**p for v in V )**(1/p)


print(p_norm([3,4],2))