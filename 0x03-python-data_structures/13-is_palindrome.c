#include "lists.h"
/**
 * is_palindrome - a function in C that checks if a singly linked list is a palindrome
 * @head: the head of a singly linked list
 * Retur: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return(1);
	return(_palind(head, *head));
}
/**
 * _palind - a function to know if palindrome
 * @head: the head of a singly linked list
 * @end: end list
 * Retur: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int _palind(listint_t **head, listint_t *end)
{
        if (end == NULL)
                return(1);
        if (_palind(head, end->next) && (*head)->n == end->n)
	{
	        *head = (*head)->next;
		return (1);
	}
	return (0);
}
