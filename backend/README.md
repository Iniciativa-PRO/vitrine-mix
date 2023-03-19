# Sistema Backend do projeto Vitrine Mix

Sistema para catálogo de serviços para múltiplas lojas.

## Instalação
- O projeto foi criado utilizando Python 3.10.6, portanto é recomendado que seja utilizado a mesma versão.
- É recomendado usar um ambiente virtual para instalar as dependências.
- Para instalar as dependências, execute o comando `pip install -r requirements.txt`
- Para configurar a `SECRET_KEY` do projeto, renomeie o arquivo `.env.example` para `.env` e adicione a `SECRET_KEY` desejada.
  - Há como gerar uma `SECRET_KEY` utilizando o comando `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
  - Para facilitar, pode-se gerar uma chave no site [djecrety.ir](https://djecrety.ir/)
- Execute o comando `python manage.py migrate` para criar as tabelas no banco de dados.
## Execução
- Acesse a pasta `backend` e execute o comando `python manage.py runserver`