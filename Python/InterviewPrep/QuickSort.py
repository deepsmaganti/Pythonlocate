def quicksort_recursive(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = quicksort([x for x in array[1:] if x < pivot])
        right = quicksort([x for x in array[1:] if x >= pivot])
        return left + [pivot] + right


void quicksort_non_recursive(int *array, int left, int right)
{
    int stack[1024];
    int i=0;

    stack[i++] = left;
    stack[i++] = right;

    while (i > 0)
    {
        right = stack[--i];
        left = stack[--i];

        if (left >= right)
             continue;

        int index = partition(array, left, right);
        stack[i++] = left;
        stack[i++] = index - 1;
        stack[i++] = index + 1;
        stack[i++] = right;
    }
}