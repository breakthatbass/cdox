import sys
import pathlib
import os.path

'''
add @param and @global KEYWORDS
'''

class Doc:

    KEYWORDS = {
        'PARAM_LINE' : '@param:',           # func params
        'DESC_LINE' : '@desc:',             # func description
        'RETURN_LINE' : '@return:',         # func returns
        'NAME_LINE' : '@name:',             # API doc name
        'API_DESC_LINE' : '@description:'   # API doc description
    }

    RETURN_BOLD_MD = '- **returns**'
    END_LINE = '\n#\n'
    SECTION_SEPR_MD = '\n<br>\n\n'
    FUNC_START = '```C\n'
    FUNC_END = '\n```\n'
    DOC_END = ' * */\n'

    def __init__(self, infile, outfile):
        self.infile = infile        # file to create the doc for
        self.outfile = outfile      # the doc file to be created
        
        self.name = ''
        self.description = ''
        self.info_list = []  # should end up being something like [@desc, @param, @param, @return]
        self.func_name = ''

        # make sure files are usuable for the program
        error_check(self.infile, self.outfile)


    def handle_keyword_line(self, line):
        '''
            handle a line containing a cdox keyword, parse it as necessary,
            and either return it or write it to the markdown file.
            
            params: line
                line - the line from the file that contains a cdox keyword
            
            returns:
                None if the line does not contain a keyword
                otherwise it defines the global class variables
        '''
        index = line.find(':')+2
        doc_line = line[index:]

        if self.KEYWORDS['NAME_LINE'] in line:
            self.name = f'# {doc_line.strip()} documentation\n'

        elif self.KEYWORDS['API_DESC_LINE'] in line:
            self.description = f'{doc_line} {self.END_LINE}'

        # bullet points
        elif self.KEYWORDS['RETURN_LINE'] in line:
            self.info_list.append(f'{self.RETURN_BOLD_MD} {doc_line}')

        elif self.KEYWORDS['PARAM_LINE'] in line:
            self.info_list.append(f'- {doc_line}')

        elif self.KEYWORDS['DESC_LINE'] in line:
            self.info_list.append(f'{doc_line}')

        else:
            return None



    def get_func_name(self, line):
        '''
            parses a line containing a function parameter 
            and returns it ready to be written to the doc
            
            param: line
                a line from the file being read from - expects a function in the line
            
            returns:
                a formatted code string to be written to the markdown doc
        '''
        # chars that might be in the func line that we don't want
        junk = ['{', ';']
        for jank in junk:
            if jank in line:
                line = line.replace(jank, '')

        return f'{self.FUNC_START}{line.strip()} {self.FUNC_END}'



    def write_name_desc(self, doc):
        '''
            writes the objects @name and @description varibles to the top
            of the markdown doc. then erases them...which maybe isn't necessary.

            param: doc
                the markdown file being written to

        '''
        doc.write(self.name)
        doc.write(self.description)
        self.name = ''
        self.description = ''



    def doc_write(self, doc):
        '''
            write all the info pertaining to a funtion to the markdown doc
            then erase the global variables to be used for another function.

            param: doc
                the markdown file being written to
        '''
        doc.write(self.func_name)
        for el in self.info_list:
            doc.write(el)
        doc.write(self.SECTION_SEPR_MD)
        self.info_list.clear()
        self.func_name = ''
            

   
    def parse_file(self):
        '''
            parse the file, open the mrkdown file, and parse the necessary lines
            and write the documentation
        '''
        # file we're writing to, at this point, we're sure it'll open
        doc = open(self.outfile, 'w')

        with open(self.infile, 'r') as cfile:
            prev = ''
            line = cfile.readline()
            while line != '':
                if self.name != '' and self.description != '':
                    self.write_name_desc(doc)
                # check if line contains any of the string constants above
                if any(keyword in line for keyword in self.KEYWORDS.values()):
                    self.handle_keyword_line(line)
                elif prev == self.DOC_END:
                    # we're at the function prototype/name
                    self.func_name = self.get_func_name(line)
                    # if we've got the function name, we write to the doc
                    self.doc_write(doc)
                prev = line
                line = cfile.readline()
        doc.close()
            

def error_check(infile, outfile):
    '''
        check that infile and outfile have specific file extentions

        params: infile, outfile
            infile - the file to be read from and create the doc for
            outfile - the markdown documentation file to write

        returns:
            1: infile does not have the right file extension
            2: outfile is not a markdown file
            0: both files are usable
    '''
    ok_files = ['.c', '.h']
    # check file extensions
    in_ext = pathlib.Path(infile).suffix
    out_ext = pathlib.Path(outfile).suffix

    assert (in_ext in ok_files), f'ERROR: {infile} is not a valid file'
    assert (out_ext == '.md'), f'ERROR: outfile must be markdown format'
    assert (os.path.exists(infile)), f'ERROR: {infile} not found'




def main():

    if len(sys.argv) != 3:
        print('usage: cdox infile outfile')
        sys.exit(1)

    d = Doc(sys.argv[1], sys.argv[2])
    d.parse_file()

if __name__ == '__main__':
    main()
