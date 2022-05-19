from flask import Flask, render_template
from random import random
from random import randint
app = Flask(__name__)
@app.route("/")
def home():
        bg_color = "white"
        font_color = "black"
        msg = "Hello"
        value = randint(0, 3)
        names = ['Logic will get you from A to B. Imagination will take you everywhere.', 'There are 10 kinds of people. Those who know binary and those who dont', 'There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies', 'It is pitch dark. You are likely to be eaten by a grue','It is not that is so smart,it is just that I stay with problems longer']
      
        return render_template('index.html', bg_color=bg_color, font_color=font_color, msg=names[value])

if __name__ == '__main__':
       app.run(host="0.0.0.0")
    #margin-top: -100px; 
    #margin-left: -900px; 
