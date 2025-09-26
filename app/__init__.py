from flask import Flask
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'minha_chave_secreta'

    # Configuração para envio via Outlook
    app.config['MAIL_SERVER'] = 'smtp.office365.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'weslleysantana2oo2@outlook.com'
    app.config['MAIL_PASSWORD'] = 'dvbnpsmtrsjewuhd'  # sua senha de app
    app.config['MAIL_DEFAULT_SENDER'] = 'weslleysantana2oo2@outlook.com'

    mail.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app

