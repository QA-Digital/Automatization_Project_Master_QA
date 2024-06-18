from starter_master_browserstack import runner_tests_generalized
from FWSK.starter_local import suite_FWSK_full
import unittest


while True:
    runner_tests_generalized(suite_FWSK_full, "FWSK")