import argparse

import pymupdf4llm


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    return parser.parse_args()


def main():
    args = parse_args()
    md_text = pymupdf4llm.to_markdown(args.filename)
    print(md_text)


if __name__ == "__main__":
    main()
