# Recursive Fault Trace 
# ANTONIO | SEED: 3 | RADIOHEAD


LAST_NAME = "ANTONIO"
SEED_NUM = 3
FAVORITE_ARTIST = "RADIOHEAD"

def log_process(func):
    def wrapper(*args, **kwargs):
        print(f"Execution Log: Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_process
def generate_fault_code():
    base_code = (len(LAST_NAME) + len(FAVORITE_ARTIST)) * SEED_NUM
    return base_code

call_counter = 0

@log_process
def trace_fault(code):
    global call_counter
    call_counter += 1
    
    if code <= SEED_NUM:
        return [code]
    else:
        return [code] + trace_fault(code - SEED_NUM)

# Execution
if __name__ == "__main__":
    print("=== RECURSIVE FAULT TRACE SYSTEM ===")
    fault_code = generate_fault_code()
    trace_result = trace_fault(fault_code)
    
    print("\n--- ASSESSMENT DATA ---")
    print(f"Generated Fault Data: {fault_code}")
    print(f"Recursive Trace: {trace_result}")
    print(f"Number of Recursive Calls: {call_counter}")
    print(f"Final Output: Fault successfully traced down to base condition {trace_result[-1]} in {call_counter} steps.")