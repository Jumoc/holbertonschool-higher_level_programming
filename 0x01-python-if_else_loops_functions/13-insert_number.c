#include "lists.h"

/**
 * insert_node - inserts a node in order
 * @head: head of the list
 * @number: value of the node
 * Return: added node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	current = *head;
	if (current->n > number)
	{
		newNode->next = current;
		*head = newNode;
		return (*head);
	}

	while (current->next != NULL)
	{
		if (current->next->n > number)
		{
			newNode->next = current->next;
			current->next = newNode;
			return (newNode);
		}
		current = current->next;
	}
	current->next = newNode;
	return (newNode);
}
