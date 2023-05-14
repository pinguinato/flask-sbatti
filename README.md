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

Questo template riceve una variabile **name** dalla rotta e questa variabile deve poi avere un riscontro nel file .html del template Jinja.

**name=name** può confondere, facciamo chiarezza: il parametro name sulla sinistra indica quello richiamato nel file di template user.html, mentre il parametro sulla destra rappresenta quello corrente nella rotta.

#### Sintassi Jinja2

Il modo in cui nel file html ho di richiamare il parametro passato in rotta, descritta sopra:

                {{ name }}

Ad esempio:

                <h1>Hello {{ name }}</h1>

Jinja può riconoscere variabili di diverso tipo:

- valori dizionario
- liste
- valore da una lista
- valore da un metodo di un oggetto

Ad esempio:

                {{ name['key'] }}

                {{ name_list[3] }}

                {{ name_list[my_name] }}

                {{ name.some_method() }}

Possibilità di usare anche dei **filtri**:

                <h1>Hello, {{ name|capitalize }}

Esempi di filtri:

- safe (renderizza il valore senza aplpicare escape)
- capitalize (converte la prima lettera in maiuscolo)
- lower (converte in minuscolo tutto)
- upper (converte in maiuscolo tutto)
- title
- trim (rimuove tutti gli spazi bianchi ad inizio e fine stringa)
- striptags (rimuove tutti i valori html prima del rendering del valore stesso)

**N.B.** Jinja di default effettua l'escape su tutti le varibili nel template per questioni di sicurezza.

Non usare il filtro *safe* sulle variabili non protette dei form dove vengono immmessi dati degli utenti!

##### Strutture di controllo Jinja2

Esempio di strutture di controllo:

                {% if user %}
                        Hello {{ user }}
                {% else %}
                        Hello stranger
                {% endif %}

                <ul>
                        {% for comment in comments %}
                                <li>{{ comment }}</li>
                        {% endfor %}
                </ul>

##### Macro

Jinja2 supporta le Macro che sono simili a delle funzioni del codice Python

Esempio:

                {% macro render_comment(comment) %}
                        <li>{{ comment }}</li>
                {% endmacro %}

                <ul>
                        {% for comment in comments %}
                                {{ render_comment(comment) }}
                        {% endfor %}
                </ul>

Le macro per renderle più usabili si possono importare in altro codice e richiamare.

##### Include

Serve per importare porzioni di template da un template ad un altro per riutilizzarlo o estenderlo.

Esempio:

                {% include 'index.html' %}

##### Blocchi

Altro modo molto pratico per portarsi dietro porzioni di codice da riutilizzare.

Esempio:

        <body>
                {% block content %}

                {% endblock %}
        </body>

##### Extends

Estende un intero template:

        {%  extends 'base.html' %}

### Integrazione di Bootstrap dentro i Flask Templates

Web Framewrok open source di Twitter. Framewrok client side. Si può importare Boostrap in Flask come libreria nella forma tradizionale, richiamandola nel file HTML, però Flask dà la possibliità di installarlo direttamente dentro il progetto in questo modo:

                pip install flask-bootstrap

                pip freeze > requirements.txt

E poi richiamandolo nell'app del progetto:

                from flask_bootstrap import Bootstrap

                bootstrap=Bootstrap(app)

per poterlo inizializzare.

### Pagine degli errori customizzate

Per definire pagine degli errori in Flask dobbiamo servirci del decorator **errorhandler**.

Esempio di definizione di una pagina 404:

                @app.errorhandler(404)
                def page_not_found(e):
                        return render_template("404.html"), 404
