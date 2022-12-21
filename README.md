# Wavelet Tree Datastructure and RQQ

# Question 

Let A =[a1, a2, a3, . . . ..an] be a given sequence of integers. The range quantile query RQQ(k, l ,r ) over A returns the k-th smallest integer in the range A[l. . . .r].
For example, on the given A[1. . . 10] = [6, 2, 0, 7, 9,3 ,1,8,5,4] sequence , RQQ(5,3,9) returns
5th smallest integer in the range A[3. . . . . . 9] = [0, 7, 9, 3, 1, 8, 5]
Implement the range quantile queries with the wavelet tree data structure

# This is how it will look like.

wv_tree = Wavelet_Tree([6, 2, 0, 7, 9, 3, 1, 8, 5, 4])
wv_tree.print()

Level 0: 1001100110

Level 1: 00101, 00110

Level 2: 100, 01, 010, 10

Level 3: 01, X, X, X, 10, X, X, X

wv_tree.RQQ(5, 3, 9)

Level 0: (5,3,9)

Level 1: (2,2,5)

Level 2: (2,2,3)

Level 3: (1,1,1)
