#!flask/bin/python
"""Maybe for real this time"""
import random
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'text': 'git',
        'ing': 'An idiot'
    },
    {
        'id': 2,
        'text': 'ynan',
        'ing': 'similar to ygran'
    },
    {
        'id': 3,
        'text': 'get tae fuck',
        'ing': 'please remove yourself from my presence'
    },
    {
        'id': 4,
        'text': 'butt',
        'ing': 'Toms face lul'
    },
    {
        'id': 5,
        'text': 'woke',
        'ing': 'see: Nick'
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
