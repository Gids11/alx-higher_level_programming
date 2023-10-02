#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: A pointer to the head of the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *a;
	listint_t *b;

	a = list;
	b = list;

	while(b != NULL && a->next != NULL && a->next->next != NULL)
	{
		a = a->next->next;
		b = b->next;

		if (a == b)
			return (1);
	}

	return (0);
}
