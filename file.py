from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    Farmer_curensy = 0
    if request.method == 'POST':
        Farmer_curensy = request.form.get('Farmer_backpack', type=str)
    return render_template('index.html', Farmer_backpack=Farmer_curensy)
@app.route("/blog")
def blog_page():
   return 'Блог <a href="/">Вернуться назад</a></p>'

app.run(debug=True)
 