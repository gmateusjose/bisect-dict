from bisect import bisect_right, bisect_left


def find_lt(seq, value):
    """Find rightmost value less than x"""
    if index := bisect_left(seq, value):
        return seq[index-1]
    raise ValueError


def find_le(seq, value):
    """Find rightmost value less than or equal to x"""
    if index := bisect_right(seq, value):
        return seq[index-1]
    raise ValueError


def find_gt(seq, value):
    """Find leftmost value greater than x"""
    index = bisect_right(seq, value)
    if index != len(seq):
        return seq[index]
    raise ValueError


def find_ge(seq, value):
    """Find leftmost item greater than or equal to x"""
    index = bisect_left(seq, value)
    if index != len(seq):
        return seq[index]
    raise ValueError


saldos_cbb = {
    '2021-01-01 00:00:00': {'valor': 5, 'pm': 0},
    '2022-01-01 00:00:00': {'valor': 10, 'pm': 0},
    '2022-01-01 18:00:00': {'valor': 1, 'pm': 0},
}

dt1 = find_gt(list(saldos_cbb.keys()), '2022-01-01 00:00:00')
assert dt1 == '2022-01-01 18:00:00'

dt2 = find_lt(list(saldos_cbb.keys()), '2022-01-01 00:00:00')
assert dt2 == '2021-01-01 00:00:00'
