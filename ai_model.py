```python
# Import necessary modules
import tensorflow as tf
from tensorflow.keras.models import load_model

class AIModel:
    def __init__(self, config):
        self.model_path = config['model_path']
        self.model = self.load_ai_model()

    def load_ai_model(self):
        """
        Function to load the AI model from the specified path
        """
        try:
            model = load_model(self.model_path)
            print("AI Model loaded successfully.")
            return model
        except Exception as e:
            print(f"Error occurred while loading the model: {e}")
            return None

    def predict(self, input_data):
        """
        Function to make predictions using the loaded AI model
        """
        try:
            prediction = self.model.predict(input_data)
            return prediction
        except Exception as e:
            print(f"Error occurred while making prediction: {e}")
            return None
```
