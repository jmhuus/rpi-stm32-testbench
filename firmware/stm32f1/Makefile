FREERTOS_DIR 	= lib/freertos
OPENCM3_DIR 	= lib/libopencm3
BUILD_DIR 	= bin
FREERTOS_DIRS 	:= lib/freertos lib/freertos/include lib/freertos/portable/GCC/ARM_CM3
OPENCM3_DIR 	= lib/libopencm3
CFILES 		= src/main.c
DEVICE		= stm32f103c8
VPATH += $(SHARED_DIR)
OPENCM3_DEVICE_TARGET 	= stm32/f1
CPP 		= arm-none-eabi-gcc

include src/other_sources.mk
include lib/libopencm3/mk/genlink-config.mk
include lib/libopencm3/mk/genlink-rules.mk

lib/freertos/libfreertos_kernel.a:
	make -C $(FREERTOS_DIR)

lib/libopencm3/lib/libopencm3_stm32f1.a:
	make -C $(OPENCM3_DIR) TARGETS=$(OPENCM3_DEVICE_TARGET)

libopencm3_freertos_template.elf: clean_ldscript $(LDSCRIPT) src/main.o src/libother_sources.a
	arm-none-eabi-gcc \
	-T$(LDSCRIPT) \
	-Llib/libopencm3/lib \
	-nostartfiles \
	-mcpu=cortex-m3 \
	-mthumb \
	-msoft-float \
	-specs=nano.specs \
	-Wl,--gc-sections \
	-Lsrc \
	-Llib/freertos \
	-Llib/libopencm3/lib \
	src/main.o   \
	-lother_sources \
	-lfreertos_kernel \
	-lopencm3_stm32f1 \
	-Wl,--start-group \
	-lc \
	-lgcc \
	-lnosys \
	-Wl,--end-group \
	-o libopencm3_freertos_template.elf

libopencm3_freertos_template.bin: libopencm3_freertos_template.elf
	arm-none-eabi-objcopy \
	-O \
	binary  \
	libopencm3_freertos_template.elf \
	libopencm3_freertos_template.bin

flash: 	lib/freertos/libfreertos_kernel.a \
	lib/libopencm3/lib/libopencm3_stm32f1.a \
	src/libother_sources.a \
	libopencm3_freertos_template.bin
	st-flash --reset write libopencm3_freertos_template.bin 0x8000000

clangd_db:
	rm -f build_commands.txt
	make lib/freertos/libfreertos_kernel.a
	make lib/libopencm3/lib/libopencm3_stm32f1.a
	rm -f src/main.o src/led/led.o src/steppers/steppers.o src/libother_sources.a
	make src/main.o src/libother_sources.a
	python3 compile_commands.py

.PHONY: flash clean_ldscript


clean_ldscript:
	rm -f $(LDSCRIPT)

clean:
	make -C $(OPENCM3_DIR) clean
	make -C $(FREERTOS_DIR) clean
	rm \
	-rf \
	*.elf \
	*.bin \
	src/*.a \
	src/*.o \
	src/*.d \
	src/led/*.d \
	src/led/*.o
