a command line program that takes several CSV files as arguments. Each CSV file (found in the fixtures directory of this repo) will have the same columns. Program output a new CSV file to stdout that contains the rows from each of the inputs along with an additional column that has the filename from which the row came (only the file's basename, not the entire path). Use filename as the header for the additional column.

## Running the Program
```
$ python csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv ./fixtures/household_cleaners.csv

## Running the  Unit Test Program
python -m unittest CSVCombinerUnitTest -v

## Example

Given two input files named `clothing.csv` and `accessories.csv`.

```
$ python csv-combiner.py ./fixtures/clothing.csv ./fixtures/accessories.csv