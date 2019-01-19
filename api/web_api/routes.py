from flask import request, jsonify
from api.services.history_service import HistoryService
from api.services.matching_process_service import MatchingProcessService
from api.web_api import app
import io
import jsonpickle

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


@app.route('/matchingProcess', methods=['POST'])
def run_matching_process():
    if 'file' not in request.files:
        return handle_exception("No file part", 400)
    else:
        file = request.files["file"]
        if file.filename == '':
            return handle_exception("No selected file", 400)
        if not allowed_file(file.filename):
            return handle_exception("Not supported file extension", 400)
        file_raw_bytes = file.read()
        image_file = io.BytesIO(file_raw_bytes)
    if 'photoDatabaseId' in request.form and is_int(request.form['photoDatabaseId']):
        photoDatabaseId = int(request.form['photoDatabaseId'])
    else:
        photoDatabaseId = 1

    matching_process_service = MatchingProcessService()
    matching_process_service.run_matching_process(image_file, photoDatabaseId)

    return jsonify({"message": "Temporary response"}), 200


@app.route('/recentMatches', methods=['GET'])
def get_recent_matches(n=1):
    temp = request.args.get('n')
    if is_int(temp):
        n = int(temp)

    history_service = HistoryService()
    recent_matches = history_service.get_recent_histories(n)

    response = app.response_class(
        response=jsonpickle.encode(recent_matches, make_refs=False, unpicklable=False),
        status=200,
        mimetype='application/json'
    )

    return response


def handle_exception(message, status_code):
    response = jsonify({'message': message})
    response.status_code = status_code
    return response


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def is_int(object):
    try:
        int(object)
        return True
    except:
        return False
