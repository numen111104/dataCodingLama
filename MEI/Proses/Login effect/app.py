from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Placeholder for checking if the user exists in the database
    if email == 'example@example.com' and password == 'password':
        return redirect('/home')
    else:
        return redirect('/')

@app.route('/home')
def home():
    return 'Welcome Home'

if __name__ == '__main__':
    app.run(debug=True)
