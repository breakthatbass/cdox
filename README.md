# cdox

A script to automate documentation of your C APIs in markdown format.  

`cdox` reads in a source code file creates documentation based on the comments. it's sort of like doxygen but simpler and creates a markdown file.  

## Usage
```
cdox infile outfile
```

## Installation
```
pip install cdox
```

## Rules 

**cdox keywords:**
- `@name:` name of documentation.
- `@description:` description of file documentation.
- `@desc:` a description of a function.
- `@param:` a bullet point for info on a function paramter.
- `@return:` a bullet point for what the function returns.

**rules:**
- the keywords must be in multiline comments. 
- the multiline comments must start with `/* *` and end with `* */` each on their own line.
- the function name/protoype must be on the line following the `* */`


## Example Usage
Check out [`example.md`](https://github.com/breakthatbass/cdox/blob/main/example.md) for what the below example would produce.
#
```C
// test.c

/* *
 * strncmp
 * 
 * @desc: compare two strings up to `n` characters.
 * 
 * @param: `s1` - a char array of at least one char.
 * @param: `s2` - a char array of at least one char.
 * @param: `n` - the number of chars to compare of each string.
 * 
 * @return: 0 if strings are the same else a non-zero int.
 * */
int strncmp(const char *s1, const char *s2, int n)
{
  while(n > 0 && *s1 == *s2++) {
    if(*s1++ == '\0')
      return 0;
    n--;
  }
  return (n == 0 ? 0 : *s1 - *--s2);
}
```

## todo
- add feature to allow making section headers
- add @global keyword for documentation of global variables