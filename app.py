import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

@app.route('/')
def app_root():
    return "Flask app on Heroku!"

if __name__ == "__main__":
    app.run(debug=True)
