import numpy as np
import pandas as pd

import niimpy
from . import preprocess

def shutdown_info(battery_status):
    """ Returns a DataFrame with the timestamps of when the phone has shutdown.
    This includes both events, when the phone has shut down and when the phone 
    has been rebooted. 

    Parameters
    ----------
    battery_status: pandas series of the battery status 


    Returns
    -------
    shutdown: pandas series

    """
    if not battery_status.str.isnumeric().all():
        battery_status = pd.to_numeric(battery_status) #convert to numeric in case it is not
    
    shutdown = battery_status[battery_status.between(-3, 0, inclusive=False)]
    return shutdown