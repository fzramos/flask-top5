from top5_app import app

from flask import render_template

# Default route
@app.route('/')
def home():
    return render_template('home.html')

# List route
@app.route('/mylist')
def myList():
    myTop = {
        '1': 'Great Pyramid of Giza',
        '2': 'Eiffel Tower',
        '3': 'Machu Piccu',
        '4': 'Taj Mahal',
        '0': 'Basilica of the Sagrada Familia'
    }

    return render_template('my_list.html', myTop5 = myTop)