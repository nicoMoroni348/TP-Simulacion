def validar_parametros_simulacion(i, j, x):

    try:
        i = int(i)
        j = float(j)
        x = float(x)
    except ValueError:
        return False
    
    if j > x or j < 0 or x < 0 or i < 1 or i > 100000:
        return False

    return i, j, x


def validar_demora(demora_min, demora_max):

    try:
        demora_min = float(demora_min)
        demora_max = float(demora_max)
    except ValueError:
        return False
    
    if demora_min < 0 or demora_max < 0 or demora_max < demora_min:
        return False

    return demora_min, demora_max


def validar_float_positivo(value):

    try:
        value = float(value)
    except ValueError:
        return False
    
    if value < 0:
        return False

    return value


def validar_media_desviacion(media, desviacion):

    try:
        media = float(media)
        desviacion = float(desviacion)
    except ValueError:
        return False
    
    if media < 0 or desviacion < 0 or desviacion > media:
        return False

    return media, desviacion