import psycopg2
from faker import Faker
import random


conn = psycopg2.connect(
    dbname='task_manager',
    user='postgres',
    password='postgrespassword',
    host='localhost',
    port='5432'
)

cur = conn.cursor()

fake = Faker()

status_types = ['new', 'in progress', 'completed']
cur.executemany(
    'INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING',
    [(status,) for status in status_types]
)

conn.commit()

num_users = 10
users = []
for _ in range(num_users):
    fullname = fake.name()
    email = fake.unique.email()
    users.append((fullname, email))

cur.executemany(
    'INSERT INTO users (fullname, email) VALUES (%s, %s)',
    users
)

conn.commit()

num_tasks = 30
tasks = []
for _ in range(num_tasks):
    title = fake.sentence(nb_words=6)
    description = fake.text(max_nb_chars=200)
    status_id = random.randint(1, len(status_types))
    user_id = random.randint(1, num_users)
    tasks.append((title, description, status_id, user_id))

cur.executemany(
    'INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)',
    tasks
)

conn.commit()

cur.close()
conn.close()