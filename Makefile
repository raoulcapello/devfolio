# The 'dev' environment spins up the following containers:
# - postgres
# - docs
# So no Django App container - if you want that, use 'local' (see below)
dev-build:
	docker-compose -f dev.yml build

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
