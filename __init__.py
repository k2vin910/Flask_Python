from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(1,n+1):
        for i in range(j+1):
            etoiles += ' '   
        for i in range(j-1,0,-1):
            etoiles += '0'
        etoiles += '<br>'
    return etoiles

if __name__ == "__main__":
  app.run(debug=True) 
