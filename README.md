# cdox

a script to automate documentation of your projects.  

## usage
```
cdox infile outfile
```

## installation
```
# clone repo then
pip install .
```

## how it works
cdox reads in a source code file and creates documentation in a markdown file.  
it should work with any programming language that uses `/*` and `*/` for multiline comments.  

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
- add feature to allow making section headers
- add ability to handle a multi-line @descripton

## example with correct formatting
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
*   @description: a small library to push and pop some functions and see how the doc program works
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
 * @info: somre more info.
 *
 * @returns: 0 if `malloc` fails, else 1.
 * */
int push(list_t *l, int int_to_push);


/* *
 * append:
 *
 * @info: adds `int_to_append` at end of list.
 *
 * @returns: 0 if `malloc` fails, else 1.
 * */
int append(list_t *l, int int_to_append);

#endif
```

<br>

running `cdox test_prog.h test_prog.md` will create:

`test_prog.md`

---
<br>

# my test file documentation
a small library to push and pop some functions and see how the doc program works  
#
```C
int push(list_t *l, int int_to_push);
```
- adds `int_to_push` to front of list
- somre more info.
- **returns** 0 if `malloc` fails, else 1.

<br>

```C
int append(list_t *l, int int_to_append);
```
- adds `int_to_append` at end of list.
- **returns** 0 if `malloc` fails, else 1.

<br>

---