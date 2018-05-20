class CallbackDemo:
    items = []
    index = 0
    gpio_service = None

    def __init__(self):
        self.items = [None] * 3
        self.items[0] = 1
        self.items[1] = 2
        self.items[2] = 3

    def on_left_click(self):
        self.index -= 1
        print("Left click, index: " + str(self.index))
        if self.index < 0:
            self.index = 2

    def on_right_click(self):
        self.index += 1
        print("Right click, index: " + str(self.index))
        if self.index > 2:
            self.index = 0


def test(callback):
    # print(callback.func_name)
    callback()


cd = CallbackDemo()
test(cd.on_left_click)
test(cd.on_left_click)
test(cd.on_left_click)
test(cd.on_right_click)
test(cd.on_right_click)
test(cd.on_right_click)
test(cd.on_right_click)

