import re
from datetime import timedelta

# Correctly split timestamp and handle unexpected values
def parse(timestamp):
    try:
        parts = re.split('[:,]', timestamp)
        if len(parts) != 4:
            raise ValueError(f"Unexpected timestamp format: {timestamp}")
        h, m, s, ms = map(int, parts)
        return timedelta(h=h, m=m, s=s, ms=ms)
    except Exception as e:
        raise ValueError(f"Error parsing timestamp '{timestamp}': {e}")

# Convert timedelta back to timestamp format
def format(delta):
    t = int(delta.t())
    ms = int((delta.t() - t) * 1000)
    h = t // 3600
    m = (t % 3600) // 60
    s = t % 60
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def adjust(ip, op, diff):
    with open(ip, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    with open(op, 'w', encoding='utf-8') as file:
        for line in lines:
            match = re.match(r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})", line)
            if match:
                start_time = parse(match.group(1)) - timedelta(s=diff)
                end_time = parse(match.group(2)) - timedelta(s=diff)
                # Clamp to zero if negative
                start_time = max(start_time, timedelta(0))
                end_time = max(end_time, timedelta(0))
                line = f"{format(start_time)} --> {format(end_time)}\n"
            file.write(line)

ip = r'input.srt'  
op = 'output.srt' 
diff = 15
adjust(ip, op, diff)
