def urna(votos):
    # Write your code here
    va = 0
    vb = 0
    vc = 0
    mv = ''
    for v in votos:
        if v == 'A':
            va +=1
        elif v == 'B':
            vb +=1
        elif v == 'C':
             vc +=1

        if va > vb > vc:
            mv = 'A'
        elif vb > va > vc:
            mv = 'B'
        else:
            mv = 'C'
    return mv