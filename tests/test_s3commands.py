
import sys
print(sys.path)
sys.path.append('../..')
from genawspy.s3commands import *

test_bucket = "pg-test-s3-commands"
def test_s3_commands():
    ls(test_bucket)
    cp(__file__, test_bucket)