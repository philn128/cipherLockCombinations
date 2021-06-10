# $C(n)$ and $D(n)$

Let $C(n)$ be the set of nonempty sequences of disjoint nonempty subsets of the set $\{1,\ldots,n\}$.

Let $D(n)$ be the set of sequences of disjoint nonempty sets with union $\{1,\ldots,n\}$.

## example

$$C(2)= \left\{\begin{array}{c} (\{1\}) \\ (\{2\}) \\ (\{1\},\{2\}) \\ (\{2\},\{1\}) \\ (\{1,2\}) \end{array} \right\}$$

$$D(2)=\left\{\begin{array}{c} (\{1\},\{2\}) \\ (\{2\},\{1\}) \\ (\{1,2\}) \end{array} \right\}$$

> note that the order of $D$ doesn't matter whereas the order of $C$ does

* $\{1,2\}$ is a [set](https://en.wikipedia.org/wiki/Set_(mathematics)) and order independent whereas $(1,2)$ is a [sequence](https://en.wikipedia.org/wiki/Sequence). $\{1,2\}$ means 1 and 2 at the same time wherease $(1,2)$ means pressing a 1 followed by a 2.
* For $D(n)$ and $C(n)$ [_disjoint_](https://en.wikipedia.org/wiki/Disjoint_sets) means not being able to use the same number more than once per sequence. So having a sequence $(\{1\},\{1\})$ would be invalid because $\{1\} \cap \{1\} \neq \emptyset$

```bash
# finding C(n) can be done using random sampling
./keypad_random.py -k 2 -n 1e4
```

# Relationship between |$C(n)$| and $|D(n)|$ cardinality

The [cardinality](https://en.wikipedia.org/wiki/Cardinality) (size) of $|C(n)|$ is $2|D(n)|-1$ because
any sequence $(a_1,\ldots,a_m)$ in $D(n)$ of length 2 or more
can be truncated to $(a_1,\ldots,a_{m-1})$ to obtain
a sequence in $C(n)$ but not in $D(n)$.

Conversely, any sequence $(b_1,\ldots,b_l)$ in $C(n)$ but not $D(n)$
has a unique extension $(b_1,\ldots,b_{l+1})$ of length $l+1$
that is in $D(n)$.

In other words, if we have a set of sequences $T(n)$ where $T(n)$ is the is a set where the last element of each sequence in $D(n)$ has been truncated then

$$T(n) \cup D(n) = C(n) \cup \{\emptyset\}$$

## example

### cardinality

$$|C(2)|=5=2 \cdot |D(2)|-1=2\cdot 3-1=5$$

* We have $n$ button presses in each $D(n)$. $C(n)$ has more sequences because we don't need to use all the buttons.

### truncating

* Truncating $(\{2\},\{1\})$ gives $\{2\}$ and truncating $(\{1\},\{2\})$ gives $\{1\}$
	* If we "truncated" all the way to $a_m$ instead of $a_{m-1}$ we wouldn't be truncating

$$T(2) = \left\{\begin{array}{c} (\{1\}) \\ (\{2\}) \\ (\{\}) \end{array} \right\}$$

> note that truncating $\{1,2\}=\{\}=\emptyset$

$$T(2) \cup D(n) = \left\{\begin{array}{c} (\{1\}) \\ (\{2\}) \\ (\{\}) \end{array} \right\} \cup \left\{\begin{array}{c} (\{1\},\{2\}) \\ (\{2\},\{1\}) \\ (\{1,2\}) \end{array} \right\} = \left\{\begin{array}{c} (\{1\}) \\ (\{2\}) \\ (\{\}) \\ (\{1\},\{2\}) \\ (\{2\},\{1\}) \\ (\{1,2\}) \end{array} \right\} = C(n) \cup \{\emptyset\}$$

$$\therefore T(2) \cup D(n) \backslash \{\emptyset\} = C(2)$$

> The backslash symbol ($\backslash$) denotes [set difference](https://en.wikipedia.org/wiki/Complement_(set_theory)#Relative_complement). For example, $\{1,2\} \backslash \{1\} = \{2\}$

# Finding $|D(n)|$ cardinality

## splitting $|D(n)$ into subsets with fixed sequence length 

Let $D(n,k)$ be the set of all sequences $(a_1,\ldots,a_k)$
of $k$ disjoint nonempty sets with union $\{1,\ldots,n\}$.
Then the cardinality $|D(n)|$ is $\displaystyle \sum_{k=1}^n|D(n,k)|$.

### example

Each sequence of $D(n,k)$ is of length $k$. We're effectivley splitting $D(n)$ into various subsets where the sequence lengths are the same for each subset

$$\bigcup_{k=1}^n D(n,k) = D(n)$$

$$D(2,1) = \left\{\begin{array}{c} (\{1,2\}) \end{array} \right\}$$

$$D(2,2) = \left\{\begin{array}{c} (\{1\},\{2\}) \\ (\{2\},\{1\}) \end{array} \right\}$$

> Although $\{1,2\}$ is of length 2 the sequence $(\{1,2\})$ is of length 1

## recursion

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

