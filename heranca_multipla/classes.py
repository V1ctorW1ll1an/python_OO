class Electronics:
    def __init__(self, name):
        self._name = name
        self._on = False

    def turns_on(self):
        if self._on:
            return
        self._on = True
        print(f'{self._name} is on now!')

    def turns_off(self):
        if not self._on:
            return
        self._on = False
        print(f'{self._name} is off now!')


class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as file:
            file.write(msg)
            file.write('\n')

    def log_info(self, msg):
        self.write(f'INFO:  {msg}')

    def log_error(self, msg):
        self.write(f'ERROR:  {msg}')


class Smartphone(Electronics, LogMixin):
    def __init__(self, name):
        super().__init__(name)
        self._connected = False

    def connect(self):
        if not self._on:
            error = f'{self._name} is off'
            print(error)
            self.log_error(error)
            return
        if self._connected:
            error_msg = f'{self._name} already connected'
            print(error_msg)
            self.log_error(error_msg)
            return
        self._connected = True
        info = f'{self._name} is connect now'
        print(info)
        self.log_info(info)

    def disconnect(self):
        if not self._connected:
            error_msg = f'{self._name} is not connected'
            print(error_msg)
            self.log_error(error_msg)
            return
        self._connected = False
        info = f'{self._name} is disconnect now'
        print(info)
        self.log_info(info)
