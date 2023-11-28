#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!current || new->n < current->n)
	{
		new->next = current;
		return(*head = new);
	}
	while (current)
	{
		if (!current->next || new->n < current->next->n)

		{
			new->next = current->next;
			current->next = new;
			return (current);
		}
		current = current->next;
	}
	return (NULL);
}
