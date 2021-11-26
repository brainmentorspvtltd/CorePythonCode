dataset = {
    "action" : ["Ironman","Thor","KGF", "Batman","Superman","Aquaman","Hulk","Baahubali",
                "Master","Avengers"],
    "comedy" : ["Thor","Golmaal","Hera Pheri", "Dhamaal", "Yes man", "The mask"],
    "sci-fi" : ["Ironman","Interstellar", "Gravity"],
    "thriller" : ["Oculus","KGF","Superman","Master","Avengers","It","Kahani"],
    "horror" : ["Oculus","It","The Nun"]
}

user1 = {"Ironman","Avengers","Gravity","It","The mask","Thor","Hulk","Batman","KGF"}
user2 = {"Ironman","Master","Gravity","It","Golmaal","Thor","Aquaman","KGF"}

scores = {}
for key in dataset:
    movies = set(dataset[key])
    common_movies = user1.intersection(user2)
    score = len(movies.intersection(common_movies)) / len(movies.union(common_movies))
    scores[key] = score

max_value = max(scores.values())
for key in scores:
    if scores[key] == max_value:
        category = key
        break
rec1 = set(dataset[category] - user2)
rec2 = set(dataset[category] - user2)
print("movie recommended to user 1", rec1)
print("movie recommended to user 1", rec2)