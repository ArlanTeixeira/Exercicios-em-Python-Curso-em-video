def notas(*n, sit=False):
    r = dict()
    r['Total: '] = len(n)
    r['Maior: '] = max(n)
    r['Menor: '] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r ['Situação'] = 'Boa'
        elif  r['Média'] < 7 > 5:
            r ['Situação'] = 'Regular'
        elif r['Média'] < 5:
            r['Situação'] = 'Ruim'
    return r


resp = notas(5.5, 3.5, 8.5, 4, sit=True)
print(resp)