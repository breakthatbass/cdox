/******************************************************************************
*
*   Author: Taylor Gamache
*   Email: gamache.taylor@gmail.com
*
*   @name: mylib
*   @description: a test api for the cdox program
*
******************************************************************************/

#include "mylib.h"

/* *
* @global: describe a global varible like this...@global keyword in the workds...
* */
int global_int = 100;


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
