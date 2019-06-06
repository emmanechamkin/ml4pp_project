import pandas as pd
import numpy as np
import sys
import os

## This script produces one concatenated file. 
## I did not end up using this in my final work.

OUTPUT = "final_output.csv"
CLEANED = "final_output_cleaned_sampled.csv"

def run_concatenation(files, output=OUTPUT):
    for file in files:
        os.system(f"cat {str(file)} >> {str(output)}")


def reduce_df(output=OUTPUT, cleaned=CLEANED, seed=0):
    all_data = pd.read_csv(output)
    relevant_tweets = all_data[all_data.iloc[:,1] != "Neutral"]
    np.random.seed(seed)
    relevant_tweets.iloc[:,0].to_frame().sample(1000).to_csv(CLEANED, header=None)

if __name__ == "__main__":
    assert len(sys.argv) > 1, "Usage: python3 combine_and_sample.py <all files>"
    try: 
        run_concatenation(sys.argv[1:])
    except IOError as e:
        print("IO Error:", e)
    except Exception as e:
        print("General exception", e)

    reduce_df()