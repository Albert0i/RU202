
try:
    from redis import Redis
    print("Redis module is installed successfully.")
except ImportError:
    print("Redis module is NOT installed.")