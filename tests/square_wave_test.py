from pytest import approx, mark
from scope_utils import Scope
from typing import Final


SCOPE_IP_ADDRESS: Final[str] = "192.168.0.21"
TCP_IP_STRING: Final[str] = f"TCPIP::{SCOPE_IP_ADDRESS}::INSTR"
SCOPE_SCPI_SOCKET_PORT: Final[int] = 5555


@mark.parametrize("expected_duty_ms", [(0.5)])
def test_square_wave(expected_duty_ms):
    with Scope(TCP_IP_STRING) as scope:
        duty_ms = scope.detect_square_wave_duty()
        assert duty_ms == approx(expected_duty_ms, rel=1e-3)
