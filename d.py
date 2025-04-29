import sqlite3
    
# Veri tabanı ile bağlantı kurma
connection = sqlite3.connect('movie.db')

# SQL sorgularını çalıştırmak için bir imleç (cursor) oluşturma
cursor = connection.cursor()

cursor.execute("SELECT * FROM movies WHERE budget > 30000000 AND director_id = 5417")

# Sonuçları almak için fetchall() yöntemini kullanma
result = cursor.fetchall()

# Sonuçları ekrana yazdırma
for row in result:
    print(row)
    
# Programın sonunda veri tabanı bağlantısını kapama
connection.close()