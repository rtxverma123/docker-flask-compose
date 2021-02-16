from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'hello From Flask'

@app.route('/blog')
def blog():
  return 'These are the thoughts on my blog....Care to read them'

@app.route('/home')
def home():
    return render_template("index.html")


if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True)



# @app.route("/about")
# def about():
#   return render_template("about.html")

# if __name__ == "__main__":
#   app.run(debug=True)
