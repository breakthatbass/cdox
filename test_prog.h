/******************************************************************************
*
*   Author: Taylor Gamache
*   Email: gamache.taylor@gmail.com
*
*   Version: 0.1.2
*
*   License: MIT 2020
*
*   @name: my test file
*   @description: a small library to push and pop some functions and see how the doc program works
*
******************************************************************************/

#ifndef TEST_PROG_H__
#define TEST_PROG_H__

#include <stdlib.h>

struct node {
    int value;
    struct node *next;
};
typedef struct node node_t;

struct list {
    node_t *head;
    size_t nodes;
};
typedef struct list list_t;



/* *
 * push:
 *
 * @info: adds `int_to_push` to front of list
 *
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
