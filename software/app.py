from importlib.metadata import metadata
from flask import Flask , request, render_template, Response
from tempfile import mkdtemp

import re
from apps.production import create_metadata
from apps.validation import validate_metadata
import json
from time import strftime, gmtime
import pandas as pd

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
    validation_result = validate_metadata(metadata_object)

    if validation_result == True:
        return generate_resultpage(metadata_object)
    else:
        return render_template('invalidpage.html', errors=validation_result, metadata_string=json.dumps(metadata_object, indent=4))

@app.route("/download_json", methods=["POST"])
def download_json():
    metadata_string = request.form.get('metadatastring')

    timestamp = strftime("%Y%m%d-%H%M", gmtime())
    filename = f"export_{timestamp}.json"

    return Response(metadata_string, 
            mimetype='application/json',
            headers={'Content-Disposition':f'attachment;filename={filename}'})

def generate_resultpage(metadata_object):

    doc_table = pd.DataFrame(metadata_object['documents']).to_html(border=0, classes="table table-striped")
    metadata_string = json.dumps(metadata_object, indent=4)

    return render_template('validpage.html', metadata=metadata_object, 
                                             table=doc_table, 
                                             metadata_string=metadata_string)