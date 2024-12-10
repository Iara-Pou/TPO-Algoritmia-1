import datetime
import traceback


def setInformacionUsuario(id, rol):
    informacion_usuario['id'] = id
    informacion_usuario['rol'] = rol


def getIdUsuario():
    return informacion_usuario['id']


def getRolUsuario():
    return informacion_usuario['rol']


def loguearExcepcion(mensaje_customizado, mensaje_excepcion):
    """
    Registra excepciones en un archivo de log incluyendo:
    - La hora 
    - El nombre de la excepción
    - Un mensaje customizado
    - El stacktrace 

    Args:
        mensaje_customizado (str): Mensaje personalizado a registrar.
        mensaje_excepcion (Exception): La excepción capturada.
    """
    try:
        with open(ruta_log, 'a', encoding='utf-8') as archivo:
            hora_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            tipo_excepcion = type(mensaje_excepcion).__name__
            stacktrace = traceback.format_exc()

            archivo.write(f"[{hora_actual}] {mensaje_customizado}\n")
            archivo.write(f"Tipo de Excepción: {tipo_excepcion}\n")
            archivo.write(f"Mensaje de Excepción: {mensaje_excepcion}\n")
            archivo.write("Stacktrace:\n")
            archivo.write(f"{stacktrace}\n")
            archivo.write("-" * 80 + "\n")
    except Exception as e:
        # Si falla escritura de excepcion (es archivo)
        print(f"Error al loguear excepción: {e}")


def loguearError(mensaje_error):
    # Si hay un error de validación, guardarlo en un txt con la hora.
    try:
        with open(ruta_log, 'a', encoding='utf-8') as archivo:
            hora_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            archivo.write(f"[{hora_actual}] ERROR: {mensaje_error}\n")
    except Exception as e:
        print(f"Error al loguear error: {e}")


def loguearInformacionUsuario(id, rol, es_login, es_logout):
    # Si es login, guardar datos del usuario con un separador.
    # Si es logout, loguear cierre de sesión y un separador.
    try:
        with open(ruta_log, 'a', encoding='utf-8') as archivo:
            hora_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if es_login:
                archivo.write(
                    f"**********************************************************\n")
                archivo.write(f"[{hora_actual}] LOGIN:\n")
                archivo.write(f"ID Usuario: {id}\n")
                archivo.write(f"Rol Usuario: {rol}\n")
                archivo.write(
                    f"**********************************************************\n")

            if es_logout:
                archivo.write(
                    f"[{hora_actual}] LOGOUT: Sesión cerrada para el usuario ID {id}.\n")
                archivo.write(
                    f"----------------------------------------------------------\n")

    except Exception as e:
        print(f"Error al loguear información del usuario: {e}")


ruta_log = 'data/logEjecucion.txt'
informacion_usuario = {
    'id': '',
    'rol': ''
}
