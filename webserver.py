

from flask import (
    Flask,
    render_template,
    request
)

from flask_restful import Resource, Api
import monitor



app = Flask(__name__, template_folder=".")
api = Api(app)
api.add_resource(monitor.Monitor, "/process")




@app.route('/')
def home_path():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)