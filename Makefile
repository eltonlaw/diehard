test:
	docker pull eltonlaw/pybase
	docker build -t diehard .
	docker run diehard python2.7 -m pytest
	docker run diehard python3.4 -m pytest
	docker run diehard python3.5 -m pytest
	docker run diehard python3.6 -m pytest

deps:
	pip install -r requirements/base.txt
	pip install -r requirements/dev.txt

docker-pybase:
	docker build -t pybase -f Dockerfile.pybase .
	docker tag pybase eltonlaw/pybase
	docker push eltonlaw/pybase
