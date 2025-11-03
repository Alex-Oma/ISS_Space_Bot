import time

def epoch_to_readable(epoch_time):
    '''
    This function converts epoch time to a human-readable string.
    Parameters:
        epoch_time (int): The epoch time to be converted.
    Returns:
        str: The human-readable date and time string.
    '''

    return time.ctime(epoch_time)