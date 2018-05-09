# cs410project2018

## Setup
Use python3

### Yelp Dataset
Download the JSON format of the [Yelp Dataset](https://www.yelp.com/dataset). Extract the files and put them in a folder called `dataset`.

Then create a new folder called `data`. This will contain our program's intermediate data files and output files.

### Install Dependencies
```
pip install -r requirements.txt
```

## Running The App
Run:
```
python3 app/setup.py
```

You should theoritically only need to do it once.

Then run:
```
python3 app/main.py
```

This will run the entire pipeline and create the intermediate data files and search results output as it runs.

The search results/output of the pipeline will be in the `data` folder, called something like `search_output_###.txt`.
