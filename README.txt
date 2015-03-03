----------------------------------------------------------------------------------------------------------------------------------------------------
Problem Statement

John Watson performs an operation called Right Circular Rotation on an integer array [a0, a1, ... an-1]. 
Right Circular Rotation transforms the array from [a0, a1, ... aN-1] to [aN-1, a0,... aN-2].

He performs the operation K times and tests Sherlock's ability to identify the element at a particular position in the array.
He asks Q queries. Each query consists of one integer, idx, for which you have to print the element at index idx in in the rotated array, i.e., a[idx].

(Solution:In C )(File: rotate.c)

-----------------------------------------------------------------------------------------------------------------------------------------------------
Shellsort

    Improves on insertion sort.
    Starts by comparing elements far apart, then elements less far apart,
    and finally comparing adjacent elements (effectively an insertion sort).
    By this stage the elements are sufficiently sorted that the running time
    of the final stage is much closer to O(N) than O(N2).

Shellsort, also known as the diminishing increment sort, is one of the oldest sorting algorithms, named after its inventor Donald. L. Shell (1959).
 It is fast, easy to understand and easy to implement. However, its complexity analysis is a little more sophisticated. 

(File:Shellsort.c)

-----------------------------------------------------------------------------------------------------------------------------------------------------