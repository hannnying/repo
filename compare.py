# compares historical data for stocks
from argparse import ArgumentParser
import os
import pandas as pd
import yfinance as yf

DIR = os.path.abspath(os.path.dirname(__file__))

def main():
    parser = ArgumentParser()
    parser.add_argument("--tickers", type=str, required=True)
    parser.add_argument("--period", type=str, default="5y")
    parser.add_argument("--columns", type=str, default="Close")
    args = parser.parse_args()

    companies_lst = args.tickers.split()
    columns_lst = args.columns.split()
    res = pd.DataFrame()
    for company in companies_lst:
        ticker = yf.Ticker(company)
        df = ticker.history(period=args.period)
        row = {"Date": df.index[0].date(),
               "Company": company}
        for column in columns_lst:
            row[column] = df[column]
        res = pd.concat([res, pd.DataFrame(row)], axis=0)

    for column in columns_lst:
        print(column)
        print(res.pivot(columns="Company", values=column))
        print("\n")

        
if __name__ == "__main__":
    main()