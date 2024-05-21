## Gerenciamento de Dispositivos

### Desenvolvedor: Carlos César

---

### Descrição do Projeto

Aplicação básica para reconhecer quais dispositivos estão conectados no sistema operacional. A aplicação é compatível tanto com Windows quanto com Linux. Esta aplicação utiliza alguns plugins específicos para cada sistema operacional para funcionar corretamente.

### Requisitos

Para executar este projeto, você precisará dos seguintes plugins:

- Flask
- pyudev (apenas para Linux)
- pythoncom e wmi (apenas para Windows)

### Instalação

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/carloscesar/gerenciamento_dispositivos.git
   cd gerenciamento_dispositivos
   ```

2. **Crie e ative um ambiente virtual:**

   ```sh
   python -m venv .venv
   source .venv/bin/activate   # Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências:**

   ```sh
   pip install -r requirements.txt
   ```

### Executando a Aplicação

1. **Inicie a aplicação:**

   ```sh
   python app.py
   ```

2. **Acesse a aplicação no navegador:**

   Abra seu navegador e acesse `http://localhost:5000`.

### Funcionalidades

- **Página Inicial (`/`):** Exibe a página principal da aplicação.
- **Dispositivos Conectados (`/dispositivos`):** Exibe os dispositivos USB conectados ao sistema.
- **Status dos Dispositivos (`/status`):** Exibe o status dos dispositivos, incluindo aqueles que foram desconectados.

### API Endpoints

- **`/api/dispositivos`**: Retorna uma lista de dispositivos USB conectados.
- **`/api/status`**: Retorna o status dos dispositivos, incluindo aqueles que foram desconectados(Produção).

### Observações

- A aplicação realiza a verificação contínua dos dispositivos conectados a cada 10 segundos em uma thread separada.
- A implementação inclui funções específicas para obter dispositivos conectados tanto em sistemas Linux quanto Windows, utilizando bibliotecas apropriadas para cada plataforma.

### Contato

Para mais informações, entre em contato com Carlos César.

---
