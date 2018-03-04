init:
		pip install -r requirements.txt

test:
	docker build -t diehard_test .
	docker run diehard_test python2.7 -m pytest
	docker run diehard_test python3.4 -m pytest
	docker run diehard_test python3.5 -m pytest
	docker run diehard_test python3.6 -m pytest
