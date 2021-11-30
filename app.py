from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    with app.app_context():
        import routes
        app.run(debug=True)
