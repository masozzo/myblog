print("Ciao Python")
volume = 57
print('Volume =',volume)
if volume < 20:
    print("Piuttosto basso.")
elif 20 <= volume < 40:
    print("Adatto per musica di sottofondo")
elif 40 <= volume < 60:
    print("Perfetto, posso apprezzare ogni dettaglio")
elif 60 <= volume < 80:
    print("Ideale per le feste")
elif 80 <= volume < 100:
    print("Un po' altino!")
else:
    print("Oddio, le mie orecchie! :(")

def ciao(nome):
    if nome == 'Marcello':
        print('Ciao Marcello')
    elif nome == 'Mario':
        print('Ciao Mario')
    else:
        print('Ciao Anonimo')

ciao('Mario')
