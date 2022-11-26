REPO=plynxteam
BASENAME=$(shell basename $(CURDIR))
export VERSION=$(shell . version.sh; getVersion)

DOCKER_COMPOSE_DEV_FILE = ./docker-compose-dev.yml

build:
	docker build --rm -t ${REPO}/${BASENAME}:${VERSION} . ;
	docker tag ${REPO}/${BASENAME}:${VERSION} ${REPO}/${BASENAME}:latest;

push:
	docker push ${REPO}/${BASENAME}:${VERSION}
	docker push ${REPO}/${BASENAME}:latest

dev:
	python -m webbrowser "http://localhost:3001/"
	docker-compose -f $(DOCKER_COMPOSE_DEV_FILE) up --abort-on-container-exit
