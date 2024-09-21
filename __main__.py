import os.path

from dotenv import load_dotenv

from textblaze_to_espanso import TextBlazeToEspansoConverter
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "--env_file", type=str, help="Path to env file for the package "
    )
    args = parser.parse_args()
    if args.env_file:
        if os.path.exists(args.env_file):
            load_dotenv(args.env_file)
            print(f"Loaded environment variables from {args.env_file}")
        else:
            print(f"File {args.env_file} does not exist.")
            exit(1)


if __name__ == "__main__":
    parse_arguments()
    TextBlazeToEspansoConverter().convert()
