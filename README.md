# secfilings
An python package that gets forms 10-K, 10-Q, and 8-K from the SEC.

## Installation
`pip install secfilings`

## Usage

Two main functions. Each function returns a dictionary.
#### getForm(ticker)
returns "date", "url" and "form"
ex: 
```{'date': u'2017-02-03', 'url': 'https://www.sec.gov/Archives/edgar/data/1652044/000165204417000008/goog10-kq42016.htm', 'form': u'10-K'}```

#### getData(ticker)
returns "cik", "industry","ticker", "name", and "yrEnd"
ex: 
```{'cik': u'0001652044', 'industry': u'SERVICES-COMPUTER PROGRAMMING, DATA PROCESSING, ETC.', 'ticker': 'GOOG', 'name': u'Alphabet inc.', 'yrEnd': u'1231'}```

## Sample
```python
import secfilings as sec
#Prints the url to the latest 10K filing.
print sec.getForm("GOOG", "10-K")['url']
```
