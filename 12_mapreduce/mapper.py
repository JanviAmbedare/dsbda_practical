def mapper(line):
    parts = line.strip().split()
    if len(parts) >= 3:
        log_level = parts[2]
        return (log_level, 1)
    return None
