from flask import Flask, render_template, jsonify,request
import requests
from markupsafe import Markup
# import google.generativeai as genai

app = Flask(__name__)


# from langchain_huggingface import HuggingFaceEndpoint
# sec_key="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"

# repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
# llm = HuggingFaceEndpoint(repo_id=repo_id,  temperature=0.7, huggingfacehub_api_token=sec_key)

# def invoke_model(prompt):
#     """Function to send prompt to the Hugging Face model and get response"""
#     try:
#         response = llm.invoke(prompt)
#         return response
#     except Exception as e:
#         error_message = f"Error: {str(e)}"
#         print(error_message)  # Print error message if there's an exception
#         return error_message

# def invoke_model(prompt):
#     """Function to send prompt to the Gemini API and get response."""
#     try:
#         genai.configure(api_key="AIzaSyD0dJZbnmMxAYAplgcrcJDQFmcwc_7dVMw")
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         response = model.generate_content(prompt)
#         return response

#     except requests.exceptions.RequestException as e:
#         error_message = f"Error communicating with Gemini API"
#         print(error_message)
#         return error_message



@app.route("/")
def home():
    page = request.args.get('page', 1, type=int)  # Get the page number from the query string, default to 1
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key=21999cc28a6ea4239ee7b4e251ffc57f&page={page}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    movies = response.json()['results']
    total_pages = response.json().get('total_pages', 1)  # Get the total number of pages
    return render_template("home.html", movies=movies, page=page, total_pages=total_pages)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=21999cc28a6ea4239ee7b4e251ffc57f"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    movies = response.json()
    movie_title = movies['original_title']
    

    prompt = f"You're a well-known film critic who understands the essence of every movie. Share your personal thoughts on the story of {movie_title}. Highlight the **most captivating element** of the movie's plot, and include a popular quote or saying from the film that makes it more intriguing to watch, formatted using <strong> tags and <br/> tags . Keep it simple and brief And Make sure to tell Whether to watch or not to watch as user is a muslim with 'Watch' has a <style> of green text-color and 'Not to Watch' with red text color "

    
    # api_response = invoke_model(prompt)
    # ai = Markup(api_response)
    # print(ai)
    return render_template("movie.html", movie=movies)

@app.route("/search")
def search():
    query = request.args.get('query', '', type=str)
    page = request.args.get('page', 1, type=int)
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&api_key=21999cc28a6ea4239ee7b4e251ffc57f&page={page}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    results = response.json().get('results', [])
    total_pages = response.json().get('total_pages', 1)
    return render_template("home.html", movies=results, page=page, total_pages=total_pages, query=query)

if __name__ == "__main__":
    app.run(debug=False)
