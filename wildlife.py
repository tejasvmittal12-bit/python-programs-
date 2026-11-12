# ============================================================
# DSCM11L3 — SQL Statements Part 2
# Activity: Wildlife Park Records Analyzer
# ============================================================

# ---- PART 1: Build the Database ----
# This database stores information about animals in a wildlife park.
# It has three tables: Animal, Keeper, and Animal_Keeper.
# We will use SQL to sort, count, total, average, and group
# the data in different ways.

import sqlite3
import pandas as pd

conn = sqlite3.connect('wildlife_park.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Animal;
DROP TABLE IF EXISTS Keeper;
DROP TABLE IF EXISTS Animal_Keeper;

CREATE TABLE Animal (
    Animal_Id     INTEGER PRIMARY KEY,
    Animal_Name   TEXT,
    Animal_Type   TEXT,
    Habitat       TEXT,
    Age           INTEGER,
    Food_Kg       REAL
);

CREATE TABLE Keeper (
    Keeper_Id     INTEGER PRIMARY KEY,
    Keeper_Name   TEXT,
    Country       TEXT
);

CREATE TABLE Animal_Keeper (
    Animal_Id  INTEGER,
    Keeper_Id  INTEGER
);

INSERT INTO Animal VALUES
  (1,'Leo','Mammal','Savannah',8,7.5),
  (2,'Maya','Mammal','Savannah',5,6.0),
  (3,'Ella','Bird','Rainforest',4,1.5),
  (4,'Rio','Bird','Rainforest',3,1.2),
  (5,'Tara','Reptile','Wetland',10,2.0),
  (6,'Max','Mammal','Forest',6,4.5),
  (7,'Nina','Mammal','Forest',2,3.0),
  (8,'Ollie','Bird','Wetland',7,1.8),
  (9,'Zara','Reptile','Desert',9,2.5),
  (10,'Ben','Mammal','Savannah',11,8.0),
  (11,'Kiwi','Bird','Forest',5,1.4),
  (12,'Rex','Reptile','Desert',6,2.2);

INSERT INTO Keeper VALUES
  (1,'Aarav', 'India'),
  (2,'Diya', 'India'),
  (3,'Meera', 'Kenya'),
  (4,'Kabir', 'Australia'),
  (5,'Riya', 'India');

INSERT INTO Animal_Keeper VALUES
  (1,1),(2,1),(3,2),(4,2),(5,3),
  (6,4),(7,4),(8,3),(9,5),(10,1);
""")

conn.commit()
print('Wildlife park database ready!')

# ---- PART 2: DISTINCT — Unique Values Only ----
# DISTINCT removes duplicate values.
# It shows each unique value only once.

# All unique animal types in the Animal table
animal_types = pd.read_sql("""SELECT DISTINCT(Animal_Type)
    FROM Animal;""", conn)
print(animal_types)

# All unique habitats in the Animal table
habitats = pd.read_sql("""SELECT DISTINCT(Habitat)
    FROM Animal;""", conn)
print(habitats)

# ---- PART 3: ORDER BY — Sorting Results ----
# ORDER BY sorts results by a chosen column.
# DESC sorts from largest to smallest.

# All animals sorted by age — oldest first
oldest_animals = pd.read_sql("""SELECT Animal_Name, Animal_Type, Age
    FROM Animal
    ORDER BY Age DESC;""", conn)
print(oldest_animals)

# All animals sorted by food amount — smallest first
food_order = pd.read_sql("""SELECT Animal_Name, Food_Kg
    FROM Animal
    ORDER BY Food_Kg;""", conn)
print(food_order)

# Keepers sorted by name
keeper_names = pd.read_sql("""SELECT Keeper_Name, Country
    FROM Keeper
    ORDER BY Keeper_Name;""", conn)
print(keeper_names)

# ---- PART 4: COUNT and SUM ----
# COUNT(column) counts the number of rows.
# SUM(column) adds all values in a number column.

# Total number of mammals in the wildlife park
mammal_count = pd.read_sql("""SELECT COUNT(Animal_Id)
    FROM Animal
    WHERE Animal_Type == 'Mammal';""", conn)
print(mammal_count)

# Total food needed by all birds
bird_food = pd.read_sql("""SELECT SUM(Food_Kg)
    FROM Animal
    WHERE Animal_Type == 'Bird';""", conn)
print(bird_food)

# ---- PART 5: AVG — Finding the Average ----
# AVG(column) finds the average value in a column.

# Average age of all animals
average_age = pd.read_sql("""SELECT AVG(Age)
    FROM Animal;""", conn)
print(average_age)

# Average food needed by mammals
average_mammal_food = pd.read_sql("""SELECT AVG(Food_Kg)
    FROM Animal
    WHERE Animal_Type == 'Mammal';""", conn)
print(average_mammal_food)

# ---- PART 6: GROUP BY — Summarising by Category ----
# GROUP BY creates groups using values from one column.
# COUNT, AVG, and SUM can then be used for each group.

# Number of animals in each habitat
animals_per_habitat = pd.read_sql("""SELECT Habitat, COUNT(Animal_Id)
    FROM Animal
    GROUP BY Habitat;""", conn)
print(animals_per_habitat)

# Average age of animals in each habitat
average_age_per_habitat = pd.read_sql("""SELECT Habitat, AVG(Age)
    FROM Animal
    GROUP BY Habitat
    ORDER BY AVG(Age) DESC;""", conn)
print(average_age_per_habitat)

conn.close()
