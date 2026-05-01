#include "FreeRTOS.h"
#include "task.h"
#include "led.h"

#include <libopencm3/cm3/common.h>
#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>
#include <libopencm3/stm32/dbgmcu.h>
#include <libopencm3/stm32/iwdg.h>
#include <libopencm3/cm3/vector.h>

/*
 * Handler in case our application overflows the stack
 */
void vApplicationStackOverflowHook(TaskHandle_t xTask __attribute__((unused)),
                                   char *pcTaskName __attribute__((unused))) {
  taskDISABLE_INTERRUPTS();
  // TODO(jordanhuus): Attempt to collect high water mark data and log
  // those details.
  // TODO(jordanhuus): Implement a serial message that the offending task
  // exceeded the task stack depth.
  for (;;);
}

void vAssertCalled( const char * pcFile, unsigned long ulLine )
{
    volatile unsigned long ul = 0;

    ( void ) pcFile;
    ( void ) ulLine;

    taskDISABLE_INTERRUPTS();
    for( ;; )
    {
        /* An assertion has failed. The file name and line number are passed in the
        pcFile and ulLine parameters. Use a debugger to inspect these values. */
        ul++;
    }
}

/*
 * Task that toggles PC13, which is the LED
 */
static void task1(void *args __attribute__((unused))) {
  for (;;) {
    // Turn LED on
    gpio_toggle(GPIOA, GPIO12);
    vTaskDelay(pdMS_TO_TICKS(50));
  }
}

/*
 * Main loop, this is where our program starts
 */
int main(void) {
  // Setup main clock, using external 8MHz crystal
  rcc_clock_setup_in_hse_8mhz_out_72mhz();
  set_up_built_in_led();

  // Tell FreeRTOS about our toggle task, and set it's stack and priority
  xTaskCreate(task1, "LED", 100, NULL, 2, NULL);

  // Start RTOS Task scheduler
  vTaskStartScheduler();

  for (;;);
  return 0;
  
}
