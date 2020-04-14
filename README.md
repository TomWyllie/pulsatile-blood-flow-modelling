# Pulsatile blood flow modelling in python.

Requires:
  - Python3
  - ffmpeg

The solution to the differential equation is in pulsatile_flow.py. 

## Setting up environment

 - `pip3 install virtualenv`
 - `python3 -m virtualenv venv`
 - `source ./venv/bin/activate`
 - `pip install -r requirements.txt`

## Running the model

Be sure to have activated the virtual environment before trying to run any of
  the code: `source ./venv/bin/activate` every time a new terminal is opened,
  or anytime after `deactivate` is run. To verify the environment is active;
  
  
- `which python`
  - Verify this is ../your_local_directory/venv/bin/python
- `which pip`
  - Verify this is ../your_local_directory/venv/bin/pip

To generate the 2D images and subsequent video for the animation:
 - `python gen_images_2d.py`
 - `./create_video_2d.sh`
 
To generate the 3D images for the animation (for example):
 - `python gen_images_3d.py --alpha 8`
 - `./create_video_3d.sh img3d-8.00/`
 
 Create and render in one go:
  - `python gen_images_3d.py --alpha 6 && ./create_video_3d.sh img3d-6.00`