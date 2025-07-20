from datetime import datetime

import time_machine

from integrify.lsim.types import timestamp_to_str


@time_machine.travel('2025-04-03 02:01:00')
def test_timestamp_to_str_with_str():
    assert timestamp_to_str('NOW') == '2025-04-03 02:01:00'


def test_timestamp_to_str_with_datetime():
    assert timestamp_to_str(datetime(2025, 4, 3, 2, 1, 0)) == '2025-04-03 02:01:00'
