import sys
import unittest
from pathlib import Path

from botocore.exceptions import ClientError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.load_IAM import _already_exists


class LoadIamIdempotencyTests(unittest.TestCase):
    def test_detects_localstack_style_group_already_exists(self):
        error = ClientError(
            {"Error": {"Code": "Unknown", "Message": "Group bigdata-read already exists"}},
            "CreateGroup",
        )
        self.assertTrue(_already_exists(error))

    def test_detects_entity_already_exists(self):
        error = ClientError(
            {"Error": {"Code": "EntityAlreadyExists", "Message": "Already exists"}},
            "CreateGroup",
        )
        self.assertTrue(_already_exists(error))


if __name__ == "__main__":
    unittest.main()
