from pathlib import Path
import sys
import time
import os
from easy_ec2 import library_root_dir
current_dir = Path(__file__).parent.__str__()
parent_dir = Path(__file__).parent.parent.__str__()
sys.path.append(parent_dir)
test_config_path = library_root_dir + '/examples/small_test.yaml'
main_path = library_root_dir + '/easy_ec2/main.py'

from easy_ec2.main import main  # noqa: E402


# conditional for github actions
bigquery_client = None
if "GITHUB_ACTIONS" in os.environ:
    test_config_path = './test_configs/small_test_github.yaml'
    main_path = '/home/runner/work/easy_ec2/easy_ec2/easy_ec2/main.py'


def test_ec2_list_all():
    # call main for ec2 list_all test
    result = main('easy_ec2', 'ec2', 'list_all')
    if result is not None:
        assert True
    else:
        assert False


def test_ec2_list_running():
    # call main for ec2 list_running test
    result = main('easy_ec2', 'ec2', 'list_running')
    if result is not None:
        assert True
    else:
        assert False


def test_ec2_list_stopped():
    # call main for ec2 list_stopped test
    result = main('easy_ec2', 'ec2', 'list_stopped')
    if result is not None:
        assert True
    else:
        assert False


def ec2_stop(instance_id):
    # call main for ec2 stop test
    result = main('easy_ec2', 'ec2', 'stop', instance_id)
    print(result)
    if result is not None:
        assert True
    else:
        assert False


def ec2_terminate(instance_id):
    # call main for ec2 stop test
    result = main('easy_ec2', 'ec2', 'terminate', instance_id)
    print(result)
    if result is not None:
        assert True
    else:
        assert False


def test_ec2_create():
    # call main for ec2 create test
    result = main('easy_ec2', 'ec2', 'create', test_config_path)
    print(f'result: {result}')
    if result is not None:
        instance_id = result['instance_id']

        # wait a few seconds to ensure instance is stop-able
        time.sleep(5)

        # stop instance
        ec2_stop(instance_id)

        # wait a few seconds to ensure instance is stop-able
        time.sleep(15)

        # stop instance
        ec2_terminate(instance_id)

        assert True
    else:
        assert False
