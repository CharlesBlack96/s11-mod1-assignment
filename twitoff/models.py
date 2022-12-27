from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()

class User(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    username = DB.column(DB.String)
    #tweets = []

class Tweet(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True, nullable=False)
    text = DB.column(DB.Unicode(300))
    #creating a relationship between users and tweets
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    #create a whole list of tweets to be attatched to the user
    user = DB.relationship('User', backref=DB.backref('tweets'), lazy=True)



