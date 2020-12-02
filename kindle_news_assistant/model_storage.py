"""A set of functions for storing and retrieving the article classification model."""
import os
from sklearn.linear_model import SGDClassifier  # type: ignore
from joblib import dump, load

dirname = os.path.dirname(__file__)
RELATIVE_PATH = "../userdata/model.pkl.compressed"
absolute_path = os.path.join(dirname, RELATIVE_PATH)


def model_exists():
    """Check whether the model file exists.

    :return: True if it exists, False otherwise
    """
    return os.path.isfile(absolute_path)


def load_model():
    """Load the model from the model file.

    :raises LookupError: The model file could not be found
    :return: The model as an SGDClassifer
    """
    if not model_exists():
        raise LookupError("Model file does not exist.")

    clf: SGDClassifier = load(absolute_path)
    return clf


def store_model(clf: SGDClassifier):
    """Dump the model data into the model file.

    The model is compressed using ZLIB compression.

    :param clf: The classifier to be stored
    """
    dump(clf, absolute_path, compress=("zlib", 3))
