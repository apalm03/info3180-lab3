from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iloveformalmethods'
app.config['MAIL_SERVER']= 'smtp.mailtrap.io'
app.config['MAIL_PORT']=  '2525'
app.config['MAIL_USERNAME'] = '2121ef427b7b0e'
app.config['MAIL_PASSWORD'] = '34628590fdc253'

mail = Mail(app)
from app import views