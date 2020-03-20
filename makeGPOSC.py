"""
makeGPOSC.py takes the outputs from tRECs and makes GPosc compatable output files from full tracks

usage: makeGPOSC.py [-h] [-c C] [-v V] tRecs_file

positional arguments:
  tRecs_file

optional arguments:
  -h, --help         show this help message and exit
  -c C, -channel C
  -v V, -variable V


"""

if __name__ == "__main__":

    import pandas as pd
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('tRecs_file')
    parser.add_argument('-c', '-channel', type=int, default=2)
    parser.add_argument('-v', '-variable', type=str, default='Intensity Mean')

    args = parser.parse_args()

    data_file = pd.read_csv(args.tRecs_file, header=0, sep='\t')

    data_file = data_file.loc[(data_file.variable==args.v)&(data_file.channel==args.c)]

    data_file = data_file[['hours', 'value', 'full_track']]
    
    data_file_melt = data_file.pivot(columns='full_track', index='hours', values='value')   
    
    data_file_melt = pd.DataFrame(data_file_melt)
    
    data_file_melt.insert(0, 'hours', data_file_melt.index)

    print(data_file_melt.head())
    pd.DataFrame.to_excel(data_file_melt, args.tRecs_file.replace('.tsv', '.xlsx'), index=False)