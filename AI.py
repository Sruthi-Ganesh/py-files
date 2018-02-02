p=[0.2,0.2,0.2,0.2,0.2]
world=['green','red','red','green','green']
pHit=0.6
pMiss=0.2

Z='green'

def sense(p,Z,world):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    sumval=sum(q)
    if sumval!=1:
     for i in range(len(q)):
        q[i]=q[i]/sumval
    return q

print sense(p,Z,world)
