from flask import Flask ,request
from serv import content
from serv import get_something

app=Flask(__name__)
app.register_blueprint(content.content)
app.register_blueprint(get_something.gs)

if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)