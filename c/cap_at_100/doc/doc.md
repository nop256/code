/*
 * Write 2 functions, one of which calls the other.
 *
 * The first function should check whether the number pointed to by 'elt' is greater than 100.
 * If it is, cap it at 100 (i.e., set it to 100), and return 1 to indicate it was modified.
 * If it's already 100 or less, do nothing and return 0.
 *
 * Prototype: int cap_at_100(int *elt);
 *
 * The second function should loop through the 'len' elements in lst,
 * call the helper function on each one, and return the number of modifications made.
 *
 * Prototype: int normalize_array(int *lst, int len);
 *
 * In main, define an array with several numbers (some >100),
 * call normalize_array on it, print the modified array and the number of changes.
 */

