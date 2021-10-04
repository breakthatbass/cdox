
/******************************************************************************
*
*   Author: Taylor Gamache
*   Email: gamache.taylor@gmail.com
*
*   @name: my test file
*   @description: a small library to push and pop some functions and see how the doc program works
*
******************************************************************************/


class Test {
	private Node head = null;
	private int size = 0;

	private class Node {
		Item item;
		Node next = null;
	}

/* *
 * push:
 *
 * @info: adds `int_to_push` to front of list
 * @info: somre more info.
 *
 * @returns: 0 if `malloc` fails, else 1.
 * */
	public void push(Item item) {
		Node tmp = head;

		head = new Node();
		head.item = item;
		head.next = tmp;

		size++;
	}


/* *
 * append:
 *
 * @info: adds `int_to_append` at end of list.
 *
 * @returns: 0 if `malloc` fails, else 1.
 * */
	public Item pop() {
		if (isEmpty())
			return null;

		Node tmp = head;
		head = head.next;
		size--;

		return tmp.item;
	}
}
