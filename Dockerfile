FROM ubuntu:16.04

RUN apt-get update && \
    apt-get -y install software-properties-common \
                       python-software-properties && \
    add-apt-repository -y ppa:deadsnakes/ppa && apt-get update && \
    apt-get autoclean

RUN apt-get -y install \
    python2.7 python2.7-dev \
    python3.4 python3.4-dev \
    python3.5 python3.5-dev \
    python3.6 python3.6-dev && \
    apt-get autoclean

RUN apt-get install wget && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python2.7 get-pip.py && \
    python3.4 get-pip.py && \
    python3.5 get-pip.py && \
    python3.6 get-pip.py && \
    rm get-pip.py

COPY ./requirements /diehard/requirements
RUN pip2.7 install -r /diehard/requirements/dev.txt && \
    pip3.4 install -r /diehard/requirements/dev.txt && \
    pip3.5 install -r /diehard/requirements/dev.txt && \
    pip3.6 install -r /diehard/requirements/dev.txt

COPY ./setup.py ./setup.cfg ./pytest.ini ./README.rst /diehard/
COPY ./docs /diehard/docs
COPY ./tests/ /diehard/tests
COPY ./diehard /diehard/diehard
WORKDIR /diehard
RUN pip2.7 install -e . && \
    pip3.4 install -e . && \
    pip3.5 install -e . && \
    pip3.6 install -e .

CMD ["python3.6", "-m", "pytest"]
