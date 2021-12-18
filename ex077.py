palavras = ('aprender', 'programar', 'curson', 'python',
            'aula', 'video', 'trabalhar', 'praticar',
            'mercado', 'futuro', 'linguagem')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=" ")
    for letras in p:
        if letras in 'aeiou':
            print(letras, end=" ")
