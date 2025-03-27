/*
 * Write 2 functions, one of which calls the other.
 *
 * The first function should check whether the number pointed to by 'elt' is negative.
 * If it is negative, set it to 0, and return 1 (to indicate a change was made).
 * If it's not negative, leave it unchanged and return 0.
 *
 * Prototype: int zero_if_negative(int *elt);
 *
 * The second function should loop over the 'len' elements in lst,
 * and for each one, call the helper function.
 * It should return the total number of elements that were modified (i.e., changed from negative to zero).
 *
 * Prototype: int sanitize_array(int *lst, int len);
 *
 * Then, in main, define an array with some negative and positive integers,
 * call sanitize_array on it, and print both the modified array and the number of changes.
 */

