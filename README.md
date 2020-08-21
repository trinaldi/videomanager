# videomanager

Django project to manage video files from Google Drive's "Shereable link".

## Motivation

Create a Django project that is *actually* useful.  
This projects combine simple CRUD actions, templates, thirdy-party modules, _et al._  
Templates were create using [Bootstrap4](https://getbootstrap.com) and [Material Icons](https://material.io/resources/icons/?style=baseline)

## Requirements

  + [Python 3](https://www.python.org/)
  + [pip](https://pip.pypa.io/en/stable/)
  + [FFmpeg](https://ffmpeg.org) is required for thumbnail creation.
  
## Usage

1. Clone this repository

	`$ git clone git@github.com:trinaldi/videomanager.git`

2. (Optional, though recommended) Create a virtual enviroment with Python inside the base dir. I use [`venv`](https://github.com/python/cpython/tree/3.8/Lib/venv/)

	`$ python -m venv .env`

3. Hopefully `freeze` correctly created the requirements, make sure to install them

	`$ pip install -r requirements.txt`

4. `cd` into the project folder and run migrations

	`$ python manage.py migrate`

5. Run the local server

	`$ python manage.py runserver`

---

At this point, the `videomanager` app will be running at http://localhost:3000

## Further information

  + Videos are saved as `mp4` for now. You can use FFmpeg to convert, if necessary.
  + Media files are created at app/`media` folder.
  + Files *will* be overwritten.

