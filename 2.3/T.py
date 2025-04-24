# Хайпанём немножечко

N = int(input())
h = [0] * (N + 1)

for n in range(N):
    bn = int(input())
    hn = bn % 256
    mn = bn // (256 ** 2)
    rn = (bn // 256) % 256
    
    if (hn != (37 * (mn + rn + h[n])) % 256) or (hn >= 100):
        print(n)
        exit()
    else:
        h[n + 1] = hn
        
print(-1)
