from sklearn.externals import joblib

import location
import map

__author__ = 'Michael'


class Predictor(object):
    def __init__(self, model, labels):
        self.model = model
        self.labels = labels

    def predict(self, lat, long):
        x, y = location.to_x(lat), location.to_y(long)
        prediction = model.predict([(x, y)])[0]
        return self.labels[prediction]


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('model')
    parser.add_argument('label')
    parser.add_argument('coordinate', nargs='+')
    args = parser.parse_args()

    model = joblib.load(args.model)

    label_map = map.read_file(args.label)
    label_map = {v: k for k, v in label_map.items()}
    predictor = Predictor(model, label_map)

    for coord in args.coordinate:
        lat, long = [float(i) for i in coord.split(',')]
        print(predictor.predict(lat, long))
