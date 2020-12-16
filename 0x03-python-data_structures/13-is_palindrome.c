#include "lists.h"

/**
 * list_len - returns the size of a list
 *
 * @h: header of the singly linked list
 *
 * Return: number of nodes
 */

int list_len(listint_t *h)
{
	int i = 0;
	listint_t *current = h;

	while (current != NULL)
	{
		i++;
		current = current->next;
	}
	return (i);
}

/**
 * is_palindrome - checks if a s linked list is a palindrome
 * @head: head of the list
 * Return: 1 if palindrome 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *tail;
	int size = 0, i = 0, j = size;

	if (!*head)
		return (0);
	size = list_len(*head);
	if (size == 1)
		return (1);
	size--;
	current = *head;
	tail = *head;
	for (i = 0; i < (size / 2) + 1; i++)
	{
		tail = current;
		for (j = i; j < (size - i); j++)
			tail = tail->next;
		if (current->n != tail->n)
			return (0);
		current = current->next;
	}
	return (1);
}
