# Computer Aided Diagnosis Tool: Using Class Activation on X-Ray Image Data

The Densenet121.py is for the classification model implementation. The model is saved has Chnet.h5 and is available in the DS Capstone Backend.

ClassActivation.py contains the Class Activation Mapping implementation. The Class activation mapping.py requires importing the Chnet.h5 as the learning model.

## Setting up Flask.

### Backend.

1.	To install all the dependencies,  pip install -r requirements.txt

2.	Must have python 3.8+

3.	In the terminal, go to the directory where app.py is, and run flask run to have the backend server running.

4.	The backend server will be running in the port localhost:5000.



## Setting up the React based frontend.

### Frontend.

1. First please make sure you have nodeJS v14.17.0 and yarn installed. Then in the terminal, go to the directory where yarn.lock and package.json are located.

2. Enter the command yarn which will install all the required dependencies.

3. Now enter yarn start.

4. The frontend server will be running in the port localhost:3000.

## Installing Pytest

### Tests

To install pytest go to terminal and enter "pip install pytest"


## Data.

The dataset is uploaded here 
https://drive.google.com/file/d/1bum9Sehb3AzUMHLhBMuowPKyr_PCrB3a/view
