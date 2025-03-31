from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for i in range(valeur):
        etoiles += '*' 
    return etoiles 
    
    def carre_etoile(count):
        count=5
    for i in range (count):
        
    return ('*'* valeur)


if __name__ == "__main__":
  app.run(debug=True)
