import platform

def obter_dispositivos_conectados():
    dispositivos = []

    # Obter informações do sistema operacional
    sistema_operacional = platform.system()

    if sistema_operacional == 'Linux':
        dispositivos = obter_dispositivos_linux()
    elif sistema_operacional == 'Windows':
        dispositivos = obter_dispositivos_windows()

    return dispositivos

def obter_dispositivos_linux():
    import pyudev
    dispositivos = []

    context = pyudev.Context()
    for device in context.list_devices(subsystem='usb'):
        if device.device_type == 'usb_device':
            dispositivos.append({
                'nome': device.get('ID_MODEL', 'Desconhecido'),
                'fabricante': device.get('ID_VENDOR', 'Desconhecido'),
                'tipo': 'USB',
                'status': 'ativo',
                'logs': []
            })

    return dispositivos

def obter_dispositivos_windows():
    import pythoncom
    import wmi

    dispositivos = []

    try:
        # Inicializar a COM library
        pythoncom.CoInitialize()

        c = wmi.WMI()
        for usb in c.Win32_PnPEntity():
            if usb.Name and 'USB' in usb.Name:
                dispositivos.append({
                    'nome': usb.Name,
                    'fabricante': usb.Manufacturer if usb.Manufacturer else 'Desconhecido',
                    'tipo': 'USB',
                    'status': 'ativo',
                    'logs': []
                })
    except Exception as e:
        print(f"Erro ao obter dispositivos USB: {e}")
    finally:
        # Liberar a COM library
        pythoncom.CoUninitialize()

    return dispositivos

def obter_status_dispositivos(dispositivos):
    for dispositivo in dispositivos:
        dispositivo['status'] = 'ativo'  # Implementação simplificada
    return dispositivos
