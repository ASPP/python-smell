import numpy as np


class MicroscopeState:
    def __init__(self):
        self.under_void = False
        self.probe_present = False
        self.connected = False

        
def connect_to_microscope():
    """ Connect and lock microscope, and return state object. """
    microscope_state = MicroscopeState()
    microscope_state.connected = True
    print('Connected to microscope')
    return microscope_state


def release_microscope(microscope_state):
    """ Unlock the microscope. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')
    
    microscope_state.connected = False
    print('Microscope released')
    

def make_void(microscope_state):
    """ Activate the void pump. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')

    microscope_state.under_void = True
    print('Microscope under void')


def release_void(microscope_state):
    """ Deactivate the void pump. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')
    if not microscope_state.under_void:
        raise RuntimeError('Microscope not under void')
    
    microscope_state.under_void = False
    print('Void released')
    

def insert_sample(microscope_state):
    """ Insert the sample in the void chamber. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')
    if not microscope_state.under_void:
        raise RuntimeError('Microscope not under void')
    
    microscope_state.probe_present = True
    print('Probe inserted')
    

def remove_sample(microscope_state):
    """ Remove the sample from the void chamber. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')
    if not microscope_state.under_void:
        raise RuntimeError('Microscope not under void')
    if not microscope_state.probe_present:
        raise RuntimeError('Probe not present')
      
    microscope_state.probe_present = False
    print('Probe removed')

    
def calibrate(microscope_state):
    """ Collect a calibration image. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')
    if not microscope_state.under_void:
        raise RuntimeError('Microscope not under void')

    print('Collecting calibration image...')
    calibration_image = np.zeros((256, 256))
    print('... done.')
    
    return calibration_image


def scan_sample(microscope_state):
    """ Scan the sample currently in the void chamber. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')
    if not microscope_state.under_void:
        raise RuntimeError('Microscope not under void')
    if not microscope_state.probe_present:
        raise RuntimeError('Probe not present')
    
    print('Scanning probe...')
    sample_image = np.ones((256, 256))
    print('... done.')
    
    return sample_image
 
