MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'scholar-control'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

student_schema = {
    'firstname': {
        'type': 'string', 
        'minlength': 3,
        'required': True
    },
    'lastname': {
        'type': 'string', 
        'minlength': 3,
        'required': True
    },
    'location': {
        'type': 'string',
        'required' = True
    },
    'phone_number': {
        'type': 'string',
        'minlength': 10,
        'maxlength': 10
    },
    'status': {
        'type': 'boolean'
    }
}

students = {
    'item_title': 'student',
    'schema': student_schema
}

DOMAIN = {
    'students': students
}