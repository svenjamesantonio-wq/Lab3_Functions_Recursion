# telemetry_module.py
# ANTONIO | SEED: 3 | RADIOHEAD

LAST_NAME = "ANTONIO"
SEED_NUM = 3
FAVORITE_ARTIST = "RADIOHEAD"

# Decorator for monitoring
def log_process(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Generator for telemetry stream
def telemetry_generator():
    base = len(LAST_NAME) * SEED_NUM
    for i in range(1, 6):
        yield base + (i * SEED_NUM)
    yield "INVALID_DATA"  # triggers exception handling

@log_process
def process_telemetry():
    valid_count = 0
    invalid_count = 0
    processed_values = []
    
    # Lambda function to transform data
    transform = lambda x: x * 2

    for item in telemetry_generator():
        # Exception handling for invalid values
        try:
            if not isinstance(item, (int, float)):
                raise ValueError(f"Bad reading: {item}")
            
            val = transform(item)
            processed_values.append(val)
            valid_count += 1
        except ValueError as e:
            invalid_count += 1
            print(f"[ERROR CAUGHT] {e}")

    return valid_count, invalid_count, processed_values

# Recursive analysis function
@log_process
def trace_abnormal(val):
    if val <= SEED_NUM:
        return [val]
    return [val] + trace_abnormal(val - SEED_NUM)