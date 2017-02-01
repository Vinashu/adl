from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        # Seed the random number generator, so it generates the same numbers
        # every time the program runs.
        random.seed(1)

        #We model a single neuron, with 3 input connections and 1 output connection.
        #we assing randon weights to a 3 x 1 matrix, with values  in the range -1 to 1
        #and mean 0
        self.synaptic_weights = 2 * random.random((3,1)) - 1

    #The sigmoid function, which describes as s sharped curve
    #we pass the wighted sum of the inputs through this function
    #to normalise them betwenn 0 and 1
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            #pass the training set through our neu
            output = self.predict(training_set_inputs)

            # Calculate the error (The difference between the desired output
            # and the predicted output).
            error = training_set_outputs - output

            # Multiply the error by the input and again by the gradient of the Sigmoid curve.
            # This means less confident weights are adjusted more.
            # This means inputs, which are zero, do not cause changes to the weights.
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            #adjustment the weights
            self.synaptic_weights += adjustment
    
    # The neural network thinks.
    def predict(self, inputs):
        #pass inputs through our neural network (our single neuron)
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

if __name__ == "__main__":
    #Initialise a single neuron neural netowork.
    neural_network = NeuralNetwork()

    print ("Random starting synaptic weights: ")
    print (neural_network.synaptic_weights)

    #The training set. We have 4 examples, each consisting of 3 input values
    #and 1 output value.abs
    training_set_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    training_set_outputs = array([[0,1,1,0]]).T

    #Train the neural network using a training set.
    #Do it 10,000 times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print ("Neu synapitc weights after training: ")
    print (neural_network.synaptic_weights
)
    #Test the nerual network with a new situation. 
    print ("Considering new situation [1,0,0] -> ?: ")
    print (neural_network.thing(array([1,0,0])))