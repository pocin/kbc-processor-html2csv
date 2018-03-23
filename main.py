import logging
import os
import sys
import pandas as pd
import glob


def find_all_files(datadir):
    logging.info("Looking for files in '%s'", datadir)
    for path in glob.iglob(os.path.join(datadir, '**/*'), recursive=True):
        if os.path.isfile(path):
            yield path


def _build_outpath_from_inpath(inpath):
    infolder, name = os.path.split(inpath)
    outfolder = infolder.replace('/data/in/files', '/data/out/files')
    if not os.path.isdir(outfolder):
        os.makedirs(outfolder)
    basename, suffix = os.path.splitext(name)
    outpath = os.path.join(outfolder, basename + '.csv')
    return outpath

def _parse_table(inpath):
    df = pd.read_html(inpath)[0]
    return df

def process_table(inpath):
    logging.info("processing '%s'", inpath)
    df = _parse_table(inpath)
    outpath = _build_outpath_from_inpath(inpath)
    logging.info("saving into '%s'", outpath)
    df.to_csv(outpath, index=False)
    return outpath

def main(datadir):
    for path in find_all_files(datadir):
        process_table(path)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO)
        main('/data/in/files/')
    except (ValueError, KeyError) as err:
        logging.error(err)
        sys.exit(1)
    except:
        logging.exception("Internal error")
        sys.exit(2)
