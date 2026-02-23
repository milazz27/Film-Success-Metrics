import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd

'''
EXAMPLE OF FILE ACCCESS FOR IMDB DATASET
'''

# Set the path to the file you'd like to load
file_path = "imdb_top_1000.csv"

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows",
  file_path
)

print("First 5 records:", df.head())