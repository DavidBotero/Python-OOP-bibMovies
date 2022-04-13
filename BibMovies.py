# def standarize(function)
import json
import os

class Film:
    
    def __init__(self, method) -> None:
        self.FilmData = {
            "FilmName": str,
            "DirName": str,
            "Release": str,
            "Genre": str,
            "Cast": []
            }
        
        if method == 1:
            Film.addFilm(self)
        elif method == 2:
            Film.removeFilm(self)
        elif method == 3:
            Film.listFilms(self)
        elif method == 4:
            Film.searchFilm(self)
        elif method == 5:
            Film.modifyFilm(self)


    def addFilm(self):
        self.FilmData["FilmName"] = input("Film's name: ")
        print(self.FilmData["FilmName"])
        self.FilmData["DirName"] = input("Film Director's name: ")
        print(self.FilmData["DirName"])
        self.FilmData["Release"] = input("Release date: ")
        print(self.FilmData["Release"])
        self.FilmData["Genre"] = input("Genre: ")
        print(self.FilmData["Genre"])
        #cast
        while True:
            try:
                cast = int(input("How many people is the cast formed by?: "))
                break
            except:
                print("Invalid input, please introduce a correct one.")
        print("Please introduce the full name of each actor/actress:\n")
        for i in range(1,cast+1):
            person = input(f"{i}.: ")
            self.FilmData["Cast"].append(person)
            print(self.FilmData["Cast"])
        
        with open("./filmsData.json", "a") as Data:
            try:
                Data.write(json.dumps(self.FilmData, indent=3))
                print("Data succesfully added!...")
            except:
                print("Fail registring film's data, q pena so;(...")
            finally:
                Data.close()

    def removeFilm(self):
        print("bajale a la calentura so")


    def listFilms(self):
        print("bajale a la calentura so")


    def searchFilm(self):
        print("bajale a la calentura so")


    def modifyFilm(self):
        print("bajale a la calentura so")


def main():
    while True:
        error = 0
        os.system("clear")

        while True:
            #Menu and Menu validation
            try:
                print("\nHi, please select one option (numericaly): \n\n [1]Add film.\n [2]Remove film.\n [3]List films\n [4]Search film\n [5]Modify film \n [0]Exit")
                if error != 0:
                    selected = int(input("\nInvalid choice, please introduce an existing option.\nChoice: "))
                else:
                    selected = int(input("\nChoice: "))
                print("Bien hecho patrona")
                break
            except:
                error+=1
                os.system("clear")

        if selected != 0:
            Film(selected)
        else:
            os.system("clear")
            print("Vemos so!")
            break


if __name__=="__main__":
    main()