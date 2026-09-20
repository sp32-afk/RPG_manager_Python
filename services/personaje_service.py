def es_valido(nombre, clase, nivel) -> bool:
    if nombre is None or not nombre.strip():
        return False
    clasesPermitidas = ["Guerrero","Mago","Arquero"]
    if clase is None or clase.capitalize()not in clasesPermitidas:
        return False
    if nivel < 1 or nivel > 100:
        return False
    return True