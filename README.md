# cdox

a script to automate documentation of `c` projects.  

i made this super fast just to get a bunch of documentation automated and done quick. maybe i'll come back and make the code clean and proper when i get some time! in the meantime it's working well enough.

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
cdox reads in a `.h` or `.c` file and creates documentation in a markdown file.

**keywords:**
- `@name:` name of documentation
- `@description` description of documentation
- `@info:` a bullet point for a function
- `@returns:` what the function returns

**rules:**
- the keywords must be in multiline comments. 
- `cdox` pplaces them in a markdown file so markdown syntax can be used.  
- the multiline comments must start with `/* *` and end with `* */` each on their own line
- the function prototype must be on the line following the `* */`

## example with correct formatting
#
```C
/******************************************************************************
*
*   Author: Taylor Gamache
*   Email: gamache.taylor@gmail.com
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
#

### the above file will create this:
#
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

#