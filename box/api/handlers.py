from flask import (
    jsonify,
    make_response
)


def override_handlers(app):
    '''
    Override handlers to return JSON message
    '''

    @app.errorhandler(404)
    def not_found(error):
        '''
        Override default Not Found response
        '''

        return make_response(jsonify({'error': 'Not found'}), 404)
