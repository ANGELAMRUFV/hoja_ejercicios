def categoria_envio(peso):
    if peso<=1:
        return "sobre"
    elif peso<=5:
        return "paquete pequeño"
    elif peso<=20:
        return "paquete grande"
    else:
        return "voluminoso"
print(categoria_envio(3))