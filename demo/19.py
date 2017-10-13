class Tree:
    """A tree is a root value and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self, k=0):
        indented = []
        for b in self.branches:
            for line in b.indented(k + 1):
                indented.append('  ' + line)
        return [str(self.label)] + indented

    def is_leaf(self):
        return not self.branches

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

@memo
def fib_tree(n):
    """A Fibonacci tree.

    >>> print(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])

def leaves(tree):
    """Return the leaf values of a tree.

    >>> leaves(fib_tree(4))
    [0, 1, 1, 0, 1]
    """
    if tree.is_leaf():
        return [tree.label]
    else:
        return sum([leaves(b) for b in tree.branches], [])

def height(tr):
    """The height of TR."""
    if tr.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in tr.branches])

def prune(t, n):
    """Prune sub-trees whose label value is n.

    >>> t = fib_tree(5)
    >>> prune(t, 1)
    >>> print(t)
    5
      2
      3
        2
    """
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)

def prune_repeats(t, seen):
    """Remove repeated sub-trees

    >>> def fib_tree(n):
    ...     if n == 0 or n == 1:
    ...         return Tree(n)
    ...     else:
    ...         left = fib_tree(n-2)
    ...         right = fib_tree(n-1)
    ...         return Tree(left.label + right.label, (left, right))
    >>> fib_tree = memo(fib_tree)
    >>> t = fib_tree(6)
    >>> print(t)
    8
      3
        1
          0
          1
        2
          1
          1
            0
            1
      5
        2
          1
          1
            0
            1
        3
          1
            0
            1
          2
            1
            1
              0
              1
    >>> prune_repeats(t, [])
    >>> print(t)
    8
      3
        1
          0
          1
        2
      5
    """
    t.branches = [b for b in t.branches if b not in seen]
    seen.append(t)
    for b in t.branches:
        prune_repeats(b, seen)










def hailstone(n):
    """Print a hailstone sequence and return its length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone(3*n+1)

def is_int(x):
    return int(x) == x

def is_odd(n):
    return n % 2 == 1

def hailstone_tree(k, n=1):
    """Build a tree in which paths are hailstone sequences.

    >>> hailstone_tree(6)
    Tree(1, [Tree(2, [Tree(4, [Tree(8, [Tree(16, [Tree(32), Tree(5)])])])])])
    >>> leaves(hailstone_tree(11))
    [1024, 170, 168, 160, 26, 24]
     """
    if k == 1:
        return Tree(n)
    else:
        up, down = 2*n, (n-1)/3
        branches = [hailstone_tree(k-1, up)]
        if down > 1 and is_int(down) and is_odd(down):
            branches.append(hailstone_tree(k-1, int(down)))
        return Tree(n, branches)

def longest_path_below(k, t):
    """Return the longest path through t of values all down than k.

    >>> longest_path_below(20, hailstone_tree(10))
    [1, 2, 4, 8, 16, 5, 10, 3, 6, 12]
    """
    if t.label >= k:
        return []
    elif t.is_leaf():
        return [t.label]
    else:
        paths = [longest_path_below(k, b) for b in t.branches]
        return [t.label] + max(paths, key=len)

# Printing a tree laid out horizontally.  This is quite tricky. The
# solution below is not particularly efficient, and uses features of
# Python we have not yet covered.  By all means take a look at it,
# but we don't expect you to understand it comletely.

from io import StringIO
# A StringIO is a file-like object that builds a string instead of printing
# anything out.

def width(tr):
    """Returns the printed width of this tree."""
    lbl_wid = len(str(tr.label))
    w = max(lbl_wid,
            sum([width(t) for t in tr.branches]) + len(tr.branches) - 1)
    extra = (w - lbl_wid) % 2
    return w + extra

def pretty(tree):
    """Print TREE laid out horizontally rather than vertically."""

    def gen_levels(tr):
        w = width(tr)
        lbl = str(tr.label)
        lbl_pad = " " * ((w - len(lbl)) // 2)
        yield w
        print(lbl_pad, file=out, end="")
        print(lbl, file=out, end="")
        print(lbl_pad, file=out, end="")
        yield 

        if tr.is_leaf():
            pad = " " * w
            while True:
                print(pad, file=out, end="")
                yield
        below = [ gen_levels(b) for b in tr.branches ]
        L = 0
        for g in below:
            if L > 0:
                print(" ", end="", file=out)
                L += 1
            w1 = next(g)
            left = (w1-1) // 2
            right = w1 - left - 1
            mid = L + left
            print(" " * left, end="", file=out)
            if mid*2 + 1 == w:
                print("|", end="", file=out)
            elif mid*2 > w:
                print("\\", end="", file=out)
            else:
                print("/", end="", file=out)
            print(" " * right, end="", file=out)
            L += w1
        print(" " * (w - L), end="", file=out)
        yield
        while True:
            started = False
            for g in below:
                if started:
                    print(" ", end="", file=out)
                next(g);
                started = True
            print(" " * (w - L), end="", file=out)
            yield

    out = StringIO()
    h = height(tree)
    g = gen_levels(tree)
    next(g)
    for i in range(2*h + 1):
        next(g)
        print(file=out)
    print(out.getvalue(), end="")
