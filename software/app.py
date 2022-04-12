from flask import Flask , request, render_template, Response
from tempfile import mkdtemp

import re
from apps.production import create_metadata
import json

# Configure applicatioN
app = Flask(__name__)
app.config["SECRET_KEY"] = b'5\x95@j\xd7Z}\xd6\xfd\xafV\xfbU\xd6/\xf5'

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/", methods=["GET"])
def start():
    """ Main page """

    # Render start template
    return render_template("index.html")

@app.route("/create_json", methods=["POST"])
def create_json():
    """
    Retrieve form data, create and validate JSON
    """

    form_data = request.form
    files = request.files

    metadata_object = create_metadata(form_data, files)

    # Standard metadata
    metadata_string = json.dumps(metadata_object, indent=4)

    return render_template('json.html', test_thing=metadata_string)
    #return Response(metadata_string, 
    #        mimetype='application/json',
    #        headers={'Content-Disposition':'attachment;filename=test.json'})

