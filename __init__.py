from flask import Flask

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(1, valeur + 1):
        etoiles += ' ' * (valeur - j)  # Adding spaces for alignment
        etoiles += '*' * j  # Adding stars
        etoiles += '<br>'  # HTML line break
    return etoiles

if __name__ == "__main__":
    app.run(debug=True)
