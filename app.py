import pandas
from flask import Flask, render_template, request #importiamo la classe flask
app = Flask(__name__) #inizializza app flask

df = pandas.read_csv("profile.csv")
user = df.iloc[0].to_dict()
@app.route('/') #visitiamo (`/`), la funzione home() viene eseguita.
def home():
    df = pandas.read_csv("profile.csv")
    user = df.iloc[0].to_dict()
    return render_template("index.html",df=user)

@app.route('/modifica_profilo', methods=['GET', 'POST'])  # aggiungi GET per il rendering
def modifica_profilo():
    return render_template("modifica.html")

@app.route('/salva', methods=['GET', 'POST'])  # aggiungi GET per il rendering
def salva():
    nome_nuovo = request.form['nome']
    cognome_nuovo = request.form['cognome']
    user_nuovo = user.update({'Nome': nome_nuovo, 'Cognome': cognome_nuovo})

#avvio flask
if __name__ == '__main__':
    app.run(debug=True) #aggiornamenti in tempo reale