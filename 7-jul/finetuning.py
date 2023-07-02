# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import tensorflow as tf

# Load and preprocess data
data = pd.read_csv('data.csv')
X = data.drop('target', axis=1)
y = data['target']
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

# Define model architecture
base_model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Train the model
base_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = base_model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# Save model weights
base_model.save_weights('base_model_weights.h5')

# Load pre-trained model
fine_tuned_model = tf.keras.models.clone_model(base_model)
fine_tuned_model.load_weights('base_model_weights.h5')

# Fine-tune the model
for layer in fine_tuned_model.layers[:-1]:
    layer.trainable = False
    
fine_tuned_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
fine_tuned_history = fine_tuned_model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# Evaluate fine-tuned model
val_predictions = fine_tuned_model.predict(X_val)
accuracy = accuracy_score(y_val, val_predictions)
f1 = f1_score(y_val, val_predictions)

# Print metrics
print(f"Validation Accuracy: {accuracy}")
print(f"Validation F1 Score: {f1}")

# no actual hyperparameter tuning or visualization provided, would depend on specific usage scenarios.