CANVAS_SIZE = 5

def texdraw(*points):
    """ Create a 5 x 5 matrix and draw points (and axis-aligned line) on it """

    texbuf = [[False for _ in range(CANVAS_SIZE)] for _ in range(CANVAS_SIZE)]
    points = list(points)
    points.reverse()
    curpnt = points.pop()
    while len(points) > 0:
        nxtpnt = points.pop()
        nx, ny = nxtpnt
        cx, cy = curpnt
        texbuf[cx][cy] = True
        while cx != nx or cy != ny:
            sgn = lambda x: 0 if x == 0 else x//abs(x)
            cx += sgn(nx - cx)
            cy += sgn(ny - cy)
            texbuf[cx][cy] = True
        curpnt = nxtpnt
    return texbuf

"""
Waypoints

A---B
|...|
C---D
|...|
E---F

"""
A, B, C, D, E, F = [(4 * i, 2 * j)  for j in [0, 1, 2] for i in [0, 1] ]

"""
Texture of each number
"""
numberDraw = [
    texdraw(A, B, F, E, A) #0
    , texdraw(B, F) #1
    , texdraw(A, B, D, C, E, F) #2
    , texdraw(A, B, D, C, D, F, E) #3
    , texdraw(A, C, D, B, F) # 4
    , texdraw(B, A, C, D, F, E) # 5
    , texdraw(C, D, F, E, A, B) # 6
    , texdraw(A, B, F) # 7
    , texdraw(C, A, B, F, E, C, D) #8
    , texdraw(D, C, A, B, F, E) #9
]

def render(N, M1, M2):
    """ Render N to screen with M1 vertical scaling and M2 horizontal scaling"""

    digits = []
    #Transform to digits
    while N > 0:
        digits.append(N % 10)
        N //= 10
    digits.reverse()

    for line in range(CANVAS_SIZE * M1):
        output = ""
        for d in digits:
            output += ''.join(str(d) if numberDraw[d][x//M2][line//M1] else " " for x in range(M2 * CANVAS_SIZE))
            output += ' ' * M2
        print(output)


if __name__ == "__main__":
    N, M1, M2 = [int(x) for x in input().split(' ')]
    render(N, M1, M2)

