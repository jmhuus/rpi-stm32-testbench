# Libopencm3 Details

### Build and Flash

1. `make`
1. `make flash`

### Clean

`make clean`

### Other Notes

#### How this Template was Created

1. `cd lib`
1. `git clone https://github.com/libopencm3/libopencm3 lib/libopencm3`
1. `cd lib/libopencm3/ && make TARGETS='stm32/f1'`

#### rules.mk

rules.mk came from the libopencm3-template example project

## FreeRTOS Details

### How FreeRTOS was included

1. `git clone https://github.com/FreeRTOS/FreeRTOS-Kernel.git lib/freertos`
1. Copy the FreeRTOSConfig.h config to lib/freertos/. See details below.
1. Comment out `#include "stm32f103_lib.h"` in the FreeRTOSConfig.h file.x
1. `cd lib/freertos`
1. `cmake .`
1. `make`
1. `cd ../../` back to the project directory
1. Include the following directories into the ./Makefile.INCLUDES

    - lib/freertos
    - lib/freertos/include
    - lib/freertos/portable/GCC/ARM_CM3

1. Set FreeRTOSConfig.h `configHEAP_CLEAR_MEMORY_ON_FREE` to 0
1. I also completely stripped the FreeRTOS library from files which were
   even remotely unrelated to simply compiling it using Make.

### FreeRTOS Config

The FreeRTOSConfig.h file is from here: FreeRTOS/Demo/CORTEX_STM32F103_Primer_GCC/FreeRTOSConfig.h
but requires major tweaking.

Specifically, I made the following changes:

   - Add `#define configAssert...` and it's handler. This is an interrupt handler that is called
	  when a config is improperly set up.
	  
   - Add the vAssertCalled extern function to the FreeRTOSConfig header.
   - Add the vAssertCalled definition to the main.c file.
   - Add `#define vPortSVCHandler sv_call_handler` so that FreeRTOS can override the libopencm3 weak definitions for this interrupt handler
   - Add `#define xPortPendSVHandler pend_sv_handler` so that FreeRTOS can override the libopencm3 weak definitions for this interrupt handler
   - Add `#define xPortSysTickHandler sys_tick_handler` so that FreeRTOS can override the libopencm3 weak definitions for this interrupt handler
   - Add `#define configPRIO_BITS 4` to set the number of priority bits. I'm still not familiar with that these priority bits mean.
   - Update `configMAX_SYSCALL_INTERRUPT_PRIORITY` to 176 so that the four LSB are 0.

### CMake

The following updates were made to the lib/freertos/CMakeLists.txt file:

- Add project(project_template_with_makefile) near the top of the file
- Add the following code to specify the freertos config:

```
add_library(freertos_config INTERFACE)
target_include_directories(freertos_config SYSTEM
  INTERFACE
  "./FreeRTOSConfig.h") # The config file directory
target_compile_definitions(freertos_config
  INTERFACE
  projCOVERAGE_TEST=0)
```

## How to use Debugger (OpenOCD)

1. Start OpenOCD debug server

Command:
```
openocd -f interface/stlink.cfg -f target/stm32f1x.cfg
```

Yasnippet Key:
```
opengdb
```

1. (New terminal) Start GDB client

Start a new GDB-multiarch client.

Command:
```
gdb-multiarch your_binary.elf
```

Yasnippet Key:
```
gdbm
```

1. Connect to OpenOCD debug server

Command:
```
target extended-remote :[port number]
```

Yasnippet Key:
```
tgter
```

1. Set breakpoint

Command:
```
b main
```
