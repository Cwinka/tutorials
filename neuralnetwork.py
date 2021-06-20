import random
import numpy as np

class NeuralNetwork:
    def __init__(self, learning_rate=0.1):
        self.weights_0_1 = np.random.normal(0.0, 2**-0.5, (2,6))
        self.weights_1_2 = np.random.normal(0.0, 1, (1,2))
        self.sigmoid_map = np.vectorize(self.sigmoid)
        self.learning_rate = np.array([learning_rate])

    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))

    def predict(self, inputs):
        inputs_1 = np.dot(self.weights_0_1, inputs)
        output_1 = self.sigmoid_map(inputs_1)

        inputs_2 = np.dot(self.weights_1_2, output_1)
        output_2 = self.sigmoid_map(inputs_2)
        return output_2

    def train(self, inputs, expected_predict):
        inputs = np.array(inputs)
        inputs_1 = np.dot(self.weights_0_1, inputs)
        output_1 = self.sigmoid_map(inputs_1)

        inputs_2 = np.dot(self.weights_1_2, output_1)
        output_2 = self.sigmoid_map(inputs_2)
        actual_predict = output_2[0]

        error_layer_2 = np.array([actual_predict - expected_predict])
        gradient_layer_2 = actual_predict * (1 - actual_predict)
        weights_delta_layer_2 = gradient_layer_2 * error_layer_2
        self.weights_1_2 -= np.dot(weights_delta_layer_2, output_1.reshape(1, len(output_1)) * self.learning_rate)

        error_layer_1 = self.weights_1_2 * weights_delta_layer_2
        gradient_layer_1 = output_1 * (1 - output_1)
        weights_delta_layer_1 = gradient_layer_1 * error_layer_1
        self.weights_0_1 -= np.dot(inputs.reshape(len(inputs), 1), weights_delta_layer_1).T * self.learning_rate

train_set = (
    ([1,1,1,1,1,50], 1), #  move to ....
    # ([1,0,1,1,1,50], 0), # ... move to ....
    # ([1,1,1,0,1,30], 0.8), # make ...
    # ([1,1,1,0], 1),
    # ([1,1,0,0], 0),
    # ([0,1,0,0], 0),
    # ([0,0,0,0], 0),
    # ([1,0,0,1], 0),
)
def MSE(y, Y):
    return np.mean((y-Y)**2)
epochs = 6000
learning_rate = 0.01
n = NeuralNetwork(learning_rate)
for i in range(1,epochs+1):
    inputs_ = []
    correct_pred = []
    for input, expect in train_set:
        n.train(input, expect)
        inputs_.append(np.array(input))
        correct_pred.append(np.array(expect))
    train_loss = MSE(n.predict(np.array(inputs_).T), np.array(correct_pred))
    print(f"Progress: {i}, Training loss: {str(train_loss)[:5]}")
print(n.weights_0_1)
print(n.weights_1_2)
