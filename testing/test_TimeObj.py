import sys

sys.path.append( '../timeline')

from timeline.Timeline import TimeObject

def test_minimal():
    to = TimeObject( '2024-12-12', '2023-12-12', 'task 1' )
    assert 1 == 1
