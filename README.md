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
- Compoilar arquivos estáticos e iniciar o servidor local:
    ```bash
    poetry run python manage.py collectstatic 
    poetry run python manage.py runserver
    ```

## Documentação
- Atualizar o schema:
    ```bash
    poetry run python manage.py spectacular --file schema.yml
    ```
- Acesse a referência da API em `/docs`
