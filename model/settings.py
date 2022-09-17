import os

# We will store images uploaded by the user on this folder
UPLOAD_FOLDER = "uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# REDIS
# Queue name
REDIS_QUEUE = 'job' #puede ser cualquier nombre, tiene que ser siempre el mismo#
# Port
REDIS_PORT = 6379 #puerto preconfigurado (default) de redis
# DB Id
REDIS_DB_ID = 1 #le asingo un numero al trabajo de redis
# Host IP
REDIS_IP = 'redis'
# Sleep parameters which manages the
# interval between requests to our redis queue
SERVER_SLEEP = 0.05
