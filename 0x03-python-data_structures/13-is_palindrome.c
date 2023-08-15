#include "lists.h"
#include <stdlib.h>
listint_t *reverse(listint_t *head);
/**
 * reverse - reverse the linked list
 * @head: a pointer to the first node
 * Return: a pointer to the end of the list
 */
listint_t *reverse(listint_t *head)
{
	listint_t *prev, *current, *next;

	prev = NULL;
	current = head;
	next = NULL;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
/**
 * is_palindrome - function that check if the linked list is palindrome
 * @head: a pointer to pointer to the first node
 * Return: 1 if it's palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	listint_t *f_half, *second_half;

	slow = *head;
	fast = *head;
	second_half = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	if (fast != NULL)
		slow = slow->next;
	second_half = reverse(slow);
	f_half = *head;
	while (second_half != NULL)
	{
		if (f_half->n != second_half->n)
			return (0);
		f_half = f_half->next;
		second_half = second_half->next;
	}
	return (1);
}
