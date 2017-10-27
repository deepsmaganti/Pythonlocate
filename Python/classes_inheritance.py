class inputs:
    def __init__(self,a,b):
        self.a = a
        self.b = b

class calculator(inputs):
    def __init__(self, a, b, operation):
        inputs.__init__(self, a, b)
        self.operation = operation
        if self.operation == 'addition':
            self.out = int(a + b)
            print self.out
        elif self.operation == 'subtract':
            self.out = int(a - b)
            print self.out
        elif self.operation == 'multiply':
            self.out = int(a * b)
            print self.out
        elif self.operation == 'divide':
            self.out = float(a / b)
            print self.out
        elif self.operation == 'average':
            self.out = float(a + b)/2
            print self.out

calculator(23, 65, 'addition')
calculator(52525, 45764, 'subtract')
calculator(345,43,'multiply')
calculator(34656,9765,'divide')
calculator(5346,6869678,'average')
