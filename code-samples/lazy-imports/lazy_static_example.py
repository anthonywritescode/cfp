import argparse

from lazy_static import lazy


@lazy
def something_slow() -> int:
    print('evaluating!')
    return 5


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.parse_args()  # just for help

    print(something_slow)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
