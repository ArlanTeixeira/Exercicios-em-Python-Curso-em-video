sal = float(input('Digite o salário: '))
if sal > 1250.00:
    print('O seu novo sálario é de {:.2f}'.format(sal * 0.10 + sal))
else:
    print('O seu novo salário é de {:.2f}'.format(sal * 0.15 + sal))
