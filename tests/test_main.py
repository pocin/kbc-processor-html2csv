import pytest
import logging
from main import main, _build_outpath_from_inpath, _parse_table, find_all_files

import os
from pathlib import Path

THIS_FILE = os.path.dirname(os.path.abspath(__file__))

def test_building_outpaths():
    tests = [
        ('/data/in/files/something.xls', '/data/out/files/something.csv'), 
        ('/data/in/files/nested/deeply/something.else.html', '/data/out/files/nested/deeply/something.else.csv')
    ]
    for inpath, expected in tests:
        assert _build_outpath_from_inpath(inpath) == expected

def test_finding_files(request):
    files = set(find_all_files(THIS_FILE.rstrip('/')+ '/data'))
    def pj(fname):
        return os.path.join(THIS_FILE, 'data/in/files', fname)
    assert pj('Transaction_Report.2018-03-06.xls') in files
    assert pj('firstlevel/something.txt') in files
    assert pj('need/togo/deeper.csv') in files


def test_parsing_html():
    inpath = os.path.join(THIS_FILE,  'data/in/files/Transaction_Report.2018-03-06.xls')
    df = _parse_table(inpath)


    assert len(df.columns) > 1
    assert len(df) > 10
