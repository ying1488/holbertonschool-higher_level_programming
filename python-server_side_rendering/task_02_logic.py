from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        data = json.load(file)

        item_list = data.get("items", [])
    # "items" can be accessed in items.html
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)