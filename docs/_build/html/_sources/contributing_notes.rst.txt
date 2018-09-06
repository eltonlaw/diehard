Developer Notes
=================

* Python 2.7, 3.4, 3.5 and 3.6 are installed in one Docker container to run tests.
* Dependencies are installed in a lower layer; `diehard/pybase`. If new packages are required, need to update `Dockerfile.pybase` and push changes to  Docker hub because Travis pulls from it to cut down on time running tests.
* Run tests with `make test`.
* `pytest` is the test suite used.
