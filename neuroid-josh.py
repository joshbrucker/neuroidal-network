import numpy as np


class Neuroid:
    def __init__(self):
        self.umbr = 2
        self.beta = 2
        self.kr = 2
        self.maxcount = 2

        self.count1 = 0
        self.count2 = 0

        self.y = 0
        self.nt_out = 0

    def run_comparator(self, inputs, weights):
        weighted_sum = sum([w * i for w in weights for i in inputs])
        if weighted_sum >= self.umbr:
            if self.count1 > self.beta / (weighted_sum - self.umbr):
                self.count1 = 0
            else:
                self.count1 += 1
        else:
            self.count1 = 0

    def run_pulse_freq_modulator(self):
        if self.count1 == 1:
            self.y = 1
        else:
            self.y = 0

    # TODO: write the frequency demodulator
    def run_freq_demodulator(self):
        pass

    def run_neuroid(self, inputs, weights):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
