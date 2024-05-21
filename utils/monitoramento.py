import platform

dispositivos_logs = {}
dispositivos_anteriores = {}
dispositivos_inativos = {}

def obter_dispositivos_conectados():
    dispositivos = []
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
            nome = device.get('ID_MODEL', 'Desconhecido')
            fabricante = device.get('ID_VENDOR', 'Desconhecido')
            tipo_usb = device.get('ID_USB_DRIVER', 'usb2')  # Padrão para simplificação
            frequencia = obter_frequencia_dispositivo(tipo_usb)
            dispositivos.append({
                'nome': nome,
                'fabricante': fabricante,
                'tipo': tipo_usb,
                'status': 'ativo',
                'frequencia': frequencia,
                'logs': dispositivos_logs.get(nome, [])
            })
    return dispositivos

def obter_dispositivos_windows():
    import pythoncom
    import wmi
    dispositivos = []
    try:
        pythoncom.CoInitialize()
        c = wmi.WMI()
        for usb in c.Win32_PnPEntity():
            if usb.Name and 'USB' in usb.Name:
                nome = usb.Name
                fabricante = usb.Manufacturer if usb.Manufacturer else 'Desconhecido'
                tipo_usb = determinar_tipo_usb_windows(usb)
                frequencia = obter_frequencia_dispositivo(tipo_usb)
                dispositivos.append({
                    'nome': nome,
                    'fabricante': fabricante,
                    'tipo': tipo_usb,
                    'status': 'ativo',
                    'frequencia': frequencia,
                    'logs': dispositivos_logs.get(nome, [])
                })
    except Exception as e:
        print(f"Erro ao obter dispositivos USB: {e}")
    finally:
        # Liberar a COM library
        pythoncom.CoUninitialize()
    return dispositivos

def obter_status_dispositivos(dispositivos):
    global dispositivos_logs
    global dispositivos_anteriores
    global dispositivos_inativos

    dispositivos_atuais = {d['nome']: d for d in dispositivos}
    novos_dispositivos_logs = dispositivos_logs.copy()

    for nome, dispositivo in dispositivos_anteriores.items():
        if nome not in dispositivos_atuais:
            dispositivo['status'] = 'inativo'
            dispositivo['logs'].append('Desconectado')
            dispositivos_inativos[nome] = dispositivo
            novos_dispositivos_logs[nome] = dispositivo['logs']

    for dispositivo in dispositivos:
        if dispositivo['status'] == 'ativo':
            if dispositivo['nome'] in novos_dispositivos_logs:
                dispositivo['logs'] = novos_dispositivos_logs[dispositivo['nome']]
        else:
            if dispositivo['nome'] not in novos_dispositivos_logs:
                novos_dispositivos_logs[dispositivo['nome']] = []
            novos_dispositivos_logs[dispositivo['nome']].append('Desconectado')

    dispositivos_logs = novos_dispositivos_logs
    dispositivos_anteriores = dispositivos_atuais

    return dispositivos

def obter_frequencia_dispositivo(tipo_usb):
    frequencias = {
        'usb2': '480 Mbps',
        'usb3': '5 Gbps',
        'usb3.1': '10 Gbps',
        'usb3.2': '20 Gbps'
    }
    return frequencias.get(tipo_usb.lower(), 'Desconhecida')

def determinar_tipo_usb_windows(usb):
    if '3.0' in usb.Name:
        return 'usb3'
    elif '3.1' in usb.Name:
        return 'usb3.1'
    elif '3.2' in usb.Name:
        return 'usb3.2'
    else:
        return 'usb2'
