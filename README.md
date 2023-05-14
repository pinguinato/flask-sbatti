# Sbattimento Flask

## Posto degli sbattimenti in Flask Python

### Creazione di un environment

        python -m venv mio-ambiente-virtuale

### Freezing delle dipendenze (da lanciare ogni volta che installiamo estensioni nuove)

        pip list

        pip freeze > requirements.txt

### Avvio dell'applicazione da terminale

        python app.py

## Templates

### Importante

Di default Flask usa la certella **templates** per ospitare i file **.html** che dovranno effettuare il rendering dell'output. Flask usa un template engine chiamato **jinja2** per effettuare questo rendering. Come predisporre il progetto per il rendering dei templates con Jinja:

                from flask import render_templates


                @app.route('/')
                def home():
                        return render_template('index.html')

- creare inoltre una cartella /templates dentro il progetto e metterci dentro il file **index.html**.

#### render_template

                from flask import render_template

Provvede add integrare Jinja2 in Flask. Questa funzione prendere il nome del file .html, questa funzione prende in sempre il suo primo argomento, che è il nome del file html. Ogni altro argomento aggiuntivo, che si vuole passare alla funzione da renderizzare nel template html deve essere **key-value pairs** in modo da rappresentare il valore attuale di una variabile referenziata nel template html stesso, ad esempio:

                @app.route('/user/<name>')
                def user(name):
                        return render_template('user.html', name=name)

Questo template riceve una variabile **name** dalla rotta e questa varibile deve poi avere un riscontro nel file .html del template Jinja.
