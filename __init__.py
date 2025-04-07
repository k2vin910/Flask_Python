from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  

@app.route('/<int:valeur>')
def exercice(valeur):
    a,b=0,1
count= str[str(0)]
    if valeur > 1:
        count.append(str(b))  # Then 1

    for _ in range(2, valeur):
        c = a + b
        count.append(str(c))
        a, b = b, c

    # Return the sequence nicely formatted
return ', '.join(count)



if __name__ == "__main__":
    app.run(debug=True)
