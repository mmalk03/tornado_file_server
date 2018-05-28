import signal

LED_BLUE = 11
LED_GREEN = 16
LED_RED = 18
LED_WHITE = 12

BUTTON_UPPER = 13
BUTTON_LEFT = 19
BUTTON_RIGHT = 15

BOUNCE_TIME = 1000


class GpioService:
    current_diode = 0
    pin_statuses = {LED_BLUE: 0, LED_GREEN: 0, LED_RED: 0, LED_WHITE: 0, }

    def __init__(self):
        print('Starting gpio service')

    @staticmethod
    def register_on_upper_click(callback):
        print('Registering on_upper_click')
        signal.signal(signal.SIGINT, callback)

    @staticmethod
    def register_on_left_click(callback):
        print('Registering on_left_click')
        signal.signal(signal.SIGUSR1, callback)

    @staticmethod
    def register_on_right_click(callback):
        print('Registering on_right_click')
        signal.signal(signal.SIGUSR2, callback)

    def select_blue(self):
        self.switch_diode(LED_BLUE)

    def select_green(self):
        self.switch_diode(LED_GREEN)

    def select_red(self):
        self.switch_diode(LED_RED)

    def select_white(self):
        self.switch_diode(LED_WHITE)

    def switch_diode(self, pin_number):
        if self.current_diode != 0:
            self.switch_off(self.current_diode)
        self.current_diode = pin_number
        self.switch_on(pin_number)

    @staticmethod
    def cleanup():
        print('Cleanup')

    def switch_on(self, pin_number):
        print(f'Pin number {pin_number} on')
        self.pin_statuses[pin_number] = 1

    def switch_off(self, pin_number):
        print(f'Pin number {pin_number} off')
        self.pin_statuses[pin_number] = 0

    def get_pin_value(self, pin_number):
        return self.pin_statuses[pin_number]
