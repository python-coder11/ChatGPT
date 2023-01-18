from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key = "YOUR_API_KEY"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
	question = request.form['question']
	response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=1024,
		temperature=0,
		n=1,
		stop=None
    )
	
	answer = response["choices"][0]["text"]

	return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
 
