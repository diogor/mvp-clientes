# Api de Clientes
## Instalação
- Instalar o Poetry: https://python-poetry.org/
- Copiar o arquivo `.env.example` e criar o arquivo `.env`
    - Edite o `.env` de acordo com suas necessidades
- Instalar as dependências:
    ```bash
    poetry install
    ```
- Migrar o banco de dados:
    ```bash
    poetry run python manage.py migrate
    ```
- Iniciar o servidor local:
    ```bash
    poetry run python manage.py runserver
    ```

## Documentação
Acesse a referência da API em `/docs`
