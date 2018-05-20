import subprocess


class MusicHandler:
    def switch_on(self, pin_number):
        bash_command = "gpio set " + pin_number
        process = subprocess.Popen(bash_command.split())
        output, error = process.communicate()
        # open('/sys/class/gpio/gpio' + str(pin_number) + '/value', 'w').write(1)

    def switch_off(self, pin_number):
        bash_command = "gpio clear " + str(pin_number)
        process = subprocess.Popen(bash_command.split())
        output, error = process.communicate()
        # open('/sys/class/gpio/gpio' + str(pin_number) + '/value', 'w').write(0)

    def get_pin_value(self, pin_number):
        bash_command = "gpio read " + str(pin_number)
        process = subprocess.Popen(bash_command.split())
        output, error = process.communicate()
        return int(output)
        # return int(open('/sys/class/gpio/gpio' + str(pin_number) + '/value', 'r').read())
