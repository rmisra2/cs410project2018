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
`setup.py` will create the reviews data file we will need.

It will call the `parse_reviews_dataset()` function. It's slow and uses a lot of RAM, so make sure you use a reasonable review size.
