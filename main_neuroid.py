import numpy as np
from neuron import Neuron


def main():
    neuron = Neuron(4)

    """
    1. (0, 1, 1, 1) -> 0
    2. (1, 0, 1, 0) -> 1
    3. (1, 0, 0, 0) -> 1
    4. (1, 1, 1, 1) -> 0
    Arrays that most resemble the 2 and 3 will give numbers closer to 1.
    NOTE: Doesn't provide much valuable info due to being just 4 inputs and one neuron.
    """

    inputs = np.array([[0, 1, 1, 1],
                       [1, 0, 1, 0],
                       [1, 0, 0, 0],
                       [1, 1, 1, 1]])
    labels = np.array([[0, 1, 1, 0]]).T
    neuron.train(inputs, labels, 20000)

    test_input = np.array([1, 0, 1, 1])
    prediction = neuron.predict(test_input)
    print(prediction)


if __name__ == '__main__':
    main()
