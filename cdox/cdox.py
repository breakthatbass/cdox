import sys

from argparse import ArgumentParser

IN_DOCS = False
IN_FUNC = False

def open_files(infile, outfile):
    # create markdown file
    try:
        doc = open(outfile, 'a')
    except:
        print('error: unable to open ' + outfile)
        return
    
    
    try:
        cf = open(infile, 'r')
    except:
        print('error: unable to create ' + infile)
        return
    
    in_file = cf.readlines()

    return doc, in_file


def parse(files):
    infos = []
    returns = ''
    prototype = ''
    new_func = '\n<br>\n\n'

    global IN_DOCS
    global IN_FUNC

    doc = files[0]
    hfile = files[1]

    for line in hfile:
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
            # we're in an a func doc
            IN_DOCS = True

        elif line == ' * */\n':
            # we're done with docs
            # next is a function prototype
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
        sys.exit(1)

    infile = sys.argv[1]
    outfile = sys.argv[2]
    
    # assuming we have the infile and outfile
    fps = open_files(infile, outfile)

    parse(fps)

    #fps[0].close()
    #fps[1].close()

if __name__ == '__main__':
    main()