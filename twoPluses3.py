def twoPluses(grid):
    # 1. Find all crosses
    # 2. Find radii that produce maximal product
    # 3. Find cross pair whose cells are distinct

    def rad_index(grid):
        # Returns dictionary of all crosses
        #   radius : [[y1, x1], [y2, x2], ...]
        g = [[c == 'G' for c in r] for r in grid]
        y, x, out = len(g), len(g[0]), {}
        for i in range(y):
            for j in range(x):
                if g[i][j]:
                    r = 1
                    while all(
                        [i - r >= 0, j - r >= 0,
                        i + r < y, j + r < x]
                    ):              # check within grid range
                        if all(
                            [g[i - r][j], g[i + r][j],
                            g[i][j - r], g[i][j + r]]
                        ):          # check neighbors
                            r += 1  # increment radius if ok
                        else:
                            break
                    while r > 0:    
                        r -= 1      # add index to every sub-cross
                        out[r] = out.get(r, set()) | {(i, j)}
        return(out)
    
    def prods(x):
        # Returns dictionary of products and
        # factors given dictionary of crosses 'x'
        #   product : [[f0, f1], [f2, f3], ...]
        F, out = {i: len(x[i]) for i in x}, {}
        for r1 in F:
            F[r1] -= 1              # 1 instance of factor used
            for r2 in F:            # at least 1 instance left
                if F[r2] > 0 and r1 <= r2:
                    p = (4 * r1 + 1) * (4 * r2 + 1)
                    out[p] = out.get(p, set()) | {(r1, r2)}
        return(out)
        
    def cells(r, i):
        # Returns set of cells spanned
        # given cross of radius 'r' at index 'i'
        y, x = i
        v = {(R, x) for R in range(y - r, y + r + 1)}
        h = {(y, C) for C in range(x - r, x + r + 1)}
        return(v | h)

    d = rad_index(grid)
    p = prods(d)
    for m in sorted(p)[::-1]:       # start with largest product
        for f in p[m]:              # for each unique factor pair
            r1, r2 = f
            for c1 in d[r1]:        # check radius 1 cross cells
                for c2 in d[r2]:    # check radius 2 cross cells
                    if not cells(r1, c1) & cells(r2, c2):
                        return(m)   # return if cells are distinct
                    
    
grid = [
    'BGBBGB',
    'GGGGGG',
    'BGBBGB',    
    'GGGGGG',
    'BGBBGB',
    'BGBBGB'
    ]
print(twoPluses(grid))