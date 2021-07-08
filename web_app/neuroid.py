import numpy as np

class Neuroid:
    def __init__(self, umbr, beta, kr, maxcount, log=False):
        self.log = log

        self.umbr = umbr
        self.beta = beta
        self.kr = kr
        self.maxcount = maxcount

        self.count1 = 0
        self.count2 = 0

        self.y = 0
        self.nt_out = 0
        self.time = 0

        self.count1_stream = []
        self.count2_stream = []
        self.y_stream = []
        self.nt_out_stream = []

    @staticmethod
    def calc_weight_sum(inputs, weights):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * weights[i]
        return sum

    def run_comparator(self, inputs, weights):
        weighted_sum = self.calc_weight_sum(inputs, weights)

        if weighted_sum >= self.umbr:
            if self.count1 > self.beta / (weighted_sum - self.umbr):
                self.count1 = 0
            else:
                self.count1 += 1
        else:
            self.count1 = 0

        self.count1_stream.append(self.count1)


    def run_freq_modulator(self):
        if self.count1 == 1:
            self.y = 1
        else:
            self.y = 0

        self.y_stream.append(self.y)

    def run_freq_demodulator(self):
        if self.y == 1:
            if self.count2 == 0:
                print("divide by zero in demodulator")
            else:
                self.nt_out = self.kr * (1 / self.count2)
                self.count2 = 0
        else:
            self.count2 = self.count1 + 1

        if self.count2 > self.maxcount:
            self.count2 = 0

        self.count2_stream.append(self.count2)
        self.nt_out_stream.append(self.nt_out)

    def run_neuroid(self, inputs, weights):
        if len(inputs) != len(weights):
            raise Exception("Size of inputs and size of weights must be the same!")

        for i in range(len(weights) - self.maxcount):
            self.run_comparator(inputs[i:(i + self.maxcount)], weights[i:(i + self.maxcount)])
            self.run_freq_modulator()
            self.run_freq_demodulator()
            self.time += 1

            if self.log:
                print("======= Time", self.time, "=======")
                print("nt_out =", self.nt_out)
                print("y =", self.y)
                print("count1 =", self.count1)
                print("count2 =", self.count2)
                print()


def run(umbr, beta, kr, maxcount, log=False):
    inputs = [0.0, 0.1, 0.3, 0.5, -0.2, -0.1, -0.3, 0.4, 0.8, -0.3, -0.9, 0.2, 0.5, 0.9, -0.1, -0.4, 0.2, 0.1, -0.2, -.1]
    weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    neuroid = Neuroid(umbr=umbr, beta=beta, kr=kr, maxcount=maxcount, log=log)
    neuroid.run_neuroid(inputs, weights)

    if log:
        print("y values:     ", neuroid.y_stream)
        print("count1 values:", neuroid.count1_stream)
        print("count2 values:", neuroid.count2_stream)
        print("nt_out values:", neuroid.nt_out_stream)

    return {"output": neuroid.nt_out}
