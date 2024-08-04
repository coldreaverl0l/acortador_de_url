#este programa permite acortar URL
#primero importamos la libreria
import pyshorteners


#ingresamos la URL original
url = input('ingrese la URL a acortar: ')

#creamos una instancia acortadora de URL
shortener = pyshorteners.Shortener()

# Acorta la URL
url_corta = shortener.tinyurl.short(url)

#la mostramos en pantalla
print('la url corta es: ')
print('\n')
print(url_corta)
