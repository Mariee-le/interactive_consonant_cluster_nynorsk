# Norwegian Nynorsk Consonant Cluster Finder

This Python script analyzes **Norwegian Nynorsk** text from the UDHR corpus to find words containing consecutive consonant clusters. It provides an interactive interface to explore clusters of length 2–5.

## Features

- Extracts vocabulary from the UDHR corpus for Norwegian Nynorsk.
- Detects consecutive consonant clusters using **regular expressions**.
- Interactive prompt showing counts and examples of clusters.
- Quick exploration of clusters from 2 to 5 letters.

## Requirements

- Python 3.8+
- NLTK library
- `regex` library (if using `re` is replaced by `regex`)

Install requirements:

pip install nltk, regex

## Usage

Run the script:

### Interactive Commands

| Input   | Description |
|---------|-------------|
| `cc`    | Show 2-letter consonant clusters |
| `ccc`   | Show 3-letter consonant clusters |
| `cccc`  | Show 4-letter consonant clusters |
| `ccccc` | Show 5-letter consonant clusters |
| `exit`  | Quit the program |

### Example Session


'c' represents consecutive consonants.
Write 'cc', 'ccc', 'cccc' or 'ccccc' (write exit to exit) cc

You wrote 'cc', which represents two consecutive consonants in a word.
There are 123 occurrences of this type of cluster in the text
[('st', 'stund'), ('nd', 'land'), ...]


## Notes

- The UDHR corpus is automatically downloaded if not present.
- Clusters are detected **case-insensitively**.

## License

Open source; free to use and modify.
