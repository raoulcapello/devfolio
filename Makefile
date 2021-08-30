# The 'dev' environment spins up the following containers:
# - postgres
# - docs
# So no Django App container - if you want that, use 'local' (see below)
dev-build:
	docker-compose -f dev.yml build

# Note the dev-run command spins up the 'postgres' and 'docs' containers,
# but you still need to install python packages with:
#
# pip install requirements/local.txt
#
# And run Django's development web server with:
#
# python manage.py runserver_plus
#
dev-run:
	docker-compose -f dev.yml up -d --remove-orphans

dev-status:
	docker-compose -f dev.yml ps

dev-logtail:
	docker-compose -f dev.yml logs -f

dev-stop:
	docker-compose -f dev.yml stop

dev-restart:
	docker-compose -f dev.yml restart

dev-destroy:
	docker-compose -f dev.yml down

# The 'local' environment spins up the following containers:
# - django
# - postgres
# - docs
local-build:
	docker-compose -f local.yml build

local-run:
	docker-compose -f local.yml up -d --remove-orphans

local-status:
	docker-compose -f local.yml ps

local-logtail:
	docker-compose -f local.yml logs -f

local-stop:
	docker-compose -f local.yml stop

local-restart:
	docker-compose -f local.yml restart

local-destroy:
	docker-compose -f local.yml down

### CI/CD pipelines

## Heroku

# Staging

# This will build and run the configured Heroku staging app
heroku-staging-deploy:
	git push heroku main:main

heroku-staging-logtail:
	heroku logs -a devfolio-staging --tail

# Production

# This will promote the staging app to production
heroku-production-deploy:
	heroku pipelines:promote -a devfolio-staging

heroku-production-logtail:
	heroku logs -a devfolio-prod --tail

heroku-production-restart:
	heroku dyno:restart -a devfolio-prod
