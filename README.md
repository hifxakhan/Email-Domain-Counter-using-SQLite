# Email-Domain-Counter-using-SQLite
This project processes an email dataset (e.g., mbox.txt) to extract domains from email addresses and count how many times each domain appears. The results are stored in an SQLite database and displayed in descending order.

Features
1. Reads email addresses from a text file (mbox.txt or custom file).
2. Extracts the domain part of each email (user@domain).
3. Uses SQLite to store and update counts of domains.
4. Displays the top 10 most frequent domains.

Requirements
1. Python 3.x
2. SQLite (built-in with Python)

Usage
1. Clone the repository:
git clone https://github.com/your-username/email-domain-counter.git
cd email-domain-counter

2. Run the script:
python email_counter.py

3. Enter the file name when prompted (default is mbox.txt).

Example Output: 

iupui.edu 536, 
umich.edu 491,
indiana.edu 178,
caret.cam.ac.uk 157,
vt.edu 110,
uct.ac.za 96,
media.berkeley.edu 56,
ufp.pt 28,
gmail.com 25,
et.gatech.edu 17

Notes
1. Make sure your input file (mbox.txt or another email dataset) is in the same folder as the script.
2. The database file emaildb.sqlite will be created automatically.

Learning Context
1. This project is inspired by the Python for Everybody course (Dr. Charles Severance) to practice:
2. File handling
3. String manipulation
4. Database operations with SQLite

