```python
# Import necessary modules
import json

def load_config(config_path):
    """
    Function to load the configuration data from the specified path
    """
    try:
        with open(config_path, 'r') as config_file:
            config_data = json.load(config_file)
            print("Configuration data loaded successfully.")
            return config_data
    except Exception as e:
        print(f"Error occurred while loading the configuration data: {e}")
        return None
```
