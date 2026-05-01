import json
import os
import re


FREERTOS_LIB_DIR = "lib/freertos/"
LIBOPENCM3_LIB_DIR = "lib/libopencm3/"
LIBOPENCM3_SOURCE_DIR = os.path.join(LIBOPENCM3_LIB_DIR, "lib/stm32/f1/")


def get_freertos_commands() -> list[dict]:
    build_commands_path = os.path.join(FREERTOS_LIB_DIR, "build_commands.txt")
    if not os.path.exists(build_commands_path):
        return []
    with open(build_commands_path, "r") as f:
        gcc_commands = f.readlines()

    commands = []
    for gcc_command in gcc_commands:
        gcc_command = gcc_command.rstrip()
        commands.append({
            "command": gcc_command,
            "directory": os.path.join(os.getcwd(), FREERTOS_LIB_DIR),
            "file": re.findall(r"[^\s]+\.c", gcc_command)[0],
            "output": re.findall(r"[^\s]+\.o", gcc_command)[0],
        })

    return commands


def get_libopencm3_commands() -> list[dict]:
    build_commands_path = os.path.join(
        LIBOPENCM3_LIB_DIR, "build_commands.txt")
    if not os.path.exists(build_commands_path):
        return []
    with open(build_commands_path, "r") as f:
        gcc_commands = f.readlines()

    commands = []
    for gcc_command in gcc_commands:
        gcc_command = gcc_command.rstrip()
        commands.append({
            "command": gcc_command,
            "directory": os.path.join(os.getcwd(), LIBOPENCM3_SOURCE_DIR),
            "file": re.findall(r"[^\s]+\.c", gcc_command)[0],
            "output": re.findall(r"[^\s]+\.o", gcc_command)[0],
        })

    return commands


def get_project_commands() -> list[dict]:
    if not os.path.exists("build_commands.txt"):
        return []
    with open("build_commands.txt", "r") as f:
        gcc_commands = f.readlines()

    commands = []
    for gcc_command in gcc_commands:
        gcc_command = gcc_command.strip()
        if not gcc_command:
            continue

        file_match = re.search(r"\s-c\s+([^\s]+\.c)", gcc_command)
        output_match = re.search(r"\s-o\s+([^\s]+\.o)", gcc_command)

        if file_match and output_match:
            commands.append({
                "command": gcc_command,
                "directory": os.getcwd(),
                "file": file_match.group(1),
                "output": output_match.group(1),
            })
    return commands


def get_commands() -> list[dict]:
    commands = get_freertos_commands()
    commands.extend(get_libopencm3_commands())
    commands.extend(get_project_commands())

    return commands


def main():
    commands = get_commands()
    with open("compile_commands.json", "w") as f:
        f.write(json.dumps(commands, indent=4))


if __name__ == "__main__":
    main()
