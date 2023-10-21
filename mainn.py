import pandas as pd
import argparse
from typing import List, Dict

ARTIST_CL = 7


def open_file(path: str) -> List[List[object]]:
    df = pd.read_csv(path)

    return df.values.tolist()

def get_year_stats(table: List) -> Dict:
    data = dict()
    for x in range(2000, 2023):
        data[x]=0
    for el in table:
        data[el[1]]+=1
    return table


def get_top_artist_count(table, n=5):
    artists = dict()

    for row in table:
        artists[row[ARTIST_CL]] = artists.get(row[ARTIST_CL], 0) + 1


    return sorted(artists.items(), key=lambda x: x[1], reverse=True)[:n]



if __name__ == "__main__":

    # придумываем аргументы, которые сможет прочитать прога
    parser = argparse.ArgumentParser(description="our little spotify experience")

    parser.add_argument("file_path", type=str, help="input path to our datasheet")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Shows more info during script run"
    )
    parser.add_argument(
        "-s", "--stats", action="store_true", help="returns year stats"
    )
    parser.add_argument(
        "-t", "--top_artists", type=int, help="returns top artists"
    )

    # парсим аргументы в переменные
    args = parser.parse_args()

    if args.verbose:
        print(args)
        print("Hello world")
        print(f"File path: {args.file_path}")

    table = open_file(args.file_path)

    print(len(table))
    if args.stats:
        print(get_year_stats(table))

    if args.top_artists:
        res = get_top_artist_count(table, args.top_artists)
        for idx, el in enumerate(res):
            print(f"{idx + 1}) {el[0]}: {el[1]}")
