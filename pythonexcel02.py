#!/usr/bin/python3

import pandas

EXCELFILE = "movies.xls"

def main():
    movies = pandas.read_excel(EXCELFILE)
    print(movies.head())

    movies1 = pandas.read_excel(EXCELFILE, sheet_name=0, index_col=0)
    movies2 = pandas.read_excel(EXCELFILE, sheet_name=1, index_col=0)
    movies3 = pandas.read_excel(EXCELFILE, sheet_name=2, index_col=0)

    allmovies = pandas.concat([movies1, movies2, movies3])

    print(allmovies.shape)


if __name__ == "__main__":
    main()
