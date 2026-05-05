from pytest import approx, mark
from scope_utils import Scope
from stm32f1_utils import flash_mcu
from typing import Final
import time


SCOPE_IP_ADDRESS: Final[str] = "192.168.0.21"
TCP_IP_STRING: Final[str] = f"TCPIP::{SCOPE_IP_ADDRESS}::INSTR"
SCOPE_SCPI_SOCKET_PORT: Final[int] = 5555


@mark.parametrize("expected_duty_width_ms, mcu_program_binary", [
    (48, "bins/48ms_square_wave.bin"),
    (100, "bins/100ms_square_wave.bin"),
])
def test_square_wave(expected_duty_width_ms, mcu_program_binary):
    # Arrange
    #  - Flash MCU
    flash_error = flash_mcu(mcu_program_binary)
    if flash_error:
        error_message = f"Unable to flash the '{mcu_program_binary}' to the STM32F2 MCU."
        raise RuntimeError(error_message)
    time.sleep(0.2)

    with Scope(TCP_IP_STRING) as scope:
        duty_ms = scope.measure_pulse_width_ms()
        assert duty_ms == approx(expected_duty_width_ms, rel=1e-3)
