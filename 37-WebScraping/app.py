import requests
import bs4 

resultado = requests.get('https://primerreporte.com/2024/06/18/estudiantes-de-arquitectura-uide-loja-en-gira-nacional/')


#TRAE TODO EL CODIGO FUENTE DEL SITIO
#print (resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'html.parser')


#TITULO SEL SITIO WEB

###print(sopa.select('title')[0].get_text())

#TRAER NUMERO DE ETIQUETAS P´s (PARRAFOS)
#print(len(sopa.select('p')))

#TRAER EL PARRAFO 2 
parrafo = sopa.select('p')[2].get_text()
#print(parrafo)

##TRAER LA COLUMNA LATERAL DE LA PAGINA
columna_lateral = sopa.select('.widget-title')
for p in columna_lateral:
    print(p.get_text())
    

##EXTRAER IMAGENES

imagenes = sopa.select('.custom-logo')[0]['src']
#print(imagenes)

logo_empresa = requests.get(imagenes)
#print(logo_empresa.content)

#guardar las imagenes

f = open('logo.png','wb')
f.write(logo_empresa.content)
f.close()