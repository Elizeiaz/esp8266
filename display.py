from machine import I2C
import ssd1306

WIDTH = 128
HEIGHT = 64

class Display:
    """Display on I2C"""

    def __init__(self, i2c: I2C, width=WIDTH, height=HEIGHT):
        self.display = ssd1306.SSD1306_I2C(width, height, i2c)

    def show_text(self, text: str):
        pass

    # Show important information on the top of display
    def show_info(self, text: str):
        self.display.fill(0)
        self.display.text(text, 0, 0)
        self.display.show()

    # Need to refactor
    def show_data(self, data: str):
        data_arr = data.split(';')
        self.display.fill(0)
        self.display.text(f'{data_arr[0]}', 0, 0)
        self.display.text(f'CPU:  {data_arr[1]}%', 6, 16)
        self.display.text(f'MEM:  {data_arr[2]}%', 6, 24)
        self.display.text(f'BAT:  {data_arr[3]}%', 6, 32)
        self.display.show()
