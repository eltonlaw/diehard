# pylint: disable=missing-docstring
# pylint: disable=unused-variable
import sys

def test_import_root():
    import diehard
    assert 'diehard' in sys.modules
