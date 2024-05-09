# models/ensemble/ensemble_model.py
import logging
import tensorflow as tf
from models.lstm.lstm_model import create_lstm_model
from models.xgboost.xgboost_model import create_xgboost_model

logger = logging.getLogger(__name__)

def create_ensemble_model(lstm_input_shape, xgboost_input_shape):
    try:
        lstm_model = create_lstm_model(lstm_input_shape)
        xgboost_model = create_xgboost_model(xgboost_input_shape)
        
        ensemble_inputs = [lstm_model.input, xgboost_model.input]
        ensemble_outputs = [lstm_model.output, xgboost_model.output]
        ensemble_output = tf.keras.layers.Average()(ensemble_outputs)
        
        ensemble_model = tf.keras.Model(inputs=ensemble_inputs, outputs=ensemble_output)
        ensemble_model.compile(optimizer='adam', loss='mse')
    except Exception as e:
        logger.error(f"Error creating ensemble model: {e}")
        raise e
    return ensemble_model

