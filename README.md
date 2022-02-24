# faker_companies

[![Build Status](https://travis-ci.org/VentesWorks/faker_companies.svg?branch=master)](https://travis-ci.org/VentesWorks/faker_companies)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

companies API for UI development. Check out the project's [documentation](http://VentesWorks.github.io/faker_companies/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Local Development

```
docker run --name postgres-db -e POSTGRES_PASSWORD=abc123 -e POSTGRES_USER=django -e POSTGRES_DB=djangodb -p 5432:5432 -d postgres
python manage.py runserver
```

# Deployment

run on dokku instance

```
dokku apps:create faker-companies

dokku postgres:create djangodb
dokku postgres:link djangodb faker-companies
```

run on local machine

```
git remote add dokku dokku@dokku-dev:faker-companies
git push dokku master
```

run on dokku instance (SSL)

```
dokku config:set --no-restart faker-companies DOKKU_LETSENCRYPT_EMAIL=jeff@leadbook.com
dokku letsencrypt:enable faker-companies
dokku letsencrypt:list
dokku letsencrypt:cron-job --add
sudo crontab -l -u dokku
```
