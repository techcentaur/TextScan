# TextScan
Summarise or analyse files, one file at a time.

## Usage

### Terminal Usage

```console
gavy42@jarvis:~/TextScan$ python3 scan.py -h
usage: scan.py [-h] (-s | -a) -n NUMBER filename

TextScan: Scan Text, one file at a time

positional arguments:
  filename              Enter the filename

optional arguments:
  -h, --help            show this help message and exit
  -s, --summarize       Summarize the text
  -a, --analyse         Analyse the text
  -n NUMBER, --number NUMBER
                        Number of lines
```

### Interpreter Usage

```python3
>>> from scan import Scan
>>> Scan('data.txt')
<scan.Scan object at 0x7f64a9b77f28> 
```

### Functional Usage

These public functions and variables can be utilized after creating an object of class Scan, as `Scan(<filename>)`, (say s)

**Variables**
- `s.freq_dict`: Returns a `defaultdict` of each word used and its frequency, excluding all the stop words and punctuation.
- `s.text_tokens`: Returns a list of all text tokens in the file.
- `s.text`: Returns the trivial string read from the input filename.

**Methods**
- `s.frequency_dict(reject_extreme_values)`: Calculates the frequency of each word and creates a `defaultdict` with public variable name `freq_dict`, also `reject_extreme_values` is a boolean variable, which is default=True, and when False ignores the extreme frequency of words.

- `s.sentence_rank(number)`: Gives rank to each sentence based on the occurence of word in it, also normalises it (to avoid the case of long sentences), take the number of line to be returned as an argument with `type=int`.

- `s.calculate_summary`: Returns a list with summarised data present in file.