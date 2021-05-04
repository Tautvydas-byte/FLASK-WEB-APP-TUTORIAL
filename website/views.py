from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])  # /home
@login_required  # cannot go to home page without login
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    # user=current_user check if this is autheticated
    return render_template("home.html", user=current_user)

# take request.data which is String, which is send from index.js noteID = noteId


@views.route('/delete-note', methods=['POST'])
def delete_note():
    # turn to python dictionary object, take some data from POST request which loaded as JSON dictionary
    note = json.loads(request.data)
    noteId = note['noteId']  # then access the note Id attribute
    note = Note.query.get(noteId)  # look for the note wchich has that Id
    if note:  # check if exist
        if note.user_id == current_user.id:  # if user owned this note
            db.session.delete(note)  # then delete the note
            db.session.commit()

    # return empty response as json object(nothing return, but need to return something because requirement )
    return jsonify({})
