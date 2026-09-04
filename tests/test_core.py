from debugforge.core import levels

def test_levels():
    assert levels(["INFO: ok", "error: bad", "INFO: next"]) == {"debug": 0, "info": 2, "warning": 0, "error": 1}
