# FreeRTOS Library for STM32F103C8 Projects


Add this library as a git submodule:
```shell
git -c protocol.file.allow=always \
submodule add \
~/Documents/engineering/computer_engineering/LIBRARY_FreeRTOS/freertos_library/`
libs/freertos
```


The following things were done to create this directory.

1. Clone the FreeRTOS Kernel.
   `git clone https://github.com/FreeRTOS/FreeRTOS-Kernel.git`
   
1. Remove unnecessary files.
  - CMakeLists.txt
  - cspell.config.yaml
  - examples
  - .git
  - .gitattributes
  - .git-blame-ignore-revs
  - .github
  - GitHub-FreeRTOS-Kernel-Home.url
  - .gitmodules
  - History.txt
  - LICENSE.md
  - MISRA.md
  - Quick_Start_Guide.url
  - README.md
  
  ```shell
  rm -rf CMakeLists.txt \
	  cspell.config.yaml \
	  examples \
	  .git \
	  .gitattributes \
	  .git-blame-ignore-revs \
	  .github \
	  GitHub-FreeRTOS-Kernel-Home.url \
	  .gitmodules \
	  History.txt \
	  LICENSE.md \
	  MISRA.md \
	  Quick_Start_Guide.url \
	  README.md
  ```

1. Add a FreeRTOSConfig.h file.

1. Add the following Makefile

```
# List of all .c source files
SOURCES += $(wildcard *.c)
SOURCES += $(wildcard include/*.c)
SOURCES += $(wildcard portable/Common/*.c)
SOURCES += $(wildcard portable/MemMang/heap_4.c)
SOURCES += $(wildcard portable/GCC/ARM_CM3/*.c)

# FreeRTOS dirs to create .o files from
OBJ_CREATION_FREERTOS_INCLUDE_DIRS += .
OBJ_CREATION_FREERTOS_INCLUDE_DIRS += include/
OBJ_CREATION_FREERTOS_INCLUDE_DIRS += portable/Common/
OBJ_CREATION_FREERTOS_INCLUDE_DIRS += portable/MemMang/
OBJ_CREATION_FREERTOS_INCLUDE_DIRS += portable/GCC/ARM_CM3/
OBJ_CREATION_FREERTOS_INCLUDES = $(patsubst %,-I%, $(OBJ_CREATION_FREERTOS_INCLUDE_DIRS))

# FreeRTOS flags for object file creation, specific to the STM32F1
OBJ_CREATION_FREERTOS_FLAGSS = ggdb3
OBJ_CREATION_FREERTOS_FLAGSS += mcpu=cortex-m3
OBJ_CREATION_FREERTOS_FLAGSS += mthumb
OBJ_CREATION_FREERTOS_FLAGSS += msoft-float
OBJ_CREATION_FREERTOS_FLAGSS += fno-common
OBJ_CREATION_FREERTOS_FLAGSS += ffunction-sections
OBJ_CREATION_FREERTOS_FLAGSS += fdata-sections
OBJ_CREATION_FREERTOS_FLAGSS += Wextra
OBJ_CREATION_FREERTOS_FLAGSS += Wshadow
OBJ_CREATION_FREERTOS_FLAGSS += Wno-unused-variable
OBJ_CREATION_FREERTOS_FLAGSS += Wimplicit-function-declaration
OBJ_CREATION_FREERTOS_FLAGSS += Wredundant-decls
OBJ_CREATION_FREERTOS_FLAGSS += Wstrict-prototypes
OBJ_CREATION_FREERTOS_FLAGSS += Wmissing-prototypes
OBJ_CREATION_FREERTOS_FLAGS = $(patsubst %,-%, $(OBJ_CREATION_FREERTOS_FLAGSS))

# List of all .o object files, created from the source files
OBJECTS = $(SOURCES:.c=.o)

# Rule to link all the object files into the final executable
# 
libfreertos_kernel.a: $(OBJECTS)
	arm-none-eabi-ar rcs $@ $(OBJECTS)

# Rule to compile a .c file into a .o file
%.o: %.c
	echo $(SOURCES)
	echo "arm-none-eabi-gcc $(OBJ_CREATION_FREERTOS_FLAGS) $(OBJ_CREATION_FREERTOS_INCLUDES) -c $< -o $@" >> build_commands.txt
	arm-none-eabi-gcc $(OBJ_CREATION_FREERTOS_FLAGS) $(OBJ_CREATION_FREERTOS_INCLUDES) -c $< -o $@

# Rule to clean up all the generated files
clean:
	rm -f $(OBJECTS) libfreertos_kernel.a portable/MemMang/*.o build_commands.txt
```

1. Run make.
   `make`
