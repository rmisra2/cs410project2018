# cs410project2018

## Setup
Use python3

Create a new folder called `data`. This will contain our program's data files, whereas `dataset` will contain what is provided from Yelp.

### Install Dependencies
```
pip install -r requirements.txt
```

Then run:
```
python3 app/setup.py
```

You should theoritically only need to do it once.

## Processing Dataset
In `main.py`, uncomment the call to `parse_reviews_dataset()` and run it. This will create the reviews data we will need. It's slow and uses a lot of RAM, so make sure you comment it out after you run it once.
