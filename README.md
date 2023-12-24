# AI-powered Virtual Architects and Interior Designers

This project is an AI-powered system that generates architecture and interior designs. It uses a trained AI model to predict and generate designs based on the input data.

## Project Structure

The project has the following structure:

- `main.py`: This is the main driver script that initializes and runs the architect and interior designer.
- `ai_model.py`: This script contains the AIModel class that loads the AI model and makes predictions.
- `architect.py`: This script contains the Architect class that generates architecture designs using the AI model.
- `interior_designer.py`: This script contains the InteriorDesigner class that generates interior designs using the AI model.
- `utils.py`: This script contains utility functions such as the function to load the configuration data.
- `config.py`: This script contains the configuration data for the project such as the path to the AI model.
- `requirements.txt`: This file lists all the Python dependencies that need to be installed.
- `README.md`: This is the file you are currently reading.

## Installation

To install and run this project, follow these steps:

1. Clone the repository:
```
git clone https://github.com/yourusername/yourrepository.git
```
2. Install the necessary dependencies:
```
pip install -r requirements.txt
```
3. Run the main script:
```
python main.py
```

## Configuration

The configuration data for the project is stored in a JSON file. The path to this file is specified in the `config.py` script. The configuration data includes the path to the AI model.

## Dependencies

This project requires the following Python libraries:

- numpy
- scipy
- pandas
- matplotlib
- seaborn
- scikit-learn
- tensorflow
- keras
- opencv-python
- Pillow

These can be installed with pip using the provided `requirements.txt` file.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
