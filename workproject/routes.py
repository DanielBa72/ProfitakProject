from flask import render_template, request
from workproject import app
from workproject import db
from workproject.models import User, Comment
import requests
import uuid

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user_form')
def add_user_form():
    return render_template('add_user_form.html')

@app.route('/add_user_submitted', methods=['POST'])
def add_user_submitted():
    userName = request.form['name']
    date_of_birth = request.form['date_of_birth']
    user = User(str(uuid.uuid4()), userName, date_of_birth)
    db.session.add(user)
    db.session.commit()
    return render_template('general_submit.html', 
        string_val='You successfully added a user.')


@app.route(('/edit_user_form/<id>'))
def edit_user_form(id):
    user = User.query.get_or_404(id)
    return render_template('edit_user_form.html', user=user)



@app.route('/edit_user_submitted/<id>', methods=['POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    user.name = request.form['name']
    user.date_of_birth = request.form['date_of_birth']

    db.session.commit()
    return render_template('general_submit.html', 
        string_val='You successfully edited a user.')


@app.route('/user_list')
def user_list():
    all_users = User.query.all()
    if not all_users:
        return 'You have not added a user yet.'
    return render_template('view_users.html', all_users=all_users)

@app.route('/search_user_form')
def search_user_form():
    return render_template('search_user_form.html')

@app.route('/search_user_submitted', methods=['POST'])
def search_user_submitted():
    user = User.query.filter_by(name=request.form['name']).all()
    if not user:
        return "User not found" 
    return render_template('view_users.html', all_users=user)

@app.route('/delete_user_form/<id>')
def delete_user_form(id):
    user_to_delete = User.query.get_or_404(id)

    comments_to_delete = Comment.query.filter_by(user_id=user_to_delete.id).all()
    for comment in comments_to_delete:
        db.session.delete(comment)

    db.session.delete(user_to_delete)
    db.session.commit()
    return render_template('general_submit.html', 
        string_val='You successfully deleted a user and all of his comments.')

@app.route('/add_comment_form/<id>')
def add_comment_form(id):
    return render_template('add_comment_form.html', id=id)

@app.route('/add_comment_submitted/<id>', methods=['POST'])
def add_comment_submitted(id):
    comment = Comment(str(uuid.uuid4()), request.form['comment_body'], id)
    db.session.add(comment)
    db.session.commit()
    return render_template('general_submit.html', 
        string_val='You successfully added a comment.')

@app.route('/view_all_comments')
def view_all_comments():
    comments = Comment.query.all()
    if not comments:
        return 'You have not added any comments yet.'
    return render_template('view_comments.html', comments=comments)


@app.route('/delete_comment_form/<id>')
def delete_comment_form(id):
    commentToDelete = Comment.query.get_or_404(id)
    db.session.delete(commentToDelete)
    db.session.commit()
    return render_template('general_submit.html', 
        string_val='You successfully deleted a comment.')


@app.route('/edit_comment_form/<id>')
def edit_comment_form(id):
    comment_to_edit = Comment.query.get_or_404(id)
    return render_template('edit_comment_form.html', comment_to_edit=comment_to_edit)

@app.route('/edit_comment_submitted/<id>', methods=['POST'])
def edit_comment_submitted(id):
    comment = Comment.query.get_or_404(id)
    comment.content = request.form['content']
    db.session.commit()
    return render_template('general_submit.html', 
        string_val='You successfully edited a comment.')

@app.route('/search_comment_form')
def search_comment_form():
    return render_template('search_comment_form.html')


@app.route('/search_comment_submitted', methods=['POST'])
def search_comment_submitted():
    comments = Comment.query.filter_by(content=request.form['content']).all()
    if not comments:
        return "No comments were found" 
    return render_template('view_comments.html', comments=comments)


@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    data = requests.get('https://zoo-animal-api.herokuapp.com/animals/rand')
    return ('<h1>Name:</h1> ' + data.json()['name'] + '<br><h1>Latin name:</h1> ' + data.json()['latin_name'])