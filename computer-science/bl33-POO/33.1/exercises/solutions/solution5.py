class tv:
    def __init__(self, marca, valor=0):
        self.state = 'off'
        self.marca = marca
        self.valor = valor

    def power_on_off(self):
        if self.state == 'off':
            self.state = 'on'
        else:
            self.state = 'off'
