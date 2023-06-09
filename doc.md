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

### Links con url_for

**url_for** funzione helper di Flask che viene messa a disposizione per gestire e generare in maniera dinamica gli url delle applicazioni tramite le informazioni memorizzate nella mappa degli url.

Gli url si possono generare con url_for() passando le parti dinamiche come parole chiave come argomenti.

Esempio:

                url_for('user', name=john, page=2, version=1)

                /user/john?page=2&version=1

### static

Percorso speciale per url assoluti, un posto dove risiedono le risorse statiche di una applicazione Flask, come i file css, javascript ecc...

Esempio:

                href = {{ url_for('static', filename='favicon.ico') }}

### Flask Moment (basato su Moment js)

Come includere la libreria Moment.js in Flask:

                pip install flask-moment

                pip freeze > requirements.txt

Nel progetto **app.py** includere il seguente codice:

                from flask_moment import Moment

                moment=Moment(app)

Includere nel template base.html:

                {% block scripts %}
                        {{super()}}
                        {{moment.include_moment()}}
                {% endblock %}

Valorizzare correttamente la rotta in cui usare le funzione di Moment:

                from datetime import datetime

                @app.route("/favicon")
                def favicon():
                        return render_template("favicon.html", current_time=datetime.utcnow())

Far arrivare il valore dentro la vista HTML usando le seguenti funzioni trmite Jinja2:

                <div class="page-header">
                        <h1>Hello, world</h1>
                        <p>The Local date time is: {{ moment(current_time).format('LLL') }}</p>
                        <p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>
                </div>


## Flask Forms

Flask WTF forms è un'estensione pensata per le form html in Flask.

Esempio:

        pip install flask-wtf

Permette l'installazione del modulo flask wtf, però questo modulo necessita di **una srecret key** per poter funzionare e non 
si inizializza normalmente come tutti gli altri moduli, la secret key serve per motivi di sicurezza in merito ad attacchi 
CSRF sui form. Ogni flask form si rappresenta in una Classe Python, che eredita FlaskForm.

Esempio:

        from flask_wtf import FlaskForm
        from wtforms import StringField, SubmitField
        from wtforms.validators import DataRequired


        app.config['SECRET_KEY']='38d0776e0970b72f85140f2ca6f2d5'


        # definizione di una classe per il form
        class NameForm(FlaskForm):
                name = StringField('What is you name?', validators=[DataRequired()])
                submit = SubmitField('Submit')

        # rotta con un form
        @app.route("/form_esempio", methods=['GET', 'POST'])
        def form_esempio():
                name = None
                form = NameForm()
                if form.validate_on_submit():
                        name = form.name.data
                        form.name.data = ''
                return render_template("pagina_con_form.html", form=form, name=name)

Esempio (pagina con form html):

        {% extends "bootstrap/base.html" %}

        {% block title %}Esempio di form con Flask{% endblock %}

        {% block content %}
        <form method="POST">
                {{ form.hidden_tag() }}
                {{ form.name.label }} {{ form.name() }}
                {{ form.submit() }}
        </form>
        {% endblock %}

#### Spiegazione dei flask form

##### Hidden Tag

                {{ form.hidden_tag() }}

Questo codice definisce un campo del form addizionale che è nascosto e viene usato da Flask WTF per una protezione contro CSRF, all'interno del form inserisce automaticamente un codice HTML di questo tipo:

                <input id="csrf_token" name="csrf_token" type="hidden" value="IjIwMWJhNDA0MjQxOWE4MzczNmIzNzc2Yjk2NTYxNzY3YzZkY2Y4YjUi.ZGnYwQ.GS1_mSvjyEMpUAMzaLgK4hFtmqQ">

###### Elementi del form

                {{ form.name.label }} {{ form.name(id='my-text-field') }}
                {{ form.submit() }}

Questo codice definisce i campi per il pulsante submit del form e una etichetta con il campo per l'inserimento del testo chiamato **name**.
Notare come posso fare il rendering nel form degli attributi (esempio **id**) HTML di un form poi da passare al CSS.
Inoltre va ricordato che esiste per i form una estensione aggiuntiva Bootstrap per poter lavorare al meglio con i form:

Esempio:

                {% import "bootstrap/wtf.html" as wtf %}

                {{ wtf.quick_form(form) }}

L'inserimento di queste parti di codice dentro il template HTML permettono la definizione di vari helpers Bootstrap per lo stile che vengono includi direttamente da Flask.

#### Un esempio completo di Flask Form renderizzato

1) Classe per il form:

                class NuovaForm(FlaskForm):
                        first_name = StringField('First name:', validators=[DataRequired()])
                        last_name = StringField('Last name:', validators=[DataRequired()])
                        submit = SubmitField('Ok')

La classe deve ereditare sempre FlaskForm!

2) Rotta

                @app.route("/form_esempio_2", methods=['GET', 'POST'])
                def form_esempio_2():
                        first_name = None
                        last_name = None
                        nuova_form = NuovaForm()
                        if nuova_form.validate_on_submit():
                                first_name = nuova_form.first_name.data
                                last_name = nuova_form.last_name.data
                                nuova_form.first_name.data = ''
                                nuova_form.last_name.data = ''
                return render_template("pagina_con_form2.html", form=nuova_form, first_name=first_name, last_name=last_name)

All'avvio sulla pagina la form compare non compilata e vuota, resettata. Notare come la rotta è in grado di accettare sia il metodo GET che il metodo POST.

3) Template HTML:

                {% extends "bootstrap/base.html" %}

                {% import "bootstrap/wtf.html" as wtf %}

                {{ wtf.quick_form(form) }}

                {% block page_content %}

                <div class="page-header">
                        <h1>Hello, {% if first_name and last_name %} {{ first_name }} {{ last_name }} {% else %} Stranger {% endif %}</h1>
                </div>


                <form method="POST">
                        {{ form.hidden_tag() }}
                        {{ form.first_name.label }} {{ form.first_name() }}
                        {{ form.last_name.label }} {{ form.last_name() }}
                        {{ form.submit() }}
                </form>
    
                {% endblock %}
