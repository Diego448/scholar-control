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
        'required': True
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

course_schema = {
    'name': {
        'type': 'string',
        'required': True
    },
    'teacher': {
        'type': 'string',
        'required': True
    },
    'teacher_name': {
        'type': 'string'
    },
    'students':{
        'type': 'list',
        'default': []
    },
    'start': {
        'type': 'datetime',
        'required': False
    },
    'end': {
        'type': 'datetime',
        'required': False
    },
    'cost': {
        'type': 'float',
        'required': False
    },
    'status': {
        'type': 'string',
        'allowed': ['Programado', 'Iniciado', 'Terminado', 'Cancelado']
    }
}

teacher_schema = {
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
    'students_number': {
        'type': 'integer',
        'required': False
    },
    'phone_number': {
        'type': 'string',
        'minlength': 10,
        'maxlength': 10
    },
    'status': {
        'type': 'string',
        'allowed': ['Disponible', 'No disponible']
    }
}

payment_schema = {
    'course': {
        'type': 'string', 
        'minlength': 3,
        'required': True
    },
    'course_name': {
        'type': 'string'
    },
    'student': {
        'type': 'string', 
        'minlength': 3,
        'required': True
    },
    'student_name': {
        'type': 'string'
    },
    'amount': {
        'type': 'float',
        'required': True
    },
    'payment_date': {
        'type': 'datetime',
        'required': True
    },
    'status': {
        'type': 'string',
        'allowed': ['Pagado', 'No Pagado']
    }
}

students = {
    'item_title': 'student',
    'schema': student_schema
}

courses = {
    'item_title': 'course',
    'schema': course_schema,
    'query_objectid_as_string': True,
    'additional_lookup': {
        'url': 'regex("[0-9a-f]+")',
        'field': 'teacher'
    }
}

teachers = {
    'item_title': 'teacher',
    'schema': teacher_schema
}

payments = {
    'item_title': 'payment',
    'query_objectid_as_string': True,
    'schema': payment_schema,
    'additional_lookup': {
        'url': 'regex("[0-9a-f]+")',
        'field': 'student'
    }
}

DOMAIN = {
    'students': students,
    'courses': courses,
    'payments': payments,
    'teachers': teachers
}