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
'''  
def test_class_init_pass():
    n = Doc(TEST_PASS, 'o.md')
    m = n.read_into_list()
    assert m is not None
    assert m[1] == '*\n'
'''

# dont read from file for lines to use
# just use strings instead to test on the functions
# makes the tests clearer and also makes it easier to add new keywords into test
b = Doc(TEST_PASS, 'o.md')
@pytest.mark.parametrize('test_input, expected', [
    ('this line has no kwywords', None),
    ('*   @name: mylib', '# mylib documentation\n'),
    ('@description: a test api for the cdox program\n', 'a test api for the cdox program\n'),
    ('* @junk: this should return None\n', None),
    # will add this keyword later ('* @global: describe a global varible like this.\n', 'describe a global varible like this.\n'),
    ('@desc: compare two strings up to `n` characters.\n', 'compare two strings up to `n` characters.\n'),
    ('** @param: `s1` a char array of at least one char.\n', '- `s1` a char array of at least one char.\n'),
    ('   @return: 0 if strings are the same else a non-zero int.\n', '**returns** - 0 if strings are the same else a non-zero int.\n')
])
def test_handle_keyword(test_input, expected):
    b.handle_keyword_line(test_input) == expected
    


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

    #assert size == 892
    
# def test_clean_up(): 
#    rc = subprocess.call('rm o.md', shell=True)
