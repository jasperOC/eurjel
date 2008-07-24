import sys, os

buildout_dir = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(__file__)))
os.environ['NLTK_DATA'] = os.path.join(buildout_dir, 'parts', 'nltk', 'data')

from _eurjel import word_frequency
