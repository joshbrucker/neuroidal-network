from neuroid_testing.neuroid import Neuroid


def main():
    # inputs = [0.1, 0.2, 0.4, 0.5, 0.6, 0.7, 0.6, 0.5, 0.4, 0.2, 0.2]
    # weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    inputs = [0.1, 0.3, 0.5, -0.2, -0.1, -0.3, 0.4, 0.8, -0.3, -0.9, 0.2, 0.5, 0.9, -0.1, -0.4, 0.2, 0.1, -0.2, -0.1]
    weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    neuroid = Neuroid(umbr=0.1, beta=1.25, kr=2.1, maxcount=2, log=True)
    neuroid.run_neuroid(inputs, weights)

    print("y values:     ", neuroid.y_stream)
    print("count1 values:", neuroid.count1_stream)
    print("count2 values:", neuroid.count2_stream)
    print("nt_out values:", neuroid.nt_out_stream)


if __name__ == "__main__":
    main()
