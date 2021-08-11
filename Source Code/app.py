from flask import Flask, render_template, request
from Code import recommend

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def show_index_html():
    return render_template('index.html', headings = {}, data = {})

@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        sear = request.form['sear']
        movies,genres,director_name = recommend(sear)
        return render_template('index.html', headings = ["Movies"], movies = movies,genres=genres,director_name=director_name)

if __name__ == '__main__':
    app.run(debug=True)