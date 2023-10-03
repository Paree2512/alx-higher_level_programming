#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly-linked list
 * @head: pointer to the head of the list
 * @number: number to insert
 *
 * Return: NULL if the function fails, otherwise, a pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current, *prev;

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	current = *head;
	prev = NULL;

	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}

	else
	{
		prev->next = new_node;
		new_node->next = current;
	}

	return (new_node);
}
