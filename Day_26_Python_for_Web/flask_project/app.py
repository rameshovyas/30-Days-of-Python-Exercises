from flask import Flask, render_template

app = Flask(__name__)

# Create home route
@app.route('/') 
def home ():
    cities = ["Jodhpur", "Hyderabad", "Banglore", "Puri"]
    name = "30 Days of Python Programming Solutions"
    return render_template('index.html', cities= cities, name=name, title='Home')
    
# Create about route
@app.route('/about') 
def about ():
    name = "30 Days of Python Programming Solutions"
    return render_template('about.html', name=name, title = 'About Us')

# Spin the server
if __name__ == "__main__":
  app.run()