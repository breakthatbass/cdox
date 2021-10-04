import sys

keywords = {
        'INFO_LINE' : '@info:',
        'RETURNS_LINE' : '@returns',
        'NAME_LINE' : '@name',
        'DESC_LINE' : '@description'
    }

RETURN_BOLD_MD = '- **returns**'
END_LINE = '\n#\n'
SECTION_SEPR_MD = '\n<br>\n\n'
FUNC_START = '```C\n'
FUNC_END = '\n```\n'
DOC_END = ' * */\n'


def read_infile_into_list(infile):
    '''
        read a file into a line with each element as a file line

        param: infile
            expects a src code file that handles comments with '/*' & '*/', not '#'

        return:
            list holding file contents
    '''
    try:
        cf = open(infile, 'r')
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        sys.exit()

    infile_list = cf.readlines()
    cf.close()
    return infile_list



def handle_keyword_line(line, doc):
    '''
        handle a line containing a cdox keyword, parse it as necessary,
        and either return it or write it to the markdown file.

        params: line, doc
            line - the line from the file that contains a cdox keyword
            doc - the markdown file we're attempting to write to

        returns:
            if keyword is '@name' or @description', write to doc
            else return the parsed line 
    '''

    index = line.find(':')+2
    doc_line =  line[index:]

    if keywords['NAME_LINE'] in line:
        doc.write(f'# {doc_line.strip()} documentation\n')
    elif keywords['DESC_LINE'] in line:
        doc.write(f'{doc_line} {END_LINE}')
    elif keywords['RETURNS_LINE'] in line:
        return f'{RETURN_BOLD_MD} {doc_line}'
    else:
        return f'- {doc_line}'
    return


def append_func_docs(func_line, bullets, doc):
    '''
        write a function name and its bullet points to the markdown doc

        params:
            func_line - the line containing the function name
            bullets - list containing all the info for that function
            doc - the markdown file we're attempting to write to
    '''

    # chars that might be in the func line that we don't want
    junk = ['{', ';']

    for jank in junk:
        if jank in func_line:
            func_line = func_line.replace(jank, '')

    doc.write(f'{FUNC_START}{func_line.strip()} {FUNC_END}')
    
    for bullet in bullets:
        if bullet: # just make sure bullet element is not None
            doc.write(bullet)
    doc.write(SECTION_SEPR_MD)

    

def parse(infile, outfile):
    '''
        parse each line of infile and write what we need to outfile

        params:
            infile - the file we're reading from containing line by line in a list
            outfile - the markdown file we're attempting to wrtie to
    '''
    bullet_points_md = []
    count = 0

    try:
        doc = open(outfile, 'w')
    except:
        print(f'problem creating {outfile}')
        sys.exit()

    for line in infile:
        # check if line contains any of the string constants above
        if any(keyword in line for keyword in list(keywords.values())):
            # we have a line with documentation, handle it
            bullet_points_md.append(handle_keyword_line(line, doc))
        
        # if the prev line was end a doc section, current line is a function name
        elif infile[count-1] == DOC_END:
            append_func_docs(line, bullet_points_md, doc)
            bullet_points_md.clear()
        count+=1
    doc.close()



def main():    
    if len(sys.argv) != 3:
        print('usage: cdox infile outfile')
        sys.exit()

    infile = sys.argv[1]
    outfile = sys.argv[2]
    
    infile_list = read_infile_into_list(infile)

    parse(infile_list, outfile)
   

if __name__ == '__main__':
    main()
