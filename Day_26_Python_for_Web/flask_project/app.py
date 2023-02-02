from flask import Flask

app = Flask(__name__)

# Create home route
@app.route('/') 
def home ():
    return '<h1>Welcome</h1>'

# Spin the server
if __name__ == "__main__":
  app.run()