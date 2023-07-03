"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'imasecret123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

app.app_context().push()

connect_db(app)
db.create_all()






@app.route('/')
def homepage():
    """ Routes to the application homepage """

    return render_template('homepage.html')






@app.route('/user-list')
def shows_users():
    """ Routes to user list page """

    users = User.query.all()

    return render_template('users.html', users = users)






@app.route('/user-list', methods=['POST'])
def show_form():
    """ Routes to New User Form """

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    imageurl = request.form['imageurl']

    new_user = User(first_name = firstname, last_name = lastname, image_url = imageurl)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/user-list')






@app.route('/user/<int:user_id>')
def show_details(user_id):
    """ Routes to user details """


    user = User.query.get_or_404(user_id)


    return render_template('user-details.html', user = user)






@app.route('/user/<int:user_id>/edit')
def edit_user_details(user_id):
    """ Routes to a form to edit user details """



    user = User.query.get_or_404(user_id)


    return render_template('user-edit.html', user = user)






@app.route('/user/<int:user_id>/edit', methods=['POST'])
def submit_new_details(user_id):
    """ Routes to a form to edit user details """

    user = User.query.get_or_404(user_id)

    edit = user

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    imageurl = request.form['imageurl']

    edit = User(first_name = firstname, last_name = lastname, image_url = imageurl)

    db.session.add(edit)
    db.session.commit()


    return redirect('/user-list')




@app.route('/user/<int:user_id>/delete')
def delete_user(user_id):
    """ Deletes a selected user from the database """

    User.query.filter_by(id = user_id).delete()

    db.session.commit()

    return redirect('/user-list')




# Hugh = User(first_name = 'Hugh', last_name = 'Laurie', image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4fzGWkuFhylA04iWEdyNd6UFREV6R5_bQbQ&usqp=CAU')
# Dean = User(first_name = 'Dean', last_name = 'Winchester', image_url = 'https://upload.wikimedia.org/wikipedia/en/4/45/Jensen_Ackles_as_Dean_Winchester.png')
# Crowley = User(first_name = 'Crowley', last_name = 'MacLeod', image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcQKeT9pEr-YnVrBjGaYsXbc212vPfR8ph6Q&usqp=CAU')
# Burton = User(first_name = 'Burton', last_name = 'Guster', image_url = 'https://upload.wikimedia.org/wikipedia/en/7/70/Burton_Guster.jpg')
# Shawn = User(first_name = 'Shawn', last_name = 'Spencer', image_url = 'https://m.media-amazon.com/images/M/MV5BMTkyOTYzNTk4Ml5BMl5BanBnXkFtZTgwNDQ4NDY2MjE@._V1_.jpg')



