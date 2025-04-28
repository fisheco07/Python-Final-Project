import argparse
import pandas as pd
import re
import sys
import os

def cleanup_dataframe(df, regex_clean=False):
        #Will be used to remove duplicates, whitespace and also clean up regex.
    df = df.drop_duplicates()  

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()
        if regex_clean:
           #Will make it so multiple spaces will be replaced with a single space.
            df[col] = df[col].apply(lambda x: re.sub(r'\s+', ' ', x) if isinstance(x, str) else x)

    # Will make it so that all of the columns are formatted the same.
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

#This will read the CSV file you put into the tool.
def read_csv(input_path):
    return pd.read_csv(input_path)

#This is will write the input file to the output file.
def write_csv(df, output_path):
    #This is will write the input file to the output file.
    df.to_csv(output_path, index=False)

def main():
    parser = argparse.ArgumentParser()

    # Defining the arguments.
    parser.add_argument('--input', required=True, help="Input path: CSV file.")
    parser.add_argument('--output', required=True, help="Output path: CSV file.")
    parser.add_argument('--regex', action='store_true', help="Use regex cleaning tool.")

    args = parser.parse_args()

    # This will make sure that the file put into the tool exists.

    if not os.path.exists(args.input):
        print(f" Error: Input file '{args.input}' does not exist.")
        sys.exit(1)
    #This makes sure only .csv files are used.
    input_ext = os.path.splitext(args.input)[1].lower()
    output_ext = os.path.splitext(args.output)[1].lower()

    try:
        #This will make sure that a the file put into the tool using the valid .csv format.

        if input_ext == '.csv':
            df = read_csv(args.input)
        else:
            print(" Error: Unsupported file format. Please input a .csv file.")
            sys.exit(1)

        print(f" Confirmed {len(df)} rows loaded.")

        # This will clean the dataframe
        df_cleaned = clean_dataframe(df, regex_clean=args.regex)

        #This will make sure that a the output file used is in the valid .csv format
        if output_ext == '.csv':
            write_csv(df_cleaned, args.output)
        else:
            print(" Error: Unsupported output format. Please use .csv file.")
            sys.exit(1)

        print(f" Successfully cleaned and saved {len(df_cleaned)} rows to '{args.output}'.")

    except Exception as e:
        print(f" An error has occurred: {e}. Please try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
