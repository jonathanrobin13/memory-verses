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
#### API 
- request (for sending request)
- python-dotenv (for keeping API secure and loading it)
- os (to get key from env)
- json (to get data from json file)

#### Files
- pymupdf (formerly fitz, used for handling PDF)
- openpyxl (used for handling excel sheets)

#### Other
- pathlib (for getting paths)
- tqdm (loading bar)
- time (tells program to wait if API sends a request back saying to wait)

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
- **only this file was created by AI** because I was running out of time to memorize verses
- creates verses_sorted.xlsx

## Functions
### files.py
- a function that allows you to open a file with or load a workbook

### api_handler.py
- load **api_settings.json**
- stores preferences for verse from the json and stores it in variables
- since json file does not store API key, this program gets it and adds it to the variables
- 

## AI Usage
This project used AI to help with the concepts of the code and to create length_formatter.py. That file was the only file that was written by AI and edited a little bit by me. The rest of the files were made by me. 

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
│   ├── API_System/
│   │   ├── api_handler.py
│   │   └── api_settings.json
│   │   
│   ├── esv_trans.py
│   ├── excelformatter.py
│   └── length_formatter.py
│
├── logo.png
├── .env  
├── LICENSE 
├── .gitignore
└── README.md
```

