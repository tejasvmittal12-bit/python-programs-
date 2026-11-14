# ============================================================
# Joins in SQL
# Activity: Travel Destination Explorer
# ============================================================

import sqlite3
import pandas as pd

# ---- PART 1: What is a JOIN - Build and Explore the Tables ----

# Create an in-memory database for this activity.
conn = sqlite3.connect(':memory:')

# Create a table to store travel destinations.
conn.execute("""CREATE TABLE destination (
    destination_id   INTEGER PRIMARY KEY,
    destination_name TEXT NOT NULL UNIQUE,
    country          TEXT NOT NULL
)""")

# Create a table to store attractions at each destination.
conn.execute("""CREATE TABLE attraction (
    attraction_id   INTEGER PRIMARY KEY,
    attraction_name TEXT NOT NULL,
    destination_id  INTEGER
)""")

# Add destination records.
conn.executemany("INSERT INTO destination VALUES (?, ?, ?)", [
    (1, 'Paris', 'France'),
    (2, 'Tokyo', 'Japan'),
    (3, 'Sydney', 'Australia'),
    (4, 'Rome', 'Italy'),
    (5, 'Cairo', 'Egypt'),
    (6, 'Dubai', 'UAE'),
])

# Add attraction records.
conn.executemany("INSERT INTO attraction VALUES (?, ?, ?)", [
    (1, 'Eiffel Tower', 1),
    (2, 'Louvre Museum', 1),
    (3, 'Tokyo Tower', 2),
    (4, 'Senso-ji Temple', 2),
    (5, 'Sydney Opera House', 3),
    (6, 'Colosseum', 4),
    (7, 'Trevi Fountain', 4),
])

conn.commit()

# Display both tables before joining them.
destinations = pd.read_sql("SELECT * FROM destination", conn)
attractions = pd.read_sql("SELECT * FROM attraction", conn)

print("Destination table:")
print(destinations)
print()

print("Attraction table:")
print(attractions)
print()


# ---- PART 2: INNER JOIN ----

# INNER JOIN shows only destinations that have matching attractions.
inner = pd.read_sql(
    "SELECT destination.destination_name, destination.country, "
    "attraction.attraction_name "
    "FROM destination INNER JOIN attraction "
    "ON destination.destination_id = attraction.destination_id",
    conn
)

print("INNER JOIN - destinations matched with their attractions:")
print(inner)
print()


# ---- PART 3: LEFT JOIN ----

# LEFT JOIN shows every destination.
# Destinations without attractions will show NULL.
left = pd.read_sql(
    "SELECT destination.destination_name, destination.country, "
    "attraction.attraction_name "
    "FROM destination LEFT JOIN attraction "
    "ON destination.destination_id = attraction.destination_id",
    conn
)

print("LEFT JOIN - all destinations, NULL where no attraction is found:")
print(left)
print()


# ---- PART 4: CROSS JOIN ----

# CROSS JOIN pairs each selected destination with every attraction.
cross = pd.read_sql(
    "SELECT destination.destination_name, attraction.attraction_name "
    "FROM destination CROSS JOIN attraction "
    "WHERE destination.destination_id <= 2",
    conn
)

print("CROSS JOIN - first 2 destinations paired with every attraction:")
print(cross)
print()


# ---- PART 5: UNION ----

# UNION combines destination names and attraction names into one list.
union = pd.read_sql(
    "SELECT destination_name AS name, 'Destination' AS type "
    "FROM destination "
    "UNION "
    "SELECT attraction_name AS name, 'Attraction' AS type "
    "FROM attraction",
    conn
)

print("UNION - all destination names and attraction names combined:")
print(union)

conn.close()
