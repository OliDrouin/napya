#!/usr/bin/python3

import pandas
import xlrd

EXCELFILE = "movies.xls"

def main():
    movies = pandas.read_excel(EXCELFILE)
    print(movies.head())

    movies1 = pandas.read_excel(EXCELFILE, sheet_name=0, index_col=0)
    movies2 = pandas.read_excel(EXCELFILE, sheet_name=1, index_col=0)
    movies3 = pandas.read_excel(EXCELFILE, sheet_name=2, index_col=0)

    allmovies = pandas.concat([movies1, movies2, movies3])

    print(allmovies.shape)

    sorted_by_gross = allmovies.sort_values(["Gross Earnings"], ascending=False)

    print(sorted_by_gross.head())

    allmovies.to_excel('singlesheet.xlsx')

if __name__ == "__main__":
    main()
