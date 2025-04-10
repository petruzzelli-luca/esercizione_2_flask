import pandas
from flask import Flask, render_template, redirect, url_for, request #importiamo la classe flask
app = Flask(__name__) #inizializza app flask


@app.route('/') #visitiamo (`/`), la funzione home() viene eseguita.
def home():
    df = pandas.read_csv("profile.csv")
    dati = df.iloc[0].to_dict()
    print(dati)
    return render_template("index.html",df=dati)

@app.route("/modifica", methods=["GET", "POST"])
def modifica():
    if request.method == "POST":
        nuovo_profilo = {
            "Nome": request.form["nome"],
            "Cognome": request.form["cognome"],
            "Scuola": request.form["scuola"],
            "Hobby": request.form["hobby"]
        }
        df = pandas.DataFrame([nuovo_profilo])
        df.to_csv("profile.csv", index=False)
        return redirect(url_for('home'))
    df = pandas.read_csv("profile.csv")
    dati = df.iloc[0].to_dict()
    return render_template("modifica.html", dati=dati)



#avvio flask
if __name__ == '__main__':
    app.run(debug=True) #aggiornamenti in tempo reale