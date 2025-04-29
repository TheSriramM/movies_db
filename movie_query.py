import sqlite3

DATABASE = "famous_movies.db"
db = sqlite3.connect(DATABASE)
cursor = db.cursor()

#functions
def all_movies_rand():
    query = "SELECT * FROM movies;"
    cursor.execute(query)
    results = cursor.fetchall()
    for movie in results:
        print(movie)

print("Welcome to the classic movies database!")
print("This database contains a compilation of movies that will be remembered throughout time as classics.")
print("What would you like to do? ")
print("1. View all the movies in a random list")
print("2. View all the moveis in a ordered list")
print("3. View a specific set of movies according to release year or director")
order = input("Enter 1, 2 or 3: ")
while True:
    if order == "1":
        all_movies_rand()
        break
