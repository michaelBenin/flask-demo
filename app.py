from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods = ['GET', 'POST'])
def login():
  message = 'Hi, please login'
  if request.method == 'POST':
    message = 'Thanks for loggin in '
    username = request.form['username']
    password = request.form['password']
  return render_template('login.html', username = username, password = password)

@app.route("/api/<method>")
def api(method):
    data = {
      'foo': 'bar',
      'method': method
    }
    response = jsonify(data)
    response.status_code = 200
    return response
    
@app.route("/blog/<slug>")
def blog(slug):
  data = {
    'slug': slug
  }
  return render_template('blog.html', data = data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=1337)