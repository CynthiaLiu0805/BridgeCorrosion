from flask import Flask, render_template, request
import pandas as pd
import search, inputCheck
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if inputCheck.is_within_ontario(request.form['latitude'], request.form['longitude']):
            return search.search_coordinates()
        else:
            return render_template('index.html', warning="The coordinates are not within Ontario.")

    else:
        return render_template('index.html')



if __name__ == '__main__':

    app.run(debug=True)