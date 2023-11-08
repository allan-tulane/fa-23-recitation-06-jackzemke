# CMPS 2200 Recitation 06
## Answers

**Name:** Jack Zemke


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
    - 
    Because each call creates two recursive calls, the recurrence for the work of this function can be modeled by $W(n) = W(n-1) + W(n-2) + 1$ where the $+1$ represents the additional constant work of incrimenting the `counts` list. For a node of size $n$, the cost of the root is $1$ and the cost of its children is $2$. Since there is a geometric increase, this recurrence is leaf dominated. At the leaf level, there are $2^n$ nodes each with a cost of $1$, so the work of this algorithm is upper bounded by $O(2^n)$

- **3)**
    - 
    This algorithm does not run in parallel, so the recurrence for the span is the same as the recurrence for the work: $W(n) = W(n-1) + W(n-2) + 1$. This recurrence is upper bounded by $O(2^n)$ as shown in problem 2. 

- **4)**
    - 
    I notice that the elements in `counts` are a fibonacci sequence themselves. 

- **6)**
    -
    The maximum number of times that `fib_top_down(i)` will be called for any value $i$ is just 1. Since the additional work of each call is $1$, the work of this implimentation is upper bounded by $O(n)$. This algorithm does not run in parallel, so its span is the same, $O(n)$.

- **8)**
    - 
    Same as top down. The maximum number of times that `fib_bottom_up(i)` will be called for any value $i$ is just 1. Since the additional work of each call is $1$, the work of this implimentation is upper bounded by $O(n)$. This algorithm does not run in parallel, so its span is the same, $O(n)$.
