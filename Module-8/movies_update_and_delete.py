import mysql.connector

# Configuration dictionary for database connection
config = {
    "user": "root",
    "password": "MySQL1520$",  
    "host": "localhost",
    "database": "movies",
}
db = mysql.connector.connect(**config)
cursor = db.cursor()

# Function to display films
def show_films(cursor, title):
    query = """
    SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name'
    FROM film
    INNER JOIN genre ON film.genre_id = genre.genre_id
    INNER JOIN studio ON film.studio_id = studio.studio_id
    ORDER BY film_name
    """
    cursor.execute(query)
    films = cursor.fetchall()
    
    print(f"\n-- {title} --")
    for film in films:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}")
        print(f"Genre: {film[2]}")
        print(f"Studio Name: {film[3]}\n")

cursor.execute("DELETE FROM film WHERE film_name IN ('Gladiator', 'Alien', 'Get Out', 'Avatar', 'Star Wars')")
db.commit()

# Insert initial films
initial_films = [
    ("Gladiator", "Ridley Scott", "Drama", "Universal Pictures", 155),
    ("Alien", "Ridley Scott", "SciFi", "20th Century Fox", 117),
    ("Get Out", "Jordan Peele", "Horror", "Blumhouse Productions", 104)
]

for film in initial_films:
    cursor.execute("""
    INSERT INTO film (film_name, film_director, genre_id, studio_id, film_runtime)
    VALUES (%s, %s, (SELECT genre_id FROM genre WHERE genre_name=%s), 
    (SELECT studio_id FROM studio WHERE studio_name=%s), %s)
    """, film)
db.commit()

# Display initial films
show_films(cursor, "DISPLAYING FILMS")

# Insert a new film 'Avatar'
cursor.execute("""
INSERT INTO film (film_name, film_director, genre_id, studio_id, film_runtime)
VALUES ('Avatar', 'James Cameron', (SELECT genre_id FROM genre WHERE genre_name='SciFi'), 
(SELECT studio_id FROM studio WHERE studio_name='20th Century Fox'), 162)
""")
db.commit()
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Update the film 'Alien' to be a 'Horror' film
cursor.execute("""
UPDATE film
SET genre_id = (SELECT genre_id FROM genre WHERE genre_name='Horror')
WHERE film_name = 'Alien'
""")
db.commit()
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

# Delete the film 'Gladiator'
cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
db.commit()
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

# Close the cursor and database connection
cursor.close()
db.close()