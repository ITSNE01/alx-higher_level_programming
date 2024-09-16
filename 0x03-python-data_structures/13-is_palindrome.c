#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a singly linked list.
 * @head: Pointer to the head of the list.
 * Return: A pointer to the first node of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *next = NULL;

    while (head)
    {
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }

    return prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list.
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    listint_t *slow = *head, *fast = *head, *second_half, *prev_slow;
    listint_t *middle = NULL; // To handle odd-sized lists
    int result = 1;

    // Find the middle of the list
    while (fast && fast->next)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // Handle odd-sized lists
    if (fast != NULL)
    {
        middle = slow;
        slow = slow->next;
    }

    // Reverse the second half
    second_half = reverse_list(slow);
    prev_slow->next = NULL; // Terminate the first half

    // Compare both halves
    listint_t *first_half = *head, *second_half_copy = second_half;
    while (second_half)
    {
        if (first_half->n != second_half->n)
        {
            result = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    // Restore the second half (optional)
    second_half_copy = reverse_list(second_half_copy);
    if (middle)
    {
        prev_slow->next = middle;
        middle->next = second_half_copy;
    }
    else
    {
        prev_slow->next = second_half_copy;
    }

    return result;
}
