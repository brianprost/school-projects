import json

# TODO: would love to make this a lambda function, but i'm dumb
def get_wine_stars(wine_rating):
    # TODO: move to DynamoDB
    with open('wine/wines.json') as f:
        wine_db = json.load(f)

    if wine_rating < 0:
        return "He hasn't tried this one yet! Feel free to buy him one."

    num_stars = round(wine_rating * 5)
    star_rating = ""
    for i in range(num_stars):
        star_rating += "\u2605"
    while len(star_rating) < 5:
        star_rating += "\u2606"
    return star_rating

if __name__ == "__main__":
    cab_rating = get_wine_stars(1)
    print(f"Cabernet Sauvignon is always {cab_rating}")