import webbrowser
try:
    webbrowser.get("http://www.pudim.com.br")
except:
    print('Site do pudim não está acessível!')
else:
    print('Site do pudim está online')
