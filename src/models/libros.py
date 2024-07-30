# importar la función que devolverá una instancia de una conexión
from config.db import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Libros:
    def __init__( self , data ):
        self.id_libro = data['id_libro']
        self.isbn = data['isbn']
        self.titulo = data['titulo']
        self.descripcion = data['descripcion']
        self.paginas = data['paginas']
        self.imagen = data['imagen']
        self.fecha_publicacion = data['fecha_publicacion']

    # ahora usamos métodos de clase para consultar nuestra base de datos
    # SELECT * FROM tareas ORDER BY (()) ASC LIMIT 50 SKIP 10;
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM libros;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('biblionauta').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        books = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for book in results:
            books.append( cls(book) )
        return books
    def get_all_for_category(cls, category):
        query = f"SELECT * FROM libros WHERE id_libro IN (%s);" % ','.join(map(str, category))
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('biblionauta').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        books = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for book in results:
            books.append( cls(book) )
        return books
    def get_book(cls, bookid):
        query = f"SELECT * FROM libros WHERE id_libro = {int(bookid)};"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('biblionauta').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        return results
    
    @classmethod
    def search(cls, letter):
        query = f"SELECT * FROM libros WHERE titulo LIKE '%{letter}%';"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('biblionauta').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        books = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for book in results:
            books.append( cls(book) )
        return books