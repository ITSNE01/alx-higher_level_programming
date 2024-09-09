#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list) /* check if list is empty */
		return (0);

	/* traverse the list with both pointers */
	while (slow && fast && fast->next)
	{
		slow = slow->next; /* one step */
		fast = fast->next->next; /* two steps */
		if (slow == fast)
			/* slow meets fast forming a cycle */
			return (1);
	}

	return (0);
}
