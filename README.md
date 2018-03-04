# Time event detection using LSTM architecture
- This code is the second stage of whole project called "Realtime event detection using deep learning technique" [here](http://sclab.cafe24.com/publications/Proposal%20final4.pdf)
- As our proposed system, the output of CNN based model will be accumulated tweet data whichplay  a  role  as  the  input  of  event  detection  model.  Typically,  this  time  series  data  look  likeunderlying  discrete  signal.  Value  of  each  signal  is  accumulated  frequency  of  tweets  in  giveninterval. The moving average can be used to filter noise in time series data. Our problem is similarto anomaly detection, novel detection, that also makes sense for the case of disaster event detection.The LSTM based prediction model refer to given current and past data to estimate next time pointin the time-series. Then, the errors distribution is used to event detection model which are built by anomaly likelihood.

----
## Requirements
- Keras 
- TensorFlow 
- sickit-learn 
- GPyOpt


----
## Running
- Step1: Configuration: 
    - First set the configuration settings in `configuration/config.py`.
        - Xserver is set as True
        - experiment_id: example `Result of running LSTM 2` with input data is `Earthquake1` 
        - data_folder: example `data_folder': 'resources/data/earthquake/Earthquake2/`
    - Parametter of LSTM in `configuration/multi_step_lstm_config`.
        - bathsize, look back, look aheed,....
        - Architecture [here]()

- Step2: Data Pre-processing:
    - We need form raw data to turn to proper format for LSTM architecture that refer to
look back and look head.
    - Use notebook in the designed folder /notebook/...
    Note: Just run the first half of these notebook (Preprocessing), the rest is for visulization and time detection

- Prediction Model Execution:
    - The main LSTM models used are in the file models/lstm.py. Training the model and generating predictions two main files
    are implemented by: `lstm_predictor.py`, this file uses the default LSTM implementation by keras.
    - Run to get the output file

- Step3: 
    - Comeback notebook folder and run the rest of code to time event detection and perform visualization.