informacion_usuario = {
    'id': '',
    'rol': ''
}


def set_informacion_usuario(id, rol):
    informacion_usuario['id'] = id
    informacion_usuario['rol'] = rol


def get_id_usuario():
    return informacion_usuario['id']


def get_rol_usuario():
    return informacion_usuario['rol']
