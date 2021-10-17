/******************************************************************************
*
*   Author: Taylor Gamache
*   Email: gamache.taylor@gmail.com
*
*   Version: 0.1.2
*
*   License: MIT 2020
*
*   @name: a test doc
*   @description: a small lib with string functions
*
******************************************************************************/

#ifndef STRLIB_H__
#define STRLIB_H__


/* *
 * cpy_until:
 *
 * @info: copy `s` into `dst` until `t` is encountered.
 * @info: if `t` is never encountered, entirety of `s` gets copied.
 *
 * @returns: pointer to the start of `dst` or `NULL` is `s` is NULL.
 * */
char *cpy_until(char *dst, char *s, const char t);


enum config { FIRST = 1, ALL = 2 };
/* *
 * replace:
 * 
 * @info: replaces `orig` with `repl` in `s`.
 * @info: config can be `FIRST` or `ALL`.
 * @info: `FIRST`: replace the first instance of `orig` with `repl`.
 * @info: `ALL`: replace all instances of `orig` with `repl`.
 *
 * @returns: a potiner to `s`. if not `FIRST` or `ALL` is supplied of config, or `orig` is not in `s`, pointer to `s` is returned
 * */
char *replace(char *s, const char orig, const char repl, int config);


#endif
