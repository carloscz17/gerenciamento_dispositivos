def verificar_alertas(status):
    alertas = []
    for dispositivo in status:
        if dispositivo['status'] == 'inativo':
            alertas.append(f"Alerta: O dispositivo {dispositivo['nome']} está inativo.")
    return alertas
