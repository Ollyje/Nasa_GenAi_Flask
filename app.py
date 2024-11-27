from flask import Flask, render_template, request
from nasa_genai_flask import ask_question

# app is a variable representing 
# our flask app
# __name__ is a python reserved 
# word
# telling Flask where our code
# lives
app = Flask(__name__)

# set up our landing page
@app.route('/')
def index():
	
	return render_template('index.html', question = "Type question here!", chatbot_reponse = "")

# only use this when posting data!
@app.route('/', methods=['POST'])
def index_post():
	user_question = request.form['req_question']
	chatbot_response = ask_question(user_question)
	return render_template('index.html', question = user_question, chatbot_reponse = chatbot_reponse)