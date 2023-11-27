#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *L1, *L2;

	if (!list || !list->next)
		return (0);

	L1 = list->next;
	L2 = list->next->next;
	while(L1 && L2 && L2->next)
	{
		if (L1 == L2)
			return (1);
		L1 = L2;
		L2 = L2->next->next;
	}
	return (0);
}
