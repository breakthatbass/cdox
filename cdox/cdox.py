import sys

IN_DOCS = False
IN_FUNC = False

def read_infile_into_list(infile):
    '''attempt to open the infile and outfile. if opened, return them'''
    try:
        cf = open(infile, 'r')
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        sys.exit()

    infile_list = cf.readlines()
    cf.close()
    return infile_list


def parse(file, outfile):
    '''takes a list (file as list) parses it line by line, and writes to the makrdown file'''

    # make sure `file` is a list
    if not isinstance(file, list):
        print('error: def parse() requires file as list form')
        sys.exit()

    infos = []
    returns = ''
    prototype = ''
    new_func = '\n<br>\n\n'

    global IN_DOCS
    global IN_FUNC

    with open(outfile, 'w') as doc:
        for line in file:
            if IN_DOCS == True:
                if ' * @info: ' in line:
                    info = line.replace(' * @info: ', '', 1)
                    infos.append(info)
                elif ' * @returns:' in line:
                    info = line.replace(' * @returns: ', '', 1)
                    returns = info
                    IN_DOCS = False
            elif IN_FUNC == True:
                    prototype = "```C\n" + line + "```\n"
                    doc.write(prototype)
                    for poo in infos:
                        doc.write('- ' + poo)
                    doc.write('- **returns** ' + returns)
                    doc.write(new_func)
                    infos.clear()
                    IN_FUNC = False
                    
            elif line == '/* *\n':
                IN_DOCS = True

            elif line == ' * */\n':
                IN_FUNC = True

            elif '@name:' in line:
                title = '# ' + line.split(':')[1].lstrip().strip() + ' documentation\n'
                doc.write(title)
            elif '@description:' in line:
                desc = line.split(':')[1].lstrip().strip()
                doc.write(desc + '  \n#\n')
            else:
                continue


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