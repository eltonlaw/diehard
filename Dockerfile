FROM eltonlaw/pybase

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
