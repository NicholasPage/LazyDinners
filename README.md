# LazyDinners


Lazy dinners is a way for me to pick meal choices without thinking too much

A request against the API will return a random recipe in the repository, along with ingredients neccessary

You can also call recipes by ID or list all recipe names with ID.  If a recipe sucks, you can delete it via API.

v2 will build the list from an s3 pull on a json file

v3 have be totally serverless. API calls to Lambda and dynamic updating of the json file with recipes.
