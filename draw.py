import itertools
from collections import defaultdict

import matplotlib.pyplot as plt

import location
import map

__author__ = 'Michael'


class Plotter(object):
    def __init__(self, map, labels):
        self.map = map
        self.labels = labels

        # number of different colors
        self.n = len(set(map.values()))

    def __transform(self, data):
        result = defaultdict(lambda: [])
        for d in data:
            result[self.map[d.city]].append((d.y, 1 - d.x))
        return result

    def plot(self, data):
        data = self.__transform(data)

        fig = plt.figure()
        ax = fig.add_subplot('111')
        markers = itertools.cycle('.+x')
        for i in sorted(data.keys()):
            marker = next(markers)
            x, y = zip(*data[i])
            ax.scatter(x, y, marker=marker, label=self.labels[i])
        ax.legend()
        return fig


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('output')
    parser.add_argument('map')
    parser.add_argument('label')
    parser.add_argument('data', nargs='+')
    args = parser.parse_args()

    city_map = map.read_file(args.map)
    label_map = map.read_file(args.label)
    label_map = {v: k for k, v in label_map.items()}
    plotter = Plotter(city_map, label_map)

    data = location.read_files(*args.data)
    fig = plotter.plot(data)

    fig.savefig(args.output)
