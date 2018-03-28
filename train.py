from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression

import location
import map

__author__ = 'Michael'


class Trainer(object):
    def __init__(self, map, binary):
        self.map = map
        self.binary = binary

    def __transform(self, data):
        return zip(*[((loc.x, loc.y), self.map[loc.city]) for loc in data])

    def train(self, data):
        x, y = self.__transform(data)
        if self.binary:
            model = LogisticRegression()
        else:
            model = LogisticRegression(
                multi_class='multinomial',
                solver='saga'
            )
        model.fit(x, y)
        return model

    def test(self, model, data):
        x, y = self.__transform(data)
        return model.score(x, y)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('output')
    parser.add_argument('--binary', action='store_true')
    parser.add_argument('map')
    parser.add_argument('data', nargs='+')
    parser.add_argument('--test')
    args = parser.parse_args()

    city_map = map.read_file(args.map)
    trainer = Trainer(city_map, args.binary)

    data = location.read_files(*args.data)
    model = trainer.train(data)
    joblib.dump(model, args.output)

    if args.test:
        test = location.read_files(args.test)
        print(trainer.test(model, test))
