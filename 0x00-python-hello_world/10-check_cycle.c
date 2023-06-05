#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *list_slow = list;
	listint_t *list_fast = list;

	if (!list)
		return (0);

	while (list_slow && list_fast && list_fast->next)
	{
		list_slow = list_slow->next;
		list_fast = list_fast->next->next;
		if (list_slow == list_fast)
			return (1);
	}

	return (0);
}

