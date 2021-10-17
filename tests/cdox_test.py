import pytest
from cdox.cdox import Doc
from pathlib import Path
import subprocess


TEST_FAIL = 'test.txt'      # file exists but should fail upon reading
TEST_PASS = 'test.h'        # file exists and should pass upon reading
TEST_NO_EXIST = 'no_file!'  # file doesn't exist and should fail upon readin    g


def test_class_init_fail():
    with pytest.raises(SystemExit):
        n = Doc(TEST_FAIL, 'o.md')
        o = Doc(TEST_NO_EXIST, 'o.md')
        p = Doc(TEST_PASS, 'o.txt')    # test that the non .md outfile fails

        assert n.name == ''
        assert n.description == ''
    
def test_class_init_pass():
    n = Doc(TEST_PASS, 'o.md')
    m = n.read_into_list()
    assert m is not None
    assert m[1] == '*\n'


def test_handle_keyword():
    n = Doc(TEST_PASS, 'o.md')
    n_list = n.read_into_list()
    n.handle_keyword_line(n_list[9])     # @name line
    n.handle_keyword_line(n_list[10])    # description line
    # info lines
    n.handle_keyword_line(n_list[21])
    n.handle_keyword_line(n_list[22])
    # return line
    n.handle_keyword_line(n_list[24])
    
    assert n.handle_keyword_line(n_list[0]) == None
    assert n.name == '# a test doc documentation\n'
    assert n.description == 'a small lib with string functions\n \n#\n'
    # info lines
    assert n.info_list[0] == '- copy `s` into `dst` until `t` is encountered.\n'
    assert n.info_list[1] == '- if `t` is never encountered, entirety of `s` gets copied.\n'
    assert n.info_list[2] == '- **returns** pointer to the start of `dst` or `NULL` is `s` is NULL.\n'


def test_get_func_name():
    n = Doc(TEST_PASS, 'o.md')
    func_name_test1 = 'char *cpy_until(char *dst, char *s, const char t);\n'
    func_name_test2 = 'String JavaMethod(String[] args, int number) {\n'
 
    md_test1 = n.get_func_name(func_name_test1)
    md_test2 = n.get_func_name(func_name_test2)

    assert md_test1 == '```C\nchar *cpy_until(char *dst, char *s, const char t) \n```\n'
    assert md_test2 == '```C\nString JavaMethod(String[] args, int number) \n```\n'


def test_create_doc():
    '''
        best way i can think to test the writing functions is to create a doc
        and then test the size
    '''
    doc = Doc(TEST_PASS, 'o.md')
    doc.parse_file()

    fp = Path('o.md').stat()
    size = fp.st_size

    assert size == 892
    
def test_clean_up(): 
    rc = subprocess.call('rm o.md', shell=True)
