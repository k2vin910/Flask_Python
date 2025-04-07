from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)

@app.route('/<int:valeur>')
def counter(n):
    somme = 0  # Initialisation de la somme

    for i in range(1, n + 1):
        if i % 11 == 0:
            continue  # Si divisible par 11, on passe au prochain nombre
        if i % 5 == 0 or i % 7 == 0:
            somme += i  # Si divisible par 5 ou 7, on ajoute à la somme

        if somme => 5000:
            break  # Si la somme dépasse 5000, on arrête la boucle

    return f"La somme finale est : {somme}"

if __name__ == "__main__":
    app.run(debug=True)

