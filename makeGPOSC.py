"""
makeGPOSC.py takes the outputs from tRECs and makes GPosc compatable output files from full tracks
"""

if __name__ == "__main__":

    import pandas as import pd
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('tRecs_file')
    parser.add_argument('-c', '-channel', type=int, default=2)

    args = parser.parse_args()

    