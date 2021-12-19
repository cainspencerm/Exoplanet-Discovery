import argparse
import csv
import os
import subprocess
from parse import parse
from tqdm import tqdm


parser = argparse.ArgumentParser()

parser.add_argument("--csv", type=str, required=True)
parser.add_argument("--download_dir", type=str, required=True)
parser.add_argument("--output_file", type=str, default="get_kepler.sh")
args = parser.parse_args()


_WGET_CMD = ("wget --no-clobber -nH --cut-dirs=6 -r -l0 -c -np -erobots=off "
             "-R 'index*' -A _llc.fits")
_BASE_URL = "https://archive.stsci.edu/pub/kepler/lightcurves"


# Get kepler IDs for download.
kepids = set()
with open(args.csv) as f:
    reader = csv.DictReader(row for row in f if not row.startswith("#"))
    for row in reader:
        kepids.add(row["kepid"])

# Begin download.
tqdm_kepids = tqdm(kepids)
tqdm_kepids.set_description(f'Projected Total Size: ?')

file_count = 0
size_count = 0
kepid_count = 0
for kepid in tqdm_kepids:
    kepid_count += 1

    # Prepare wget variables.
    padded_kepid = "{0:09d}".format(int(kepid))  # Pad with zeros.
    subdir = "{}/{}".format(padded_kepid[0:4], padded_kepid)
    download_dir = os.path.join(args.download_dir, subdir)
    url = "{}/{}/".format(_BASE_URL, subdir)

    # Run wget script.
    result = subprocess.run('{} -P {} {}'.format(_WGET_CMD, download_dir, url).split(), capture_output=True)

    # Update tqdm description.
    result = result.stderr.decode('utf-8').split('\n')[-2]
    files, size, _ = parse('Downloaded: {} files, {} in {}', result)
    file_count += int(files)

    if size[-1] == 'G':
        size = float(size[:-1]) * 1e9
    elif size[-1] == 'M':
        size = float(size[:-1]) * 1e6
    elif size[-1] == 'K':
        size = float(size[:-1]) * 1e3
    else:
        size = float(size[:-1])

    size_count += size
    avg_file_size = size_count / file_count
    avg_num_files = file_count / kepid_count
    total_kepids = len(kepids)
    projected_num_files = avg_num_files * total_kepids
    projected_total_size = projected_num_files * avg_file_size

    if projected_total_size > 1e12:
        projected_total_size = '{0:.3f}TB'.format(projected_total_size / 1e12)
    elif projected_total_size > 1e9:
        projected_total_size = '{0:.3f}GB'.format(projected_total_size / 1e9)
    elif projected_total_size > 1e6:
        projected_total_size = '{0:.3f}MB'.format(projected_total_size / 1e6)
    else:
        projected_total_size = '{0:.3f}KB'.format(projected_total_size / 1e3)

    tqdm_kepids.set_description(f'Projected Total Size: {projected_total_size}')
