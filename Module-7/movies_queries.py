import mysql.connector

# Configuration dictionary for database connection
config = {
    "user": "root",
    "password": "MySQL1520$",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    # Connect to the MySQL database using the configuration dictionary
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Query 1: Select all fields from the studio table
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}")
        print()

    # Query 2: Select all fields from the genre table
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}")
        print()

    # Query 3: Select movie names for movies with runtime less than two hours
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    short_films = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for film in short_films:
        print(f"Film Name: {film[0]}")
        print(f"Runtime: {film[1]}")
        print()

    # Query 4: Select film names and directors grouped by director
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    films_directors = cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order --")
    for film in films_directors:
        print(f"Film Name: {film[0]}")
        print(f"Director: {film[1]}")
        print()

except mysql.connector.Error as err:
    print("Error:", err)
finally:
    # Close the cursor and the connection
    if db.is_connected():
        cursor.close()
        db.close()
        print("MySQL connection is closed")


