#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from one_golden_test import OneGoldenTest


def main(argv):
    if len(argv) < 5:
        print(
            f"Usage: {argv[0]} emboss_front_end emboss_compiler emb_file golden_file [include_dir...]"
        )
        return 1

    emboss_front_end = argv[1]
    emboss_compiler = argv[2]
    emb_file = argv[3]
    golden_file = argv[4]
    include_dirs = argv[5:]

    suite = unittest.TestSuite()
    suite.addTest(
        OneGoldenTest(
            emboss_front_end, emboss_compiler, emb_file, golden_file, include_dirs
        )
    )
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
