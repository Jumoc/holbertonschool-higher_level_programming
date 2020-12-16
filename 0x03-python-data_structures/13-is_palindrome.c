#include "lists.h"

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
	current = *head;
	tail = *head;
	while (tail->next)
	{
		tail = tail->next;
		size++;
	}
	for (i = 0; i < (size / 2) + 1; i++)
	{
		tail = *head;
		for (j = 0; j < (size - i); j++)
		{
			tail = tail->next;
		}
		if (current->n != tail->n)
			return (0);
		current = current->next;
	}
	return (1);
}
