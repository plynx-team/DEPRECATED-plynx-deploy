REPO=plynxteam
VERSION=$(shell . version.sh; getVersion)
BASENAME=$(shell basename $(CURDIR))


build:
	docker build --rm -t ${REPO}/${BASENAME}:${VERSION} . ;
	docker tag ${REPO}/${BASENAME}:${VERSION} ${REPO}/${BASENAME}:latest;

push:
	docker push ${REPO}/${BASENAME}:${VERSION}
	docker push ${REPO}/${BASENAME}:latest
