import numpy as np

class Neuroid:
    def __init__(self, umbr, beta, kr, maxcount):
        self.umbr = umbr
        self.beta = beta
        self.kr = kr
        self.maxcount = maxcount

        self.count1 = 0
        self.count2 = 0

        self.y = 0
        self.nt_out = 0

    @staticmethod
    def calc_weight_sum(inputs, weights):
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * weights[i]
        return sum

    def run_comparator(self, inputs, weights):
        weighted_sum = sum([w * i for w in weights for i in inputs])

        if weighted_sum >= self.umbr:
            if self.count1 > self.beta / (weighted_sum - self.umbr):
                self.count1 = 0
            else:
                self.count1 += 1
        else:
            self.count1 = 0


    def run_freq_modulator(self):
        if self.count1 == 1:
            self.y = 1
        else:
            self.y = 0

    def run_freq_demodulator(self):
        if self.y == 1:
            self.nt_out = self.kr * (1 / self.count2)
            self.count2 = 0
        else:
            self.count2 = self.count1 + 1

        if self.count2 > self.maxcount:
            self.count2 = 0

    def run_neuroid(self, inputs, weights):
        if len(inputs) != len(weights):
            raise Exception("Size of inputs and size of weights must be the same!")

        for i in range(len(weights) - self.maxcount):
            self.run_comparator(inputs[i:(i + self.maxcount)], weights[i:(i + self.maxcount)])
            self.run_freq_modulator()
            self.run_freq_demodulator()
            print(self.nt_out)


def main():
    inputs = [1, 1, 1, 1, 1]
    weights = [1, 1, 1, 1, 1]

    neuroid = Neuroid(umbr=0.1, beta=1.25, kr=2.1, maxcount=24, logging=True)
    neuroid.run_neuroid(inputs, weights)


if __name__ == "__main__":
    main()
