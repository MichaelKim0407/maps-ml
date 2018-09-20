# Machine Learning with Google Maps

This project uses Google Maps API and machine learning to predict the city of a geo-coordinate.

## Installation and configuration

1. Install requirements

        pip install -r requirements.txt

2. Get API key

    [Get your own Google Maps API key](https://cloud.google.com/maps-platform/) and store it in `key.txt`.

3. Coordinates

    The scripts are used for geo-coordinates within `117.95 ~ 117.68 W`, `33.76 ~ 33.63 N`,
    which is an area around Irvine, CA, United States.

    You may edit these values in `location.py`,
    however you won't be able to use downloaded data in `data/` folder.

## Usage

1. `download.py`

    Download data using Google Maps API.
    See `python download.py --help` for details.

    Please be aware that if you use too many api calls Google may charge you.
    See pricing section in Google API documentations.

2. `map.py`

    Generate a mapping of locations to their categories using your data.
    See `python map.py --help` for details.

    If `--binary` is specified, only two categories will be generated,
    and basic logical regression will be used in the next step.

3. `train.py`

    Train the model using data specified.
    See `python train.py --help` for details.

    If `--binary` is specified, basic logical regression will be used.

    If `--test` is specified, run a test with the trained model and display results.
    This test data should not be one of the data files used in training.

4. `predict.py`

    Predict the location of coordinates using the trained model.
    See `python predict.py --help` for details

    The label file is used to associate category with location names in the output.
    For non-binary mode, you can simply use the map file.
    For binary mode, you can create a file with two lines:

        0,Others
        1,{City name}

5. `draw.py`

    Plot a map using your data.
    See `python draw.py --help` for details.
