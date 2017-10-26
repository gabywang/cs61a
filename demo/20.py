# Linked lists

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

def filter_link(f, s):
    """Return elements e of s for which f(e) is true."""
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered

def extend_link(s, t):
    if empty(s):
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))

# Sets as sorted sequences

def make_set(vals):
    """The set containing the values in list VALS."""
    result = Link.empty
    

def empty(s):
    return s is Link.empty

def contains(s, v):
    """Return true if set s contains value v as an element.

    >>> s = Link(1, Link(2, Link(3)))
    >>> contains(s, 2)
    True
    >>> contains(s, 5)
    False
    """
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return contains(s.rest, v)

def adjoin(s, v):
    """Return a set containing all elements of s and element v.

    >>> s = Link(1, Link(2, Link(3)))
    >>> t = adjoin(s, 4)
    >>> t
    Link(4, Link(1, Link(2, Link(3))))
    """
    if contains(s, v):
        return s
    else:
        return Link(v, s)

def intersect(set1, set2):
    """Return a set containing all elements common to set1 and set2.

    >>> s = Link(1, Link(2, Link(3)))
    >>> t = adjoin(s, 4)
    >>> intersect(t,  Link(1, Link(4, Link(9))))
    Link(4, Link(1))
    """
    in_set2 = lambda v: contains(set2, v)
    return filter_link(in_set2, set1)

def union(set1, set2):
    """Return a set containing all elements either in set1 or set2.

    >>> s = Link(1, Link(2, Link(3)))
    >>> t = adjoin(s, 4)
    >>> union(t, s)
    Link(4, Link(1, Link(2, Link(3))))
    """
    not_in_set2 = lambda v: not contains(set2, v)
    set1_not_set2 = filter_link(not_in_set2, set1)
    return extend_link(set1_not_set2, set2)

# Sets as (sorted) ordered sequences

def contains2(s, v):
    """Return true if set s contains value v as an element.

    >>> s = Link(1, Link(2, Link(3)))
    >>> contains2(s, 2)
    True
    >>> contains2(s, 5)
    False
    """
    if empty(s) or s.first > v:
        return False
    elif s.first == v:
        return True
    else:
        return contains2(s.rest, v)

def adjoin2(s, v):
    """Return a set containing all elements of s and element v.

    >>> s = Link(1, Link(2, Link(3)))
    >>> t = adjoin2(s, 4)
    >>> t
    Link(1, Link(2, Link(3, Link(4))))
    """
    if empty(s) or s.first > v:
        return Link(v, s)
    elif s.first == v:
        return s
    else:
        return Link(s.first, adjoin2(s.rest, v))

def add(s, v):
    """Add v to a set s, returning modified s. If s is not empty,
    returns same object.

    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
    """
    if empty(s):
        return Link(v)
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v, s.rest)
    elif s.first < v:
        add(s.rest, v)
    return s

def intersect2(set1, set2):
    """Return a set containing all elements common to set1 and set2.

    >>> s = Link(1, Link(2, Link(3)))
    >>> t = Link(2, Link(3, Link(4)))
    >>> intersect2(s, t)
    Link(2, Link(3))
    """
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, intersect2(set1.rest, set2.rest))
        elif e1 < e2:
            return intersect2(set1.rest, set2)
        elif e2 < e1:
            return intersect2(set1, set2.rest)

def union2(set1, set2):
    """Return a set containing all elements either in set1 or set2.

    >>> s = Link(1, Link(2, Link(3)))
    >>> t = Link(2, Link(3, Link(4)))
    >>> union2(s, t)
    Link(1, Link(2, Link(3, Link(4))))
    """
    if empty(set1):
        return set2
    elif empty(set2):
        return set1
    else:
        e1, e2 = set1.first, set2.first
        if e1 == e2:
            return Link(e1, union2(set1.rest, set2.rest))
        elif e1 < e2:
            return Link(e1, union2(set1.rest, set2))
        elif e2 < e1:
            return Link(e2, union2(set1, set2.rest))
