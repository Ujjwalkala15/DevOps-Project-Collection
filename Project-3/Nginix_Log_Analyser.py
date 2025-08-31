from collections import Counter

# Change this to your actual log file name
LOG_FILE = "Logfile.txt"

# Create counters for each field we want to analyze
ip_counter = Counter()
path_counter = Counter()
status_counter = Counter()
user_agent_counter = Counter()

# Read the log file line by line
with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        parts = line.split('"')  # Splits line into sections based on quotes

        try:
            ip = line.split()[0]  # First word is usually the IP address
            request = parts[1].split()  # Second quoted part is the request line
            path = request[1]  # Second word in request is the path
            status = line.split()[8]  # Status code is usually the 9th word
            user_agent = parts[-1]  # Last quoted part is the user agent

            # Count each field
            ip_counter[ip] += 1
            path_counter[path] += 1
            status_counter[status] += 1
            user_agent_counter[user_agent] += 1

        except (IndexError, ValueError):
            # Skip lines that don't match expected format
            continue

# Function to print top 5 entries from a counter
def print_top(title, counter):
    print(f"\n{title}")
    for item, count in counter.most_common(5):
        print(f"{item} - {count} requests")

# Display results
print_top("🔝 Top 5 IP addresses with the most requests:", ip_counter)
print_top("📄 Top 5 most requested paths:", path_counter)
print_top("📊 Top 5 response status codes:", status_counter)
print_top("🧭 Top 5 user agents:", user_agent_counter)
