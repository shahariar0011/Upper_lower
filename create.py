from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    choice = request.form.get('choice')
    word = request.form.get('word')

    if choice == '1':
        result = word.upper()
        message = "Converted to Uppercase:"
    elif choice == '2':
        result = word.lower()
        message = "Converted to Lowercase:"
    else:
        result = "Invalid choice"
        message = "Error:"

    return render_template('index.html', result=result, message=message)

if __name__ == '__main__':
    app.run(debug=True)
