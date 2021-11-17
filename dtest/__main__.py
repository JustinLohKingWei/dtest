import argparse
import sys
import subprocess
from .dtest import dtest


def main():
    parser = argparse.ArgumentParser(
        description='dtest is a CLI tool which parses given patient data and determines if they are diabetic or not')
    parser.add_argument('-t', action="store_true", help="runs unit tests")
    parser.add_argument('-o', action="store", help="specifies the output file to write data to. If one does not exist a default one will be created",
                        type=str, nargs="?", const="test_results.csv")
    parser.add_argument('-i', action="store", help="Specifies the file to be read. Default is the 2020-10-28_patient_data.csv when launching the application.",
                        type=str, nargs="?", const="2020-10-28_patient_data.csv")
    args = parser.parse_args()

    if args.t:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])
        
    dtest(args.i, args.o)

if __name__ == '__main__':
    main()
