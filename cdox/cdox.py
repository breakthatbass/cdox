import sys
import pathlib

'''
add @param and @global keywords
'''

class Doc:

    keywords = {
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

    # hold the data from @name and @description here for access
    name = ''
    description = ''
    info_list = []  # should end up being something like [@desc, @param, @param, @return]
    func_name = ''
    
    def __init__(self, infile, outfile):
        self.infile = infile        # file to create the doc for
        self.outfile = outfile      # the doc file to be created

        # make sure files are usuable for the program
        if error_check(self.infile, self.outfile) != 0:
            sys.exit(1)



    def read_into_list(self):
        '''
            read a file into a line with each element as a file line
            
            param: infile
                expects a src code file that handles comments with '/*' & '*/', not '#'
            
            return:
                list holding file contents
        '''
        try:
            fp = open(self.infile, 'r')
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            return None
        
        infile_list = fp.readlines()
        fp.close()
        return infile_list



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

        if self.keywords['NAME_LINE'] in line:
            self.name = f'# {doc_line.strip()} documentation\n'

        elif self.keywords['API_DESC_LINE'] in line:
            self.description = f'{doc_line} {self.END_LINE}'

        # bullet points
        elif self.keywords['RETURN_LINE'] in line:
            self.info_list.append(f'{self.RETURN_BOLD_MD} {doc_line}')

        elif self.keywords['PARAM_LINE'] in line:
            self.info_list.append(f'- {doc_line}')

        elif self.keywords['DESC_LINE'] in line:
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
        cfile = self.read_into_list()
        # doc = self._open_md_file()
        with open(self.outfile, 'w') as doc:
        
            count = 0
            for line in cfile:

                if self.name != '' and self.description != '':
                    self.write_name_desc(doc)

                # check if line contains any of the string constants above
                if any(keyword in line for keyword in list(self.keywords.values())):
                    self.handle_keyword_line(line)

                elif cfile[count-1] == self.DOC_END:
                    # we're at the function prototype/name
                    self.func_name = self.get_func_name(line)
                    # if we've got the function name, we write to the doc
                    self.doc_write(doc)
                count += 1
            

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

    if in_ext not in ok_files:
        print(f'ERROR: {infile} is not a valid file')
        return 1

    if out_ext != '.md':
        print(f'ERROR: outfile must be markdown format')
        return 2
    return 0



def main():

    if len(sys.argv) != 3:
        print('usage: cdox infile outfile')
        sys.exit(1)

    d = Doc(sys.argv[1], sys.argv[2])
    d.parse_file()

if __name__ == '__main__':
    main()
