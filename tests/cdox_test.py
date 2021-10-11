import pytest
import os

from cdox.cdox import read_infile_into_list, handle_keyword_line, append_func_docs


def test_read_infile():
    infile = read_infile_into_list('tests/tfiles/test.txt')
    assert infile[0] == 'this is a test file\n'
    assert infile[1] == 'for the read_infile_into_list\n'
    assert infile[2] == 'function.\n'


def test_read_infile_failure():
    with pytest.raises(SystemExit):
        read_infile_into_list('no_file!')

doc = open('test.md', 'w')
@pytest.mark.parametrize('test_input, expected', [
    ('this line has no kwywords', None),
    ('* @returns: a pointer to a string\n', '**returns** a pointer to a string\n'),
    ('@info: this is an info line\n', 'this is an info line\n'),
    ('* @junk: this should return None\n', None)
])
def test_keyword_line(test_input, expected):
    handle_keyword_line(test_input, doc) == expected

doc.close()
os.remove('test.md')
