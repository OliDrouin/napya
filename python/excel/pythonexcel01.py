#!/usr/bin/python3

import pandas

EXCELFILE = "movies.xls"

def main():
    movies = pandas.read_excel(EXCELFILE)
    print(movies.head())


if __name__ == "__main__":
    main()
