from contextlib import contextmanager

from microscope import (
    connect_to_microscope,  # Connect to microscope and get a state object
    release_microscope,

    activate_vacuum_pump,  # Make vacuum inside the microscope 
    deactivate_vacuum_pump,
    
    insert_sample,  # Insert sample for scanning
    remove_sample,
    
    calibrate,  # Calibrate microscope
    scan_sample,  # Scan sample currently in the microscope
)


@contextmanager
def do_stuff_under_vacuum(microscope_state):
    activate_vacuum_pump(microscope_state)
    try:
        yield  # The control is returned, and a block of code is executed
        # The context manager continues from this point when the block of code exits
    finally:
        deactivate_vacuum_pump(microscope_state)


# Write here the `sample_inserted` context manager that inserts a sample
# in the microscope before executing a block of code, and safely removes 
# it at the end of the block.


# Rewrite this script using the two context managers.
microscope_state = connect_to_microscope()

activate_vacuum_pump(microscope_state)
try:
    insert_sample(microscope_state)
    try:
        sample_image = scan_sample(microscope_state)
    finally:
        remove_sample(microscope_state)
finally:
    deactivate_vacuum_pump(microscope_state)

release_microscope(microscope_state)
