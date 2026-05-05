from typing import Final
import pyvisa
import time
import logging


SCOPE_IP_ADDRESS: Final[str] = "192.168.0.21"
TCP_IP_STRING: Final[str] = f"TCPIP::{SCOPE_IP_ADDRESS}::INSTR"
SCOPE_SCPI_SOCKET_PORT: Final[int] = 5555


logging.basicConfig(
    filename="logs/scope_utils.log",
    filemode="w",
    level=logging.INFO
)


class Scope:

    def __init__(self, tcp_ip_address: str):
        self.tcp_ip_address = tcp_ip_address

    def __enter__(self):
        logging.info("Scanning for devices...")
        self.resource_manager = pyvisa.ResourceManager("@py")
        resources = self.resource_manager.list_resources()
        logging.info(f"Found: {resources}")

        self.scope = self.resource_manager.open_resource(self.tcp_ip_address)
        self.scope.timeout = 5000
        idn_response = self.scope.query("*IDN?")
        logging.info(f"Connected to {idn_response.strip()}")
        logging.info("Sending setup commands....")
        self.scope.write(":CHAN1:DISP ON")
        self.scope.write(":CHAN1:SCAL 1.0")
        self.scope.write(":TIM:SCAL 0.03")

        return self
            
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            logging.info(f"({self.tcp_ip_address}) Scope exited normally.")
        else:
            self.scope.close()
            self.resource_manager.close()

        return False

    def measure_pulse_width_ms(self) -> float:
        """Returns the duration of the positive pulse (duty cycle) in milliseconds."""
        self.scope.write(':TRIGger:EDGE:SOURce CHANnel1')
        self.scope.write(':TRIGger:EDGE:LEVel 1.65')
        self.scope.query('*OPC?')

        # PWIDth queries the positive pulse width instead of the percentage
        raw_val = self.scope.query(":MEASure:ITEM? PWIDth,CHANnel1")

        return float(raw_val) * 1000
