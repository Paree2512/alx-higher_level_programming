#include "lists.h"

/**
 * check_cycle - check if there is a cycle in a linked list
 * @list: pointer to the head of the linked list
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	if (!list)
		return (0);

	listint_t *fast_ptr = list;
	listint_t *slow_ptr = list;

	while (fast_ptr && fast_ptr->next)
	{
		fast_ptr = fast_ptr->next->next;
		slow_ptr = slow_ptr->next;

		if (fast_ptr == slow_ptr)
			return (1);
	}

	return (0);
}
