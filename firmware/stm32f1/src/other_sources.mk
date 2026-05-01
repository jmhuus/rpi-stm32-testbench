# List of all .o object files, created from the source files
OBJECTS = $(SOURCES:.c=.o)

all: src/libother_sources.a

# Rule to link all the object files into the final executable
src/libother_sources.a: src/led/led.o
	arm-none-eabi-ar rcs $@ src/led/led.o

src/main.o:
	@echo "arm-none-eabi-gcc -ggdb3 -g -O0 -mcpu=cortex-m3 -mthumb -msoft-float -fno-common -ffunction-sections -fdata-sections -Wextra -Wshadow -Wno-unused-variable -Wimplicit-function-declaration -Wredundant-decls -Wstrict-prototypes -Wmissing-prototypes -MD -Wall -Wundef -I. -Iconfig -Iinclude/led -Ilib/freertos -Ilib/freertos/include -Ilib/freertos/portable/GCC/ARM_CM3 -Ilib/libopencm3/lib -DSTM32F1 -DSTM32F103C8 -Ilib/libopencm3/include -o src/main.o -c src/main.c" >> build_commands.txt
	arm-none-eabi-gcc \
	-ggdb3 \
	-g \
	-O0 \
	-mcpu=cortex-m3 \
	-mthumb \
	-msoft-float \
	-fno-common \
	-ffunction-sections \
	-fdata-sections \
	-Wextra \
	-Wshadow \
	-Wno-unused-variable \
	-Wimplicit-function-declaration \
	-Wredundant-decls \
	-Wstrict-prototypes \
	-Wmissing-prototypes  \
	-MD \
	-Wall \
	-Wundef \
	-I. \
	-Iconfig \
	-Iinclude/led \
	-Ilib/freertos \
	-Ilib/freertos/include \
	-Ilib/freertos/portable/GCC/ARM_CM3 \
	-Ilib/libopencm3/lib \
	-DSTM32F1 \
	-DSTM32F103C8 \
	-Ilib/libopencm3/include \
	-o src/main.o \
	-c src/main.c

src/led/led.o:
	@echo "arm-none-eabi-gcc -ggdb3 -g -O0 -mcpu=cortex-m3 -mthumb -msoft-float -fno-common -ffunction-sections -fdata-sections -Wextra -Wshadow -Wno-unused-variable -Wimplicit-function-declaration -Wredundant-decls -Wstrict-prototypes -Wmissing-prototypes -MD -Wall -Wundef -I. -Iconfig -Iinclude/led -Ilib/freertos -Ilib/freertos/include -Ilib/freertos/portable/GCC/ARM_CM3 -Ilib/libopencm3/lib -DSTM32F1 -DSTM32F103C8 -Ilib/libopencm3/include -o src/led/led.o -c src/led/led.c" >> build_commands.txt
	arm-none-eabi-gcc \
	-ggdb3 \
	-g \
	-O0 \
	-mcpu=cortex-m3 \
	-mthumb \
	-msoft-float \
	-fno-common \
	-ffunction-sections \
	-fdata-sections \
	-Wextra \
	-Wshadow \
	-Wno-unused-variable \
	-Wimplicit-function-declaration \
	-Wredundant-decls \
	-Wstrict-prototypes \
	-Wmissing-prototypes  \
	-MD \
	-Wall \
	-Wundef \
	-I. \
	-Iconfig \
	-Iinclude/led \
	-Ilib/freertos \
	-Ilib/freertos/include \
	-Ilib/freertos/portable/GCC/ARM_CM3 \
	-Ilib/libopencm3/lib \
	-DSTM32F1 \
	-DSTM32F103C8 \
	-Ilib/libopencm3/include \
	-o src/led/led.o \
	-c src/led/led.c

# # Rule to clean up all the generated files
# clean:
# 	rm -f $(OBJECTS) libother_sources.a
