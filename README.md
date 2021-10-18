# cdox

a script to automate documentation of your projects.  

## usage
```
cdox infile outfile
```

## installation
```
git clone https://github.com/breakthatbass/cdox.git
pip install .
```

## about
`cdox` reads in a source code file creates documentation based on the comments. it's like doxygen but simpler and just creates a markdown file which looks good on github.  

**cdox keywords:**
- `@name:` name of documentation
- `@description` description of documentation
- `@info:` a bullet point for info on a function
- `@returns:` a bullet point for what the function returns

**rules:**
- the keywords must be in multiline comments. 
- the multiline comments must start with `/* *` and end with `* */` each on their own line.
- the function name/protoype must be on the line following the `* */`

## TODO
- add it as a package to pypi
- add feature to allow making section headers
- add ability to handle a multi-line @descripton
- add @param keyword for function parameters
- add @global keyword for documentation of global variables
- add @class keyword for better docs for classes

## example
`test_prog.h`
#
```C
/******************************************************************************
*
*   Author: Taylor Gamache
*   Email: gamache.taylor@gmail.com
*
*   the name and description keywords are expected to be at a comment block
*   at the top of a file.
*
*   @name: my test file
*   @description: a test file to see how cdox works
*
******************************************************************************/

#ifndef TEST_PROG_H__
#define TEST_PROG_H__

/* *
 * push:
 * 
 * adding a line preceeding with the info keyword creates a bullet point for the markdown
 *
 * @info: adds `int_to_push` to front of list
 * @info: some more info.
 *
 * @returns: 0 if `malloc` fails, else 1.
 * */
int push(list_t *l, int int_to_push);


#endif
```

<br>

running `cdox test_prog.h test_prog.md` will create:

`test_prog.md`

---
<br>

# my test file documentation
a test file to see how cdox works
#
```C
int push(list_t *l, int int_to_push)
```
- adds `int_to_push` to front of list
- some more info.
- **returns** 0 if `malloc` fails, else 1.

---
