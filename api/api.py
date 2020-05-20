import flask
import service

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def demo():
    return "<h2>Use URL structure 'http://127.0.0.1:5000/profiles/user' to lookup user data</h2>"

@app.route('/profiles/<user>', methods=['GET'])
def getUserProfile(user=None):
    return service.getUserData(user)

app.run()