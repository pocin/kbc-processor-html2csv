import pytest
import logging
from main import main

def test_main_executes(caplog):
    with caplog.at_level(logging.INFO):
        main()
    assert "Hello World" in caplog.text
