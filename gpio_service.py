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

        GPIO.setup(LED_RED, GPIO.OUT)
        GPIO.setup(LED_GREEN, GPIO.OUT)
        GPIO.setup(LED_WHITE, GPIO.OUT)
        GPIO.setup(LED_BLUE, GPIO.OUT)

        GPIO.setup(BUTTON_UPPER, GPIO.IN)
        GPIO.setup(BUTTON_LEFT, GPIO.IN)
        GPIO.setup(BUTTON_RIGHT, GPIO.IN)

        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.LOW)
        GPIO.output(LED_WHITE, GPIO.LOW)
        GPIO.output(LED_BLUE, GPIO.LOW)

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
    def switch_on(pin_number):
        GPIO.output(pin_number, GPIO.HIGH)

        # bash_command = "gpio set " + pin_number
        # process = subprocess.Popen(bash_command.split())
        # output, error = process.communicate()

        # open('/sys/class/gpio/gpio' + str(pin_number) + '/value', 'w').write(1)

    @staticmethod
    def switch_off(pin_number):
        GPIO.output(pin_number, GPIO.HIGH)

        # bash_command = "gpio clear " + str(pin_number)
        # process = subprocess.Popen(bash_command.split())
        # output, error = process.communicate()

        # open('/sys/class/gpio/gpio' + str(pin_number) + '/value', 'w').write(0)

    @staticmethod
    def get_pin_value(pin_number):
        pass
        # bash_command = "gpio read " + str(pin_number)
        # process = subprocess.Popen(bash_command.split())
        # output, error = process.communicate()
        # return int(output)

        # return int(open('/sys/class/gpio/gpio' + str(pin_number) + '/value', 'r').read())
