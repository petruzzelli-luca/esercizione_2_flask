import pandas
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    df = pandas.read_csv("profile.csv")
    # Converti tutti i profili in una lista di dizionari
    profili = df.to_dict(orient="records")
    return render_template("index.html", profili=profili)

@app.route("/modifica/<int:indice>", methods=["GET", "POST"])
def modifica(indice):
    df = pandas.read_csv("profile.csv")
    if request.method == "POST":
        # Aggiorna solo il profilo specifico
        df.loc[indice, "Nome"] = request.form["nome"]
        df.loc[indice, "Cognome"] = request.form["cognome"]
        df.loc[indice, "Scuola"] = request.form["scuola"]
        df.loc[indice, "Hobby"] = request.form["hobby"]
        df.to_csv("profile.csv", index=False)
        return redirect(url_for('home'))
    
    # Ottieni il profilo specifico da modificare
    dati = df.iloc[indice].to_dict()
    return render_template("modifica.html", dati=dati)


@app.route("/aggiungi", methods=["GET", "POST"])
def aggiungi():
    if request.method == "POST":
        nuovo_profilo = {
            "Nome": request.form["nome"],
            "Cognome": request.form["cognome"],
            "Scuola": request.form["scuola"],
            "Hobby": request.form["hobby"]
        }
        df = pandas.read_csv("profile.csv")
        df_nuovo = pandas.concat([df, pandas.DataFrame([nuovo_profilo])], ignore_index=True)
        df_nuovo.to_csv("profile.csv", index=False)
        return redirect(url_for('home'))
    
    return render_template("aggiungi.html")


if __name__ == '__main__':
    app.run(debug=True)