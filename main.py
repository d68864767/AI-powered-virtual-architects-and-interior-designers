```python
# Import necessary modules
from ai_model import AIModel
from architect import Architect
from interior_designer import InteriorDesigner
from utils import load_config
import config

def main():
    # Load the configuration
    config_data = load_config(config.CONFIG_PATH)

    # Initialize the AI model
    ai_model = AIModel(config_data['ai_model'])

    # Initialize the architect and interior designer with the AI model
    architect = Architect(ai_model)
    interior_designer = InteriorDesigner(ai_model)

    # Run the architect and interior designer
    architect.run()
    interior_designer.run()

if __name__ == "__main__":
    main()
```
