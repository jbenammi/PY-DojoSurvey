from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "I<3Secrets"

@app.route('/')
def index():
	if "val_name" not in session:
		session['val_name'] = ""
	if "val_location" not in session:
		session['val_location'] = ""
	if "val_lang" not in session:
		session['val_lang'] = ""
	if "val_comment" not in session:
		session['val_comment'] = ""
	return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
	del session['val_name']
	del session['val_location']
	del session['val_lang']
	del session['val_comment']
	val_count = 0
	if request.form['name'] == "":
		session['val_name'] = "The name field is required"
		val_count += 1
	if request.form['location'] == "":
		session['val_location'] = "The location field is required"
		val_count += 1
	if request.form['lang'] == "":
		session['val_lang'] = "The language field is required"
		val_count += 1
	if request.form['comment'] == "":
		session['val_comment'] = "The comment field is required"
		val_count += 1
	elif len(request.form['comment']) > 120:
		session['val_comment'] = "The comment field cannot be longer than 120 characters"
		val_count += 1
	if val_count > 0:	
		return redirect('/')	
	else:
		info = {"name": request.form['name'], "location": request.form['location'], "lang": request.form['lang'], "comment": request.form['comment']}
		return render_template('results.html', info = info)
		

app.run(debug=True)