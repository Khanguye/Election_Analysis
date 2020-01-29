import os
import csv
from  datetime import datetime as dt

path_file = os.path.join("Preliminary","Resources","netflix_ratings.csv")
path_file_w = os.path.join("Preliminary","Resources","netflix_ratings.log")

while True:
    found = False
    with open(path_file,"r") as rfile:
        movie_reader = csv.reader(rfile)
        #[title,rating,ratingLevel,ratingDescription,release year,user rating score,user rating size]
        header = next(movie_reader)
        #print(header)
        with open(path_file_w,"a") as wfile:
            #ask for video input
            title = input("What video title are you looking for?")
            #log to the file
            wfile.write(f"{dt.now()}\tYou searched for \"{title}\" Video\n")
            #search for the title
            for movie in movie_reader:
                #print(movie)
                #search with no-case sensitive
                if (title.lower() == movie[0].lower()):
                    found_result = f"{movie[0]} is rated {movie[1]} with a rating of {movie[len(movie)-1]}"  
                    #To the terminal  
                    print(found_result)
                    #log to the file  
                    wfile.write(f"{dt.now()}\t{found_result}\n")
                    found = True
                    break
            if (not found):
                #To the terminal
                print("The video title was not found")
                wfile.write(f"{dt.now()}\tNo Found\n")
    if input("Countinue to search? y (Yes), n (No)") == "n":
        break



