from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles=''
 for row in range(valeur):  
        for spaces in range(valeur- row):  
            etoiles += '+'
        for stars in range(row+1):
            etoiles += '*'
        etoiles += '<br>'
    return etoiles


if __name__ == "__main__":
  app.run(debug=True)
