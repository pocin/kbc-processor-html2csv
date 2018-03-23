import logging
import os
import pandas as pd
import glob


def find_all_files(datadir):
    logging.debug("Looking for files in '%s'", datadir)
    for path in glob.iglob(os.path.join(datadir, '**/*'), recursive=True):
        if os.path.isfile(path):
            yield path


def _build_outpath_from_inpath(inpath):
    outfolder, name = os.path.split(inpath)
    basename, suffix = os.path.splitext(name)
    outpath = os.path.join(outfolder, basename + '.csv').replace('/data/in/files/', '/data/out/files/')
    return outpath

def _parse_table(inpath):
    df = pd.read_html(inpath)[0]
    return df

def process_table(inpath):
    logging.debug("processing '%s'", inpath)
    outpath = _build_outpath_from_inpath(inpath)
    df = _parse_table(inpath)
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
    except:
        logging.exception("Internal error")
