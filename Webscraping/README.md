# Webscraping
El webscraping es una técnica que permite extraer datos de manera automatizada desde sitios web. Consiste en desarrollar programas o scripts que recorren las páginas web, analizan su estructura y extraen la información relevante, como texto, imágenes o tablas. Esta práctica es ampliamente utilizada en diversas industrias para obtener datos en tiempo real, realizar análisis de mercado, monitorizar precios, recopilar información para investigación y muchas otras aplicaciones.

El webscraping se basa en enviar solicitudes HTTP a los servidores web, recibir las respuestas y extraer los datos deseados del código HTML. Para lograrlo, se utilizan diferentes herramientas y bibliotecas en diversos lenguajes de programación.

A continuacion se mostraran y explicaran de manera breve algunos scripts escritos en Python sobre webscraping.

## scrape_quote.py
El script en Python realiza una solicitud GET a una página web y utiliza BeautifulSoup para analizar el contenido HTML. Luego extrae las citas y los autores de la página, los imprime y los guarda en un archivo CSV.

![imagen10](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/5aaa3102-08d8-4d59-8224-fd88e2511acc)

¿Cómo funciona este script?

1. Importar bibliotecas: Se importan las bibliotecas necesarias para el script, incluyendo "requests" para realizar solicitudes HTTP, "csv" para trabajar con archivos CSV y "BeautifulSoup" para analizar el HTML.
2. Definir la URL: Se establece la dirección URL del sitio web que se desea escrapear.
3. Realizar una solicitud GET: Se utiliza la biblioteca "requests" para enviar una solicitud GET a la URL y obtener la respuesta del servidor. La respuesta se guarda en la variable "response".
4. Analizar el HTML: Se utiliza la biblioteca "BeautifulSoup" para analizar sintácticamente el HTML de la respuesta obtenida. Se crea un objeto "html" que representa la estructura del documento HTML.
5. Extraer citas: Mediante el uso de la función "find_all" de "BeautifulSoup", se buscan todos los elementos HTML que tienen la etiqueta "span" y la clase "text". Estos elementos representan las citas en el sitio web. Se guardan las citas en la lista "quotes".
6. Extraer autores: De manera similar al paso anterior, se buscan los elementos HTML que tienen la etiqueta "small" y la clase "author". Estos elementos representan los autores de las citas. Se guardan los autores en la lista "authors".
7. Imprimir citas y autores: Se utiliza un bucle "for" y la función "zip" para iterar sobre las listas de citas y autores al mismo tiempo. Se imprime cada par de cita y autor.
8. Escribir en un archivo CSV: Se abre un archivo CSV llamado "zitate.csv" en modo de escritura. Se utiliza el objeto "csv_writer" para escribir los datos en el archivo CSV. Se utiliza la función "writerows" y la función "zip" para combinar las listas de citas y autores en pares y escribirlos en el archivo CSV.

***El Script scrape_quote.py original se enccuentra en este repositorio, para verlo puedes dar click aqui: [scrape_quote.py](./scrape_quote.py)***



## scrap12.py
este script realiza web scraping en un sitio web de empleos falsos, encuentra trabajos relacionados con Python y muestra información relevante de cada trabajo, como la empresa, la ubicación, el título y la URL de solicitud.

![imagen11](https://github.com/Lion12xD/PIA_LPC062/assets/103289468/c7be0144-5736-46f9-9c27-402c8729d69d)

¿Cómo funciona este script?

1. Importa las bibliotecas necesarias: `requests` para realizar solicitudes HTTP y `BeautifulSoup` para analizar el contenido HTML.
2. Define la URL del sitio web en una variable.
3. Realiza una solicitud GET a la URL utilizando `requests.get()` y guarda la respuesta en la variable `page`.
4. Utiliza `BeautifulSoup` para analizar el contenido de la página utilizando el analizador HTML y almacena el resultado en la variable `soup`.
5. Encuentra el elemento con el identificador "ResultsContainer" en el contenido analizado de la página y guárdalo en la variable `results`.
6. Encuentra todos los elementos de trabajo buscando los elementos "div" con la clase "card-content" dentro de `results` y almacena los resultados en la variable `job_elements`.
7. Filtra los trabajos relacionados con Python buscando los elementos "h2" en los que el texto contenga la palabra "python" en minúsculas utilizando una expresión lambda como criterio. Los resultados se almacenan en la variable `python_jobs`.
8. Crea una lista `python_jobs_elements` que contiene los elementos padres de los elementos `h2` encontrados en el paso anterior.
9. Por cada elemento de trabajo en `python_jobs`:
   - Encuentra el elemento de título ("h2") con la clase "tittle" y guárdalo en la variable `title_element`.
   - Encuentra el elemento de la empresa ("h3") con la clase "company" y guárdalo en la variable `company_element`.
   - Encuentra el elemento de ubicación ("p") con la clase "location" y guárdalo en la variable `location_element`.
   - Encuentra el segundo enlace ("a") dentro del elemento de trabajo y obtén el valor del atributo "href", que representa la URL de solicitud, y guárdalo en la variable `link_url`.
   - Imprime el texto de la empresa, la ubicación, el título y la URL de solicitud utilizando `print()`.
   - Imprime una línea en blanco para separar cada trabajo.

***El Script scrap12.py original se enccuentra en este repositorio, para verlo puedes dar click aqui: [scrap12.py](./scrap12.py)***



Esto seria todo en la seccion de Webscraping!

