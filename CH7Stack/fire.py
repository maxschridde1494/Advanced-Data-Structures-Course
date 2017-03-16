def helper(pts_lst, choc_lst):
    if len(points) == 0:
        return 0
    elif len(points) == 1:
        return choc_lst[0]
    else:
        m = pts_lst.index(min(pts_lst))
        if m > 0:
            if m < len(pts_lst) - 1:
                if pts_lst[m + 1] > pts_lst[m]:
                    choc_lst[m + 1] += 1
            if pts_lst[m - 1] > pts_lst[m]:
                choc_lst[m-1] += m-1
        else:
            if pts_lst[m + 1] > pts_lst[m]:
                    choc_lst[m + 1] += 1
        return choc_lst[m] + helper(pts_lst[:m], choc_lst[:m]) + helper(pts_lst[m+1:], choc_lst[m+1:])

def distributeChocolate(points):
    """
    >>> distributeChocolate([1,5,7,1])
    7
    """
    return helper(points, [1 for i in range(len(points))])