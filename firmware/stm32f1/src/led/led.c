#include "FreeRTOS.h"
#include "led.h"

#include <libopencm3/cm3/common.h>
#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>

void set_up_built_in_led() {
  // Enable clock for GPIO channel A
  rcc_periph_clock_enable(RCC_GPIOA);

  // Set pinmode for PC13
  gpio_set_mode(
		GPIOA,
		GPIO_MODE_OUTPUT_2_MHZ,
		GPIO_CNF_OUTPUT_PUSHPULL,
		GPIO12);

  // Turn LED off
  gpio_set(GPIOA, GPIO12);
}
