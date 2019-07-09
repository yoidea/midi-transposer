from argparse import ArgumentParser
from re import match
from music21 import *


def get_args():
    parser = ArgumentParser(description="")
    parser.add_argument("source", type=str, help="source")
    parser.add_argument("-a", "--analyze-key", action='store_true', help="analyze key")
    parser.add_argument("-t", "--transpose", type=str, help="transpose")
    parser.add_argument("-o", "--output", type=str, help="output")
    return parser.parse_args()


def main():
    args = get_args()
    midi = converter.parse(args.source)
    key = midi.analyze("key")
    if args.analyze_key:
        print(key)
    if args.transpose is not None:
        if match(r"^[A-G]$", args.transpose):
            print(args.transpose)
            diff = interval.Interval(key.tonic, pitch.Pitch(args.transpose))
        if match(r"^(\+|\-)([0-9]|1[0-2])$", args.transpose):
            print(args.transpose)
            diff = interval.ChromaticInterval(int(args.transpose))
    if args.output is not None:
        output = midi.transpose(diff)
        output.write("midi", fp=args.output)


if __name__ == "__main__":
    main()
