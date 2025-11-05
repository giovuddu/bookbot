from stats import sort_dict_vals, word_count, char_count_grouped
import sys


def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as file:
        book_text = file.read()
    return book_text


def main(args):
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")

    text = get_book_text(args[1])
    nw = word_count(text)
    ncg = char_count_grouped(text)
    sncg = sort_dict_vals(ncg)

    to_print_sncg = []
    for d in sncg:
        if not d["char"].isalpha():  # type: ignore
            continue
        to_print_sncg += [f"{d['char']}: {d['count']}"]

    to_print_sncg_string = "\n".join(to_print_sncg)

    print(
        f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {nw} total words
--------- Character Count -------
{to_print_sncg_string}
============= END ==============="""
    )


if __name__ == "__main__":
    main(sys.argv)
