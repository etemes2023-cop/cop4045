import csv
class IMDB:
    def __init__(self):
        pass

    #Part A
    def display_top_collaborations(self):
        top_rated = open("imdb-top-rated.csv", "r", encoding="windows-1252")
        reader1 = csv.reader(top_rated)
        next(reader1)
        movies = []
        for row in reader1:
            movie = row[1]
            movies.append(movie)

        top_casts = open("imdb-top-casts.csv", "r", encoding="utf-8")
        reader2 = csv.reader(top_casts)
        valid = []
        for row in reader2:
            movie = row[0]
            if movie in movies:
                director = row[2]
                actors = [row[3], row[4], row[5], row[6], row[7]]
                for actor in actors:
                    valid.append((director, actor))

        top_collaborations = {}
        for pair in valid:
            if pair in top_collaborations:
                top_collaborations[pair] += 1
            else:
                top_collaborations[pair] = 1 

        sorted_collaborations = sorted(top_collaborations.items(), key= lambda x:x[1], reverse=True)
        return sorted_collaborations[:10]

    #Part B
    def display_top_actors(self):
        top_grossing = open("imdb-top-grossing.csv", "r", encoding="windows-1252")
        reader1 = csv.reader(top_grossing)
        next(reader1)
        movies = {}
        for row in reader1:
            movie = row[1]
            box_office = int(row[3])
            movies[movie] = box_office
           
        top_actors = open("imdb-top-casts.csv", "r", encoding="utf-8")
        reader2 = csv.reader(top_actors)
        valid = []
        for row in reader2:
            movie = row[0]
            if movie in movies:
                box_office = movies[movie]
                actors = [row[3], row[4], row[5], row[6], row[7]]
                for actor in actors:
                    valid.append((box_office, actor))

        highest_grossing = {}
        for pair in valid:
            actor = pair[1]
            box_office = pair[0]
            if actor in highest_grossing:
                highest_grossing[actor] += box_office
            else:
                highest_grossing[actor] = box_office

        sorted_grossing = sorted(highest_grossing.items(), key= lambda x:x[1], reverse=True)
        return sorted_grossing[:10]

    #Part C       
    def main(self):
        print("Enrique Temes")
        print(self.display_top_collaborations())
        print("\n")
        print(self.display_top_actors())

solution = IMDB()
solution.main()