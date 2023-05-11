# AY - exploring a vague idea - placeholder script - what would modeling intuition look like

# Modeling intuition, or "gut feelings", using neurons is a complex task that involves concepts from artificial intelligence, specifically from the field of neural networks. Intuition, as we understand it in humans, is a form of decision-making that doesn't rely on explicit reasoning, but instead on learned patterns from past experiences. In the field of artificial intelligence, this can be simulated through machine learning algorithms that learn patterns from data.

# In terms of neural networks, the concept of intuition can be related to the learned weights of a trained network. Once the network is trained on a certain task, it can make predictions on new, unseen data based on the patterns it learned during training. This can be seen as a form of "intuition".

# Here's a simple example of a neural network in Python using the Keras library. This network is trained to classify handwritten digits from the MNIST dataset, a task it learns to do based on patterns in the training data:

# The "intuition" of this network could be seen as the learned weights and biases that it uses to classify new, unseen images.
# AY - intuition as learned weights and biases? 

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

# Load MNIST dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocess the data
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Define the neural network model
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5, batch_size=128)

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)




