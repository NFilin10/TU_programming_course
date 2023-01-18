
A = {'♥','♦','♠','♣'}
B = {'A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'}



def korrutis(A, B):
    C = set()
    for x in A:
        for y in B:
            C.add((x, y))
    return C

print(korrutis(A, B))