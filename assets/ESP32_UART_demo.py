from machine import UART
import time

# Use UART2 (RX=GPIO16, TX=GPIO17) or change to your wiring
uart = UART(2, baudrate=9600, rx=16, tx=17)

print("ESP32 readySending LED toggle every 5 seconds and printing received potentiometer values...\n")

while True:
    if time.ticks_diff(time.ticks_ms(), last_send) >= 5000:
        uart.write(bytes([0xAA]))
        print("Sent: 0xAA")
        last_send = time.ticks_ms()

    if uart.any():
        byte = uart.read(1)
        if byte:
            print("Received:", byte[0])

    time.sleep(0.05)