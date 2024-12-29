import redis

# Connect to Redis (default localhost:6379)
r = redis.Redis(host='localhost', port=6379, db=0)

# Set a key-value pair
# r.set('test1', 'testingVal')

# Get the value of the key
value = r.delete('test1')
print(value.decode())  # Output: my_value
