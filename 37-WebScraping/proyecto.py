import requests
import bs4 # type: ignore

##crear URL sin numero de pagina

url_base = 'https://books.toscrape.com/catalogue/category/books_1/page-{}.html'

#lista de títulos con 4 o 5 estrellas 
titulos_rating_alto = []

#iterar entre paginas
for pagina in range(1, 51):
    #crear soup en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')
    
    libros = sopa.select('.product_pod')

    #iterar libros
    
    for libro in libros:
        #VERIFICAR QUE LOS LIBROS TENGAN 4 O 5 ESTRELLAS
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
           #GUARDAR TITULO EN LA VARIABLE TITULO_LIBRO
            titulo_libro = libro.select('a') [1] ['title'] #ESTA TRAYENDO LOS TITULOS DE LOS LIBROS 
        
            #AGREGAR LIBRO A LISTA
            titulos_rating_alto.append(titulo_libro)
            
for t in titulos_rating_alto:
    print(t)