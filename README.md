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
-

## Project Structure

```text
Memory-Verse/
├── data/
│   ├── 300_bible_verses_final_2026.pdf
│   └── Memory_Verses.xlsx
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




