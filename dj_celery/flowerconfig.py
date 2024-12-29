# flowerconfig.py

# Port on which Flower will run
port = 5555

# Basic Authentication
basic_auth = ['admin:admin123']  # Replace with desired username and password

# Persistent mode to retain task history after Flower restarts
# persistent = True

# Path to store the Flower database for task state persistence
db = None
# Maximum number of tasks to keep in memory
max_tasks = 10000

# Broker URL for Celery
broker_api = 'redis://localhost:6379/0'  # Replace with your broker URL

# Logging level
logging = 'INFO'  # Options: DEBUG, INFO, WARNING, ERROR

# Enable detailed monitoring for tasks
inspect_timeout = 1000.0

# URL Prefix (useful if Flower is behind a reverse proxy)
url_prefix = ''

# Enable XSRF Protection (for security)
xsrf_cookies = True

# SSL Configuration (optional)
# ssl_key = '/path/to/ssl/key.pem'
# ssl_cert = '/path/to/ssl/cert.pem'
