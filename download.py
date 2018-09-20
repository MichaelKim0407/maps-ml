import numpy as np

import location

__author__ = 'Michael'


def random_points(n):
    for p in np.random.random((n, 2)):
        yield list(p)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'output',
        help='Output file'
    )
    parser.add_argument(
        'count', type=int,
        help='Amount of data to download'
    )
    args = parser.parse_args()

    with open(args.output, 'w') as f:
        for p in random_points(args.count):
            l = location.Location(*p)
            f.write(str(l))
            f.write('\n')
            f.flush()
