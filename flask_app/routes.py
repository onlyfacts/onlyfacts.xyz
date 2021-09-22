import json
from typing import Dict, List

from flask import flash, redirect, render_template, request
from flask.helpers import url_for

from flask_app.alerts import send
from flask_app.forms import ContactForm, FactForm
from flask_app import SEND, app


@app.route('/')
def index():
    with open('facts.json', 'r', encoding='utf-8') as f:
        sources: Dict[str, List[dict]] = json.load(f)
    return render_template('index.html', sources=sources)

@app.route('/home')
def home():
    print(request.remote_addr)
    return index()


@app.route('/about')
def about():
    return render_template('about.html', title='About | Fact Sheet')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    cform = ContactForm()

    if cform.validate_on_submit():
        # Save contact entry
        with open('contact.json', 'r', encoding='utf-8') as f:
            entry = {
                'name': cform.name.data,
                'email': cform.email.data,
                'message': cform.message.data,
                'ip': request.remote_addr
            }
            contact: list = json.load(f)
            contact.append(entry)

        with open('contact.json', 'w', encoding='utf-8') as f:
            json.dump(contact, f, indent=2)

        if SEND: send('CONTACT', entry)
        flash(f'Message sent! Thank you for your feedback!', 'success')
        return redirect(url_for('home'))

    return render_template('contact.html', form=cform, title='Contact | Fact Sheet')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    fform = FactForm()

    if fform.validate_on_submit():  # Check if form was submitted

        # Append submission in usable format
        with open('submissions.json', 'r', encoding='utf-8') as f:
            
            facts = [s.strip() for s in fform.facts.data.split('\n')]
            if len(facts) == 1: facts = facts[0]
            
            sources = [s.strip() for s in fform.sources.data.split('\n')]
            if len(sources) == 1: sources = sources[0]

            entry = {
                'name': fform.name.data,
                'email': fform.email.data,
                'fact': facts,
                'source': sources,
                'ip': request.remote_addr
            }

            submissions: list = json.load(f)
            submissions.append(entry)

        with open('submissions.json', 'w', encoding='utf-8') as f:
            json.dump(submissions, f, indent=2)

        flash(f'Fact submitted! Waiting for manual review.', 'success')
        if SEND: send('SUBMISSION', entry)
        return redirect(url_for('submit'))

    return render_template('submit.html', form=fform, title='Submit | Fact Sheet')
