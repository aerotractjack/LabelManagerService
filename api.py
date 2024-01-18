import sys
from flask import Flask, request, jsonify
from flask_executor import Executor
from flasgger import Swagger

from docs import swag_gen_aois, swag_ref_aois_points, template

from LabelManager.aoi_gen import gen_aois
from LabelManager.aoi_georef import georef_aois

app = Flask(__name__)
swagger = Swagger(app, template=template)

executor = Executor(app)

@app.route("/gen_aois", methods=["GET", "POST"])
@swag_gen_aois
def gen_aois_route():
    '''
    Trigger the generation of training and validation AOIs for an image
    '''
    contents = request.get_json()
    data = {
        "gsd": .24,
        "train_n": 7,
        "train_height": 75,
        "train_width": 75,
        "val_height": 24.1,
        "val_width": 24.1,
        "val_rowbuf": 15,
        "val_colbuf": 15,
        "val_overlap_min": .1
    }
    data.update(contents)
    try:
        executor.submit(gen_aois, **{k.lower(): v for k,v in data.items()})
        return jsonify("submitted aoi generated")
    except Exception as e:
        print(e)
        sys.stdout.flush()
        return jsonify({"error": str(e)}), 500
    
@app.route("/ref_aois_points", methods=["GET", "POST"])
@swag_ref_aois_points
def ref_aois_points():
    '''
    Trigger the post-processing (georeferencing+moving to NAS) of data for
    a labeled stand
    '''
    contents = request.get_json()
    try:
        executor.submit(georef_aois, **{k.lower(): v for k,v in contents.items()})
        return jsonify("submitted label georef")
    except Exception as e:
        print(e)
        sys.stdout.flush()
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":
    from waitress import serve
    serve(app, port=7112, host="0.0.0.0")