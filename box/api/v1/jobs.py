from flask import (
    abort,
    Blueprint,
    jsonify,
    make_response,
    request,
    url_for
)


jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/', methods=['GET'])
def get_jobs():
    return jsonify({'jobs': []})

@jobs_bp.route('/<string:job_id>', methods=['GET'])
def get_job(job_id):
    return jsonify({'jobs': []})

@jobs_bp.route('/', methods=['POST'])
def create_job():
    if not request.json or not 'title' in request.json:
        abort(400)
    job = {
        'id': 'some id',
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    return make_response(jsonify({'job': job}), 201)

def make_public_job(job):
    '''
    Remove Ids from object and replace with our built-in URI
    '''

    new_job = {}
    for field in job:
        if field == 'id':
            new_job['uri'] = url_for('get_job', job_id=job['id'], _external=True)
        else:
            new_job[field] = job[field]
    return new_job
