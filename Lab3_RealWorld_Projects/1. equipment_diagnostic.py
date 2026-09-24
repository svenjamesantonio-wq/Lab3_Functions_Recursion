# Equipment Diagnostic System 
# ANTONIO | SEED: 3 | RADIOHEAD

def log_process(func):
    def wrapper(*args, **kwargs):
        print(f"Execution Log: Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_process
def generate_readings():
    return [len("ANTONIO") * 3, 25, -5, len("RADIOHEAD") * 3]

@log_process
def validate_readings(data):
    valid = []
    for x in data:
        try:
            if x < 0: raise ValueError(f"Negative value {x}")
            valid.append(x)
        except ValueError as e:
            print(f"Validation Exception Caught: {e}")
    return valid

@log_process
def calculate_and_classify(valid):
    avg = sum(valid) / len(valid) if valid else 0
    status = "OPTIMAL" if avg >= 20 else "CHECK REQUIRED"
    return avg, status

# Execution
if __name__ == "__main__":
    print("=== EQUIPMENT DIAGNOSTIC SYSTEM ===")
    raw = generate_readings()
    clean = validate_readings(raw)
    avg, status = calculate_and_classify(clean)
    
    print("\n--- ASSESSMENT DATA ---")
    print(f"Generated Equipment Data: {raw}")
    print(f"Validation Results:{clean}")
    print(f"Diagnostic Results: Average = {avg}, Status = {status}")
    print(f"Final Output: System Condition is {status}")