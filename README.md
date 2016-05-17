# Eventex

Sistema de Eventos curso WttD

[![Code Health](https://landscape.io/github/juniorcarvalho/Python-wttd/master/landscape.svg?style=flat)](https://landscape.io/github/juniorcarvalho/Python-wttd/master)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative um virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.


```
git clone git@github.com:juniorcarvalho/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer deploy?
1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o servico de email.
6. Envie o código para o heroku.

```
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gem.py'
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force
```