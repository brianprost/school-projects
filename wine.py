import json

with open('wines.json') as f:
    wine_db = json.load(f)

wine_to_rate = wine_db["white"]["sauvignon blanc"]["brian's rating"]

# TODO: would love to make this a lambda function, but i'm dumb
def get_wine_stars(wine_rating):
    if wine_rating is -1:
        return "He hasn't tried this one yet! Feel free to buy him one."
    num_stars = round(wine_rating * 5)
    star_rating = ""
    for i in range(num_stars):
        star_rating += "\u2605"
    while len(star_rating) < 5:
        star_rating += "\u2606"
    return star_rating

print(get_wine_stars(wine_to_rate))