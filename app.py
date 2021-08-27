#!flask/bin/python
"""Maybe for real this time"""
import random
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'text': 'Tacos',
        'ing': 'Meat - or alt, tortillas, tomatoes, greek yogurt, salsa, hotsauce, lettuce, beans',
	'dif': 'easy'
    },
    {
        'id': 2,
        'text': 'Pizza Night',
        'ing': 'Doughs, cheeses, tomato sauce, tomato paste, topping choices',
	'dif': 'medium'
    },
    {
        'id': 3,
        'text': 'Mandarin Chicken',
        'ing': 'TJs Orange Chicken, rice',
	'dif': 'crazy easy'
    },
    {
        'id': 4,
        'text': 'Hibachi',
        'ing': 'Meat or alt, rice, zucchini, onions, soy sauce, ginger',
	'dif': 'medium'
    },
    {
        'id': 5,
        'text': 'Steak Night',
        'ing': 'Steaks, EVOO, garlic, mustard, soy sauce, woosh, lemon juice, salt, pepper',
	'dif': 'date night'
    },
    {
        'id': 6,
        'text': 'Bourbon Salmon',
        'ing': 'Salmon, bourbon, brown sugar, pineapple juice, garlic, oil, soy sauce, black pepper',
	'dif': 'date night'
    }
    {
        'id': 7
        'text': 'Nuggies',
        'ing': 'frozen nuggets, mac and cheese side',
	'dif': 'easiest'
    }
    {
        'id': 8,
        'text': 'Steak Night',
        'ing': 'Steaks, EVOO, garlic, mustard, soy sauce, woosh, lemon juice',
	'dif': 'medium'
    }
]



@app.route('/recipe/api/v1.0/recipe/<int:id>', methods=['GET'])
def Get_Recipe(id):
    """Return recipe by ID"""
    if id not in range(1,len(recipes)):
        abort(404)
    recipe = recipes[id-1]
    return jsonify({'recipe': recipe})


	
@app.route('/recipe/api/v1.0/recipe/allrecipes', methods=['GET'])
def Get_Allrecipes():
    """Return all recipes"""
    return jsonify(recipes)

	
@app.route('/recipe/api/v1.0/recipe/recipeoftheday', methods=['GET'])
def Get_Recipeoftheday():
    """Return a random recipe"""
    recipe = random.choice(recipes)
    return jsonify({'Word of the day': recipe['text']}, {'Definition': recipe['def']})

	
@app.route('/recipe/api/v1.0/newrecipe', methods=['POST'])
def Create_Recipe():
    """Adds a recipe to the list"""
	#Example
	#curl -H "Content-Type: application/json" -X POST -d '{"text":"sampletext","def":"sampledef"}' http://localhost:5000/recipe/api/v1.0/newrecipe
    if not request.json or not 'text' in request.json:
        abort(400)
    recipe = {
        'id': len(recipes) + 1,
        'text': request.json.get('text', ""),
        'def': request.json.get('def', "")
    }
    recipes.append(recipe)
    return jsonify({'recipe': recipe}), 201
	

@app.route('/recipe/api/v1.0/DeleteRecipeById/<int:id>', methods=['DELETE'])
def Delete_RecipeById(id):
    """Delete a recipe with the provided recipeID"""
    if id not in range(1,len(recipes)):
        abort(404)
    recipe = recipes[id-1]
    recipes.remove(recipe)
    return jsonify({'Successfully removed the recipe': recipe['text']})


if __name__ == '__main__':
    app.run(debug=True)
