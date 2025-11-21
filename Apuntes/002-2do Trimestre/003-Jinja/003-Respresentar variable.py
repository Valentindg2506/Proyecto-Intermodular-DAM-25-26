from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/variable")
def variable():
	return render_template("variable.html")
	

if __name__ == "__main__":
	app.run(debug = True)
