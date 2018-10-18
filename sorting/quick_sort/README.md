
# ALGORITHM 
    - Set pivot to the middle element in the data
    - For each element:
        - If current element is the pivot, continue
        - If the element is less than the pivot, add to left array
        - Else, add to right array
    - Recursively apply quicksort to the left array
    - Recursively apply quicksort to the right array
    - Merge the left array + pivot + right array

### Complexity:

    Time: O(n log(n)) average, best, O(n^2) worst
    Space: O(n)

#### Misc:

    More sophisticated implementations are in-place, although they still take up recursion depth space
    Most implementations are not stable


![Alt Text](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)