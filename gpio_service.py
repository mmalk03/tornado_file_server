import RPi.GPIO as GPIO

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

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        led_list = [LED_BLUE, LED_GREEN, LED_RED, LED_WHITE]
        GPIO.setup(led_list, GPIO.OUT)
        GPIO.output(led_list, GPIO.LOW)

        button_list = [BUTTON_LEFT, BUTTON_RIGHT, BUTTON_UPPER]
        GPIO.setup(button_list, GPIO.IN)

    @staticmethod
    def register_on_upper_click(callback):
        GPIO.add_event_detect(BUTTON_UPPER, GPIO.RISING, callback=callback, bouncetime=BOUNCE_TIME)

    @staticmethod
    def register_on_left_click(callback):
        GPIO.add_event_detect(BUTTON_LEFT, GPIO.RISING, callback=callback, bouncetime=BOUNCE_TIME)

    @staticmethod
    def register_on_right_click(callback):
        GPIO.add_event_detect(BUTTON_RIGHT, GPIO.RISING, callback=callback, bouncetime=BOUNCE_TIME)

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
        GPIO.cleanup()

    @staticmethod
    def switch_on(pin_number):
        GPIO.output(pin_number, GPIO.HIGH)

        # bash_command = "gpio set " + pin_number
        # process = subprocess.Popen(bash_command.split())
        # output, error = process.communicate()

        # open('/sys/class/gpio/gpio' + str(pin_number) + '/value', 'w').write(1)

    @staticmethod
    def switch_off(pin_number):
        GPIO.output(pin_number, GPIO.LOW)

        # bash_command = "gpio clear " + str(pin_number)
        # process = subprocess.Popen(bash_command.split())
        # output, error = process.communicate()

        # open('/sys/class/gpio/gpio' + str(pin_number) + '/value', 'w').write(0)

    @staticmethod
    def get_pin_value(pin_number):
        return GPIO.input(pin_number)

        # bash_command = "gpio read " + str(pin_number)
        # process = subprocess.Popen(bash_command.split())
        # output, error = process.communicate()
        # return int(output)

        # return int(open('/sys/class/gpio/gpio' + str(pin_number) + '/value', 'r').read())
