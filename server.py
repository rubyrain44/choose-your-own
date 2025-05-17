from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"
#////////////////////////////////////////////////////////


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/initialize', methods=['POST'])
def initialize():
    session['name'] = request.form["name"].title()
    return redirect('/start')

@app.route('/start')
def start():
    return render_template("start.html")

# PATH ONE CHOICES -- VACATION

# PATH TWO CHOICES -- MUSEUM/JUNGLE

# PATH THREE CHOICES -- BAR/BEACH/CAVE





#////////////////////////////////////////////////////////
if __name__ == "__main__":
    app.run(debug=True)