# Memory Verse

## Project Idea
I have a memory verse competition at my church, and they gave us a PDF with so many verses from the Bible. Instead of manually going through each verse and doing all that work, instead I just created this python program to make the tasks easier. This project has 3 goals that I want to accomplish:

### Goals
1. Convert PDF into Excel Sheet
    - I do this so that I can easily learn the verses
    - I tried to use an online tool, but it did not convert the PDF into the way I wanted

2. Translate to ESV
    - I want to learn this version
    - More accurate 

3. Order the verses by length
    - Easier for me in the competition

## Installed Libraries and Sources
### Python Libraries
- tqdm (for loading bar)
- request (for API handling)
- python-dotenv (for keeping API secure and loading it)
- pymupdf (formerly fitz, used for handling PDF)
- openpyxl (used for handlin excel sheets)

### API Source
Used ESV [website](https://www.esv.org/Matthew+1/) for API 

## How it works
### excelformatter.py
- converts verses from PDF to excel
- I could use a converter online, but it did not give me the desired output
- Creates Excel Format.xlsx

### esv_trans.py
- converts verses from NKJV to ESV version
- order is maintained 
- creates ESV Verses.xlsx

### length_formatter.py
- orders ESV verses from least characters to greatest characters
- **only this file was created by chatgpt** because I was running out of time to memorize verses
- creates verses_sorted.xlsx

## Project Structure

```text
Memory-Verse/
├── data/
│   ├── Bible Verses.pdf
│   ├── Excel Format.xlsx
│   ├── ESV Verses.xlsx
│   └── verses_sorted.xlsx
│
├── source/
│   ├── esv_trans.py
│   ├── excelformatter.py
│   └── length_formatter.py
│
├── .env  
├── plan.txt 
├── .gitignore
└── README.md
```

## Example Output
### Excel Format.xlsx

| Verse Number | Reference | Verse |
|--------------|-----------|-------|
| 1            |John 3:16| For God so loved the world that He gave His only begotten Son, that whoever believes in Him should not perish but have **everlasting** life.|

The verses in this file are in NKJV. Notice the word everlasting, which is different in the ESV.


### ESV Verses.xlsx

| Verse Number | Reference | Verse |
|--------------|-----------|-------|
| 1            |John 3:16|“For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have **eternal** life.|