import sys
try:
    from cdox import Doc
except ImportError:
    from cdox.cdox import Doc


def main():

    if len(sys.argv) != 3:
        print('usage: cdox infile outfile')
        sys.exit(1)

    d = Doc(sys.argv[1], sys.argv[2])
    d.parse_file()

if __name__ == '__main__':
    main()