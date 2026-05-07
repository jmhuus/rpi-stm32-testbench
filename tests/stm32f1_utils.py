import subprocess
import logging


logging.basicConfig(
    filename="logs/stm32f1_utils.log",
    filemode="w",
    level=logging.INFO,
)


def flash_mcu(binary_path: str):
    """Flashes STM32F2 MCUs using the available ST-Link V2.

    Args:
        binary_path: Path to the arm-none-eabi ELF binary for
        the STM32F1 MCU.

    Raises:
        subprocess.SubprocessError if the st-flash CLI exits
        abnormally.
    """
    cmd = [
        "st-flash",
        "--reset",
        "write",
        binary_path,
        "0x8000000",
    ]
    logging.info(
        f"Flashing the STM32F1 MCU with the '{binary_path}' binary."
    )
    subprocess.run(cmd, check=True, capture_output=True)
    logging.info("MCU flashing successful")
