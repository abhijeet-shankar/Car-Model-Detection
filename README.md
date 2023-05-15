# Car-Model-Detection

Car Model Detection using ResNet50
This is a Python project that uses transfer learning with the ResNet50 model to detect the brand of cars. The project is built with Flask as the front-end framework.

## About the Model

The model uses the ResNet50 architecture which is a deep learning neural network that has been pre-trained on a large dataset. The ResNet50 model is fine-tuned on a dataset of car images to detect the brand of the car.

## How to Use

To run the application, follow the steps below:

1. Clone the repository to your local machine:
git clone https://github.com/<abhijeet-shankar>/car-model-detection.git

2. Install the necessary dependencies:
!pip install flask
!pip install tensorflow
  

3. Run the Flask application:
python car-detection-flask.py
  

4. Open a web browser and navigate to `http://localhost:8080` to use the application.

## Tuning the Model

The current version of the model is not always accurate and may need to be fine-tuned to improve its performance. To do this, you can modify the hyperparameters of the model in the `train.py` file and retrain the model on a larger dataset.

## Credits

Car Model Detection was created by  Abhijeet Shankar and Parth Gupta. This project is based on the ResNet50 model implemented in Keras. The car dataset used for training and testing the model was local.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


