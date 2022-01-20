import os

class Config():
	SECRET_KEY = 'c878971d6db55bcac6c2a0b48948e690'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'mail@gmail.com'
	MAIL_PASSWORD = 'password'
	# The MAIL_USERNAME requires that you input the email that will prompt password reset
	# The MAIL_PASSWORD is of the MAIL_USERNAME