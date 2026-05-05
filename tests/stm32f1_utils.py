import subprocess


def flash_mcu(binary_path: str) -> str:
    """Returns the error string, if failure. No return is success."""
    completed_process = subprocess.run(
        [
            "st-flash",
            "--reset",
            "write",
            binary_path,
            "0x8000000",
        ],
        check=True,
        capture_output=True,
    )
    if completed_process.returncode != 0:
        return completed_process.stderr

    return ""
