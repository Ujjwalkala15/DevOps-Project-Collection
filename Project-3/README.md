---

## 📘 Nginx Log Analyzer

A simple Python script to analyze Nginx access logs and extract useful insights like:
- Top 5 IP addresses
- Top 5 requested paths
- Top 5 response status codes
- Top 5 user agents

This project is perfect for beginners who want to learn basic log parsing and data analysis using Python.

---

## 🧰 Requirements

- Python 3.x installed
- A sample Nginx access log file (e.g., `Logfile.txt`)
- Basic familiarity with running Python scripts

---

## 📂 Project Structure

```
nginx-log-analyzer/
│
├── nginx_log_analyzer.py   # Main Python script
├── Logfile.txt             # Your Nginx access log file
└── README.md               # This documentation file
```

---

## 🚀 How to Run the Project

### Step 1: Clone or Download the Project

You can copy the files manually or use Git:

```bash
git clone https://github.com/your-username/nginx-log-analyzer.git
cd nginx-log-analyzer
```

### Step 2: Place Your Log File

Make sure your Nginx log file is named `Logfile.txt` and placed in the same folder as the script.

### Step 3: Run the Script

Open your terminal and run:

```bash
python nginx_log_analyzer.py
```

### Step 4: View the Output

The script will display:

- 🔝 Top 5 IP addresses with the most requests
- 📄 Top 5 most requested paths
- 📊 Top 5 response status codes
- 🧭 Top 5 user agents

Each section shows the item and how many times it appeared in the log.

---

## 🧠 How It Works (Simplified)

- The script reads each line of the log file.
- It splits the line using quotes (`"`) and spaces to extract key fields.
- It counts how often each IP, path, status code, and user agent appears.
- It prints the top 5 most frequent entries for each category.

No complex regular expressions. Just clean, readable Python code.

---

## 🛠️ Customization Tips

Want to tweak it? Try these:
- Change the number of top results (`most_common(5)` → `most_common(10)`)
- Filter by date or status code
- Export results to a `.txt` or `.csv` file

---

## 🧪 Sample Log Format (Expected)

```
192.168.1.1 - - [date] "GET /api/v1/users HTTP/1.1" 200 123 "-" "Mozilla/5.0"
```

If your log format is different, you may need to adjust how the script splits and extracts fields.

---

## 🙌 Credits

Created by Ujjwal Kala
Site Reliability Engineer | Python & Infrastructure Specialist

---
