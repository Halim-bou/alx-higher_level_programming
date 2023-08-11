#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - function that insert a node in order in
 * singly linked list
 * @head: apointer to pointer to the first node
 * @number: the number to insert in the new node
 * Return: the address of the new node or NULL if it fieled
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *curr_ptr;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	curr_ptr = *head;
	while (curr_ptr && curr_ptr->next->n < number)
		curr_ptr = curr_ptr->next;
	new_node->next = curr_ptr->next;
	curr_ptr->next = new_node;

	return (new_node);
}
