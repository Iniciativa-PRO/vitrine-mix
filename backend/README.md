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
- Após isso, o sistema estará disponível em `http://localhost:8000/`
- Rotas que exigem autenticação devem ser acessadas com o token `CSRF` gerado no login. Para isso, é necessário enviar o token no header da requisição com a chave `X-CSRFToken`.

## Rotas
- As rotas para o sistema estão disponíveis no arquivo [vitrine/urls.py](vitrine/urls.py)
- `http://localhost:8000/vitrine` - Rota para a API do sistema
- Rotas de autenticação:
  - `http://localhost:8000/vitrine/login` - Rota para login
  - `http://localhost:8000/vitrine/logout` - Rota para logout
  - `http://localhost:8000/vitrine/register` - Rota para cadastro de usuário
  - `http://localhost:8000/vitrine/delete` - Rota para deletar usuário
- Rotas para Vitrines:
  - `http://localhost:8000/vitrine/storefronts` - Rota para listar vitrines `(GET)` e criar vitrines `(POST)`
  - `http://localhost:8000/vitrine/storefronts/<id>` - Rota para exibir uma vitrine `(GET)`, atualizar uma vitrine `(PUT)`, atualizar parcialmente uma vitrine `(PATCH)` e deletar uma vitrine `(DELETE)`
- Rotas para serviços:
  - `http://localhost:8000/vitrine/storefronts/<id_vitrine>/services` - Rota para listar serviços de uma vitrine `(GET)` e criar serviços `(POST)`
  - `http://localhost:8000/vitrine/storefronts/<id_vitrine>/services/<id_servico>` - Rota para exibir um serviço `(GET)`, atualizar um serviço `(PUT)`, atualizar parcialmente um serviço `(PATCH)` e deletar um serviço `(DELETE)`