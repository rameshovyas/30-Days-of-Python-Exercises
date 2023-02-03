from flask import Flask, render_template

app = Flask(__name__)

# Create home route
@app.route('/') 
def home ():
    return render_template('index.html')
    

# Spin the server
if __name__ == "__main__":
  app.run()