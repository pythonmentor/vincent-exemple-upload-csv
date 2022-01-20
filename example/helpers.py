import csv
import codecs
from collections import defaultdict


def parse_csv(file):
    """Parses the csv file and return a dictionnary representation of its
    content."""
    reader = csv.reader(codecs.iterdecode(file, 'utf-8'))
    return {
        'names': next(reader),
        'data': list(reader),
    }
