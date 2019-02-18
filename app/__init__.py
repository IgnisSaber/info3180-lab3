from flask_mail import Mail
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'may the force be with you'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io' 
app.config['MAIL_PORT'] = '465' # (or try 2525) 
app.config['MAIL_USERNAME'] = 'username' 
app.config['MAIL_PASSWORD'] = 'password'

mail = Mail(app)
from app import views