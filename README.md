# Computer Aided Diagnosis Tool: Using Class Activation on X-Ray Image Data

All code for the Computer Aided Diagnosis tool is contained in the Computer-Aided-Diagnosis-Tool directory. Within this directory, there are 3 subdirectories, DS Capstone Frontend, DS Capstone Backend, and DS Capstone Tests.

DS Capstone Backend, contains all the files pertaining to the models and image processing. The uploads folder contains the images selected by the user for processing. The app.py folder contains the code for hosting the flask server, and for the image processing POST request.

DS Capstone Frontend, contains all the files pertaining to the web application. The app.js folder contains all the JavaScript code used in the web application. The app.css folder contains the design code for the app.js file.

DS Capstone Test, contains a file outlining several pytests used for testing the final program.

The Densenet121.py is for the classification model implementation. The model is saved has Chnet.h5 and is available in the DS Capstone Backend. 

The cnn_xray_validation.py contains the validation model implementation. The model is saved as xray_validation.h5 and is available in the DS Capstone Backend folder.

ClassActivation.py contains the Class Activation Mapping implementation. The Class activation mapping.py requires importing the Chnet.h5 as the learning model.

## Directory Structure
- Computer-Aided-Diagnosis-Tool
    - DS Capstone Backend
        - Uploads
        - app.py
        - Chnet.h5
        - requirements.txt
        - Xray_validation4.h5
    - DS Capstone Frontend
        - src
            - App.css
            - App.js
            - index.css
            - index.js
    - DS Capstone Tests
        - configtest.py
    - classactivation.py
    - cnn_xray_validation.py
    - densenet121cvid.py
    - README.md


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
