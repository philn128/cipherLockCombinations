Let $C(n)$ be the set of nonempty sequences of
disjoint nonempty subsets of the set $\{1,\ldots,n\}$.

Let $D(n)$ be the set of sequences of disjoint nonempty sets
with union $\{1,\ldots,n\}$.
Then the cardinality $|C(n)|$ is $2|D(n)|-1$ because
any sequence $(a_1,\ldots,a_m)$ in $D(n)$ of length 2 or more
can be truncated to $(a_1,\ldots,a_{m-1})$ to obtain
a sequence in $C(n)$ but not in $D(n)$. Conversely,
any sequence $(b_1,\ldots,b_l)$ in $C(n)$ but not $D(n)$
has a unique extension $(b_1,\ldots,b_{l+1})$ of length $l+1$
that is in $D(n)$.

Let $D(n,k)$ be the set of all sequences $(a_1,\ldots,a_k)$
of $k$ disjoint nonempty sets with union $\{1,\ldots,n\}$.
Then the cardinality $|D(n)|$ is $\sum_{k=1}^n|D(n,k)|$.

The cardinality $|D(n,k)|$ satisfies the recursion
$$|D(n,k)| = k(|D(n-1,k)|+|D(n-1,k-1)|)$$ because if $a_1,\ldots,a_k$
are disjoint and nonempty with union $\{1,\ldots,n-1\}$,
then there we could replace any of the $k$ sets $a_i$ with $a_i\cup\{n\}$
to make the union $\{1,\ldots,n\}$, and if $b_1,\ldots,b_{k-1}$
are disjoint and nonempty with union $\{1,\ldots,n-1\}$,
then we could insert $\{n\}$ into any of $k$ positions in the sequence
$b_1,\ldots,b_{k-1}$ to obtain union $\{1,\ldots,n\}$.
Conversely, if $c_1,\ldots,c_k$ are disjoint and nonempty
with union $\{1,\ldots,n\}$, then we can reduce the union
to $\{1,\ldots,n-1\}$ either by removing a unique $c_i=\{n\}$ or
by removing $n$ from a unique $c_i$.

The above recursion is terminated using the boundary conditions
$|D(n,1)|=1$ and $D(n,k)=0$ if $n<k$.

