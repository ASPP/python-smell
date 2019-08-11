import numpy as np


class MicroscopeState:
    def __init__(self):
        self.under_vacuum = False
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
    

def activate_vacuum_pump(microscope_state):
    """ Activate the vacuum pump. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')

    microscope_state.under_vacuum = True
    print('Vacuum pump activated')


def deactivate_vacuum_pump(microscope_state):
    """ Deactivate the vacuum pump. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')
    if not microscope_state.under_vacuum:
        raise RuntimeError('Microscope not under vacuum')
    
    microscope_state.under_vacuum = False
    print('Vacuum pump deactivated')
    

def insert_sample(microscope_state):
    """ Insert the sample in the vacuum chamber. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')
    if not microscope_state.under_vacuum:
        raise RuntimeError('Microscope not under vacuum')
    
    microscope_state.probe_present = True
    print('Probe inserted')
    

def remove_sample(microscope_state):
    """ Remove the sample from the vacuum chamber. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')
    if not microscope_state.under_vacuum:
        raise RuntimeError('Microscope not under vacuum')
    if not microscope_state.probe_present:
        raise RuntimeError('Probe not present')
      
    microscope_state.probe_present = False
    print('Probe removed')

    
def calibrate(microscope_state):
    """ Collect a calibration image. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')
    if not microscope_state.under_vacuum:
        raise RuntimeError('Microscope not under vacuum')

    print('Collecting calibration image...')
    calibration_image = np.zeros((256, 256))
    print('... done.')
    
    return calibration_image


def scan_sample(microscope_state):
    """ Scan the sample currently in the vacuum chamber. """
    if not microscope_state.connected:
        raise RuntimeError('Microscope not connected')
    if not microscope_state.under_vacuum:
        raise RuntimeError('Microscope not under vacuum')
    if not microscope_state.probe_present:
        raise RuntimeError('Probe not present')
    
    print('Scanning probe...')
    sample_image = np.ones((256, 256))
    print('... done.')
    
    return sample_image
 
