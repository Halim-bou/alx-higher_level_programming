#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - function that check if there is any cycle in the linked list
 * @list: The head pointer to the linked list
 * Return: 0 if there is no cycle or 1 if a cycle found
 */
int check_cycle(listint_t *list)
{
	listint_t *slower_ptr;
	listint_t *faster_ptr;

	if (!list || !list->next)
		return (0);
	slower_ptr = list;
	faster_ptr = list->next;
	while (faster_ptr && faster_ptr->next)
	{
		if (slower_ptr == faster_ptr)
			return (1);
		slower_ptr = slower_ptr->next;
		faster_ptr = faster_ptr->next->next;
	}
	return (0);
}
