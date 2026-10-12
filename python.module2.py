class Node:
    def __init__(self, c, p):
        self.c = c
        self.p = p
        self.next = None

def add(a, b):
    r = Node(0, 0)
    t = r

    while a and b:
        if a.p == b.p:
            c, p = a.c + b.c, a.p
            a, b = a.next, b.next
        elif a.p > b.p:
            c, p = a.c, a.p
            a = a.next
        else:
            c, p = b.c, b.p
            b = b.next

        t.next = Node(c, p)
        t = t.next

    while a:
        t.next = Node(a.c, a.p)
        t, a = t.next, a.next

    while b:
        t.next = Node(b.c, b.p)
        t, b = t.next, b.next

    return r.next

def show(p):
    while p:
        print(f"{p.c}x^{p.p}", end=" ")
        p = p.next

# P1 = 5x^3 + 4x^2 + 2
a = Node(5, 3)
a.next = Node(4, 2)
a.next.next = Node(2, 0)

# P2 = 3x^3 + 2x + 6
b = Node(3, 3)
b.next = Node(2, 1)
b.next.next = Node(6, 0)

result = add(a, b)

print("Sum: ", end="")
show(result)
