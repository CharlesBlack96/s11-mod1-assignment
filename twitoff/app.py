from flask import Flask, render_template
from .models import DB, User, Tweet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

DB.init_app(app)

def create_app():
        
    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title="Home", users=users)

    @app.route('/reset')
    def reset():
        #reseting the batabase
        DB.drop_all()
        DB.create_all()

        #create some fake tweets and users 
        ryan = User(id=1, username='ryan')
        julian = User(id=2, username='julian')

        tweet1 = Tweet(id=1, text='this is ryans tweet', user=ryan)
        tweet2 = Tweet(id=2, text='this is julians tweet', user=julian)

        DB.session.add(ryan)
        DB.session.add(julian)
        DB.session.add(tweet1)
        DB.session.add(tweet2)

        DB.session.commit()

        return render_template('base.html', title='reset')

    return app
