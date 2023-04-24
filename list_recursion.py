class ListRecursion:
    def print_sentence(lst):
        if lst is None or lst == []:
            return
        if len(lst) == 1:
            print(lst[0] + '.')
            return
        else:
            print(lst[0] + ' ', end='')
            ListRecursion.print_sentence(lst[1:])

    def reverse(lst):
        if lst is None or lst == []:
            return lst
        rest_reversed = ListRecursion.reverse(lst[1:])
        return rest_reversed + [lst[0]]

    def remove_every_other(lst):
        if lst is None or lst == []:
            return lst
        if len(lst) == 1:
            return lst
        rest_removed = ListRecursion.remove_every_other(lst[2:])
        return [lst[0]] + rest_removed

    def maximum(lst):
        if lst is None or lst == []:
            return lst
        if len(lst) == 1:
            return lst[0]
        max_in_rest = ListRecursion.maximum(lst[1:])
        if lst[0] > max_in_rest:
            return lst[0]
        else:
            return max_in_rest

if __name__ == "__main__":
    ListRecursion.print_sentence(['The', 'quick', 'brown', 'fox'])
