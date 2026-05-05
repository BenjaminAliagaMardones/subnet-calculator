def limpiar_ip(ip:str):
    ip = ip.strip()
    octetos = ip.split(".")

    if octetos != 4:
        raise ValueError(f"Direccion IP Invalida, La Direccion Debe Tener 4 octetos")
    

    octetos_limpios = []
    for octeto in octetos:
        if not octeto.isdigit():
            pass