#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *current, *aux;

    current = list;
    if (current == NULL)
        return(0);
    aux = list->next;
    while (aux != NULL && aux->next != NULL && aux->next->next)
    {
        if (aux == current)
            return (1);
        current = current->next;
        aux = aux->next->next;
    }

    return (0);
}