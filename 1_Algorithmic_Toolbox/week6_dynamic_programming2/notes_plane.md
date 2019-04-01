# Knapsack (w/ repetition)

Subproblems

Let value(w) be the maximum value of knapsack of weight w.

What is the recurrence? I think the idea is to fill knapsacks of smaller value. 

What is the unknown? How do we maximize the value for a given amount of kg from a set of discrete items if repetition is allowed.

If you've proven that the greedy approach to take as much of the highest value per unit weight item as possible is not a safe move, then what is another approach - Dynamic Programming.

Recurrence for Knapsack without repetitions:

value(w) = max i: wi <= w { value(w - wi) + vi }


Knapsack(W)
value(0) <- 0 # Maximum value of a knapsack of weight 0 is zero
for w from 1 to W:
  value(w) <- 0
  for i from 1 to n:
    if wi <= w: # wi is at most w
      val <- value(w - wi) + vi
      if val > value(w):
        value(w) <- val
return value(W)

# Knapsack (w/o repetition)

For 0 <= w <= W and 0 <= i <= n, value(w, i) is the maximum value achievable using a knapsack of weight w and items 1,...,i.

The i-th item is either used or not: value(w, i) is equal to:


Our goal is to express the solution of our problem through solutions of smaller subproblems - this is arguably the most important thing in designing dynamic programming algorithms.

Recurrence for Knapsack with repetitions:

max{ value(w - wi, i - 1) + vi, value(w, i-1) }

Knapsack(W)

initialize all value(0, j) <- 0
initialize all value(w, 0) <- 0
for i from 1 to n:
  for w from 1 to W:
    value(w, i) <- value(w, i - 1)
    if wi <= w:
      val <- value(w - wi, i - 1) + vi
      if value(w, i) < val:
        value(w, i) <- val
return value(W, n)


Reconstructiong an optimal solution
