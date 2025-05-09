"""This python code is for querying data from my classic movies database
    Here are a list of options you can choose to query from this database: 
    1. View all the movies in a random list
    2. View all the movies in a ordered list (ordered by year of release or ordered by rating)
    3. View a specific subset of the movies database that contains movies from within a certain timeframe or from a specific director
    (When you are searching for movies from a specific director, you don't need to enter the full name. Just part of the name is fine.)
    4. If you don't want to query this database you can quit the program"""

import sqlite3

#Connect to the movies database
DATABASE = "famous_movies.db"
db = sqlite3.connect(DATABASE)
cursor = db.cursor()

#Functions
def print_results():
    cursor.execute(query)
    results = cursor.fetchall()
    print("     Movie                                           Director              Year     Rating")
    for movie in results:
        print(f"{movie[1]:<48} {movie[2]:<25} {movie[3]:<10} {movie[4]}")

def timeframe():
    query = "SELECT * FROM movies WHERE year >= ? AND year <= ? ORDER BY year ASC;"
    cursor.execute(query, (year1, year2))
    results = cursor.fetchall()
    if results:
        print("     Movie                                           Director              Year     Rating")
        for movie in results:
            print(f"{movie[1]:<48} {movie[2]:<25} {movie[3]:<10} {movie[4]}")
    else:
        print("There are no movies within that timeframe in my database!")

def director_movies():
    query = "SELECT * FROM movies WHERE director LIKE ?"
    cursor.execute(query, ('%' + director + '%',))
    results = cursor.fetchall()
    if results:
        print("     Movie                                           Director              Year     Rating")
        for movie in results:
            print(f"{movie[1]:<48} {movie[2]:<25} {movie[3]:<10} {movie[4]}")
    else:
        print("This database doesn't have any directors with that name!")
        print("Please pick another director to search for!")

#Main code
print("Welcome to the classic movies database!")
print("This database contains a compilation of movies that will be remembered throughout time as classics.")
print("What would you like to do? ")
print("1. View all the movies in a random list")
print("2. View all the moveis in a ordered list")
print("3. View a specific set of movies according to release year or director")
print("4. Quit Program")
order = input("Enter 1, 2, 3 or 4: ")
while True:
    #Check which order the user has chosen
    if order == "1":
        query = "SELECT * FROM movies;"
        print_results()
        break
    elif order == "2":
        #Ask the user what to sort by
        sort = input("What would you like to order the list by (year or rating)? ")
        sort = sort.lower()
        while True:
            if sort == "year":
                #Ask if the user wants new movies or old movies at the top
                asc_dsc = input("Sorted by oldest at the top or newest at the top (new or old)? ")
                while True:
                    asc_dsc = asc_dsc.lower()
                    #Code for new movies at the top
                    if asc_dsc == "new":
                        query = "SELECT * FROM movies ORDER BY year DESC;"
                        print_results()
                        order = "done"
                        break
                    #Code for old movies at the top
                    elif asc_dsc == "old":
                        query = "SELECT * FROM movies ORDER BY year ASC;"
                        print_results()
                        order = "done"
                        break
                    else:
                        #Invalid input
                        asc_dsc = input("Please enter a valid input (old or new): ")
                break
            elif sort == "rating":
                #Ask the user if the lowest ratings or the highest ratings should be at the top
                asc_dsc = input("Sorted by lowest or highest ratings (low or high)? ")
                while True:
                    asc_dsc = asc_dsc.lower()
                    if asc_dsc == "high":
                        query = "SELECT * FROM movies ORDER BY rating DESC;"
                        print_results()
                        order = "done"
                        break
                    elif asc_dsc == "low":
                        query = "SELECT * FROM movies ORDER BY rating ASC;"
                        print_results()
                        order = "done"
                        break
                    else:
                        #Invalid input
                        asc_dsc = input("Please enter a valid input (low or high): ")
                break
            else:
                #Invalid input
                sort = input("Please enter a valid input for what to sort the list of movies by (year or rating): ")
        break
    elif order == "3":
        subset = input("Would you like a selection of movies that were released within a certain timeframe or from a specific director (time or director)? ")
        subset = subset.lower()
        while True:
            if subset == "time":
                try:
                    print("Enter 2 years and the movies that were released in that time frame will be shown in the list")
                    while True:
                        year1 = int(input("Year 1: "))
                        year2 = int(input("Year 2: "))
                        if year2 - year1 < 0:
                            print("Please enter the smallest year first and then the larger year.")
                        elif year2 < 1939:
                            print("Please enter a year after 1939. This database does not contain movies older than that")
                        elif year1 > 2025:
                            print("You can't view movies from the future!")
                        else:
                            break
                except ValueError:
                    print("Please enter two valid years after 1939")
                timeframe()
                order = "done"
                break
            elif subset == "director":
                director = input("What director would you like to search for? ")
                director_movies()
            else:
                subset = input("Please enter a valid input (time or director): ")
    elif order == "4":
        break
    elif order == "done":
        break
    else:
        order = input("Please enter a number between 1 and 4: ")