from typing import Final
import pyvisa
import time


SCOPE_ADDRESS: Final[str] = "192.168.0.21"
SCOPE_SCPI_SOCKET_PORT: Final[int] = 5555


resource_manager = pyvisa.ResourceManager("@py")

print("Scanning for devices...")
resources = resource_manager.list_resources()
print(f"Found: {resources}")

TCP_IP_STRING = f"TCPIP::{SCOPE_ADDRESS}::INSTR"
try:
    scope = resource_manager.open_resource(TCP_IP_STRING)
    scope.timeout = 5000

    idn_response = scope.query("*IDN?")
    print(f"Connected to {idn_response.strip()}")

    print("Sending setup commands....")
    scope.write(":SYST:BEEP ON")
    for _ in range(10):
        scope.write(":SYST:BEEP")
        scope.query("*OPC?")
        time.sleep(1)
    # scope.write(":CHAN1:DISP ON")
    # scope.write(":CHAN1:SCAL 1.0")
    # scope.write(":TIM:SCAL 0.001")

    print("Scope is ready.")

except Exception as e:
    print(
        f"Error:\n{e}"
    )

finally:
    try:
        scope.close()
    except:
        pass

    resource_manager.close()
