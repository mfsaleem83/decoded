import sqlite3

# Connect to the Sakila database
conn = sqlite3.connect("sqlite-sakila.db")
cursor = conn.cursor()

# --- STEP 1: Extract ---
# TODO: Change this to extract rating data from the film table instead
# cursor.execute("SELECT customer_id FROM rental")
# rentals = cursor.fetchall()
# print(f"Total rental records: {len(rentals)}")  # TODO: Update this print message to reflect the film table

cursor.execute("SELECT rating  FROM film")
ratings = cursor.fetchall()
# TODO: Update this print message to reflect the film table
print(f"Total rating records: {len(ratings)}")


# --- STEP 2: Transform ---
# TODO: Update this query to group films by rating and count how many films per rating
# transform_query = """
# SELECT customer_id, COUNT(*) AS total_rentals
# FROM rental
# GROUP BY customer_id
# """
# results = cursor.execute(transform_query).fetchall()
# print(results)

transform_query = """
SELECT rating, COUNT(*) AS total_films
FROM film
GROUP BY rating
"""
results = cursor.execute(transform_query).fetchall()
print(results)

# --- STEP 3: Load ---
# TODO: Change the table name and columns to match your new transformation (e.g., rating_summary)
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS customer_id_summary (
#    customer_id INTEGER,
#    total_rentals INTEGER
# )
# """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS rating_summary (
    rating TEXT,
    total_film INTEGER
)
""")


# TODO: Update the insert statement to match the new table and columns (e.g., rating, total_films)
# cursor.executemany("""
# INSERT INTO customer_rental_summary (customer_id, total_rentals)
# VALUES (?, ?)
# """, results)

cursor.executemany("""
INSERT INTO rating_summary (rating, total_film)
VALUES (?, ?)
""", results)


conn.commit()
# TODO: Update this message to reflect new table
print("Loaded summary data into rating_summary table.")

# --- STEP 4: Verify ---
# TODO: Update table name here to reflect your new summary table
# cursor.execute("SELECT * FROM customer_rental_summary LIMIT 5")
# for row in cursor.fetchall():
#    print(row)

cursor.execute("SELECT * FROM rating_summary LIMIT 5")
for row in cursor.fetchall():
    print(row)

conn.close()
