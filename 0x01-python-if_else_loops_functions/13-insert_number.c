#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *num_new;

	num_new = malloc(sizeof(listint_t));
	if (num_new == NULL)
		return (NULL);
	num_new->n = number;

	if (node == NULL || node->n >= number)
	{
		num_new->next = node;
		*head = num_new;
		return (num_new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	num_new->next = node->next;
	node->next = num_new;

	return (num_new);
}
