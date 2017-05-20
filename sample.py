import sqlite3
db = sqlite3.connect('grok.db')
cursor = db.cursor()
cursor.execute('create table chamados (categoria text, qtd_chamados integer)')
categorias = [('Categoria A', 10),
              ('Categoria B', 20),
              ('Categoria C', 30),
              ('Categoria D', 40)]
cursor.executemany('insert into chamados values (?, ?)', categorias)
db.commit()
db.close()
