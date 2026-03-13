"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3

"""
customers(**customer_id**, customer_name)
films(**film_id**, title, age_rating)
screenings(**screening_id**, film_id, screen)
tickets(**ticket_id**, screening_id, customer_id, price)
"""



def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.

    Write a function that returns details of tickets purchased by a specific customer.

    The function should return a list of tuples containing (in order):
    - the film title
    - the screen
    - the ticket price

    Results should be ordered alphabetically by film title.
    """
    cursor = conn.cursor()
    query = """SELECT films.title, screenings.screen, tickets.price 
    FROM customers JOIN tickets ON customers.customer_id = tickets.customer_id
    JOIN screenings ON tickets.screening_id = screenings.screening_id
    JOIN films ON screenings.film_id = films.film_id
    WHERE customers.customer_id = ?
    ORDER BY films.title ASC"""

    cursor.execute(query,(customer_id,))

    tuples = cursor.fetchall()
    return tuples
    pass


def screening_sales(conn):
    """
    customers(**customer_id**, customer_name)
    films(**film_id**, title, age_rating)
    screenings(**screening_id**, film_id, screen)
    tickets(**ticket_id**, screening_id, customer_id, price)

    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    Write a function that returns the number of tickets sold for each screening.

    The function should return a list of tuples containing (in order):
    - the screening ID
    - the film title
    - the number of tickets sold

    All screenings should be included, even if no tickets were sold for that screening.

    Results should be ordered by the number of tickets sold, from highest to lowest.
    """
    cursor = conn.cursor()
    query = """SELECT screenings.screening_id, films.title, COUNT(tickets.screening_id)
    FROM screenings INNER JOIN films ON screenings.film_id = films.film_id
    LEFT JOIN tickets ON screenings.screening_id = tickets.screening_id
    GROUP BY screenings.screening_id, films.title
    ORDER BY COUNT(tickets.screening_id) DESC"""

    cursor.execute(query)
    tuples = cursor.fetchall()
    return tuples

    pass


def top_customers_by_spend(conn, limit):
    """
    customers(**customer_id**, customer_name)
    films(**film_id**, title, age_rating)
    screenings(**screening_id**, film_id, screen)
    tickets(**ticket_id**, screening_id, customer_id, price)
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    Write a function that returns the customers who have spent the most money on tickets.

    The function should return a list of tuples containing (in order):
    - the customer name
    - the total amount spent on tickets

    Only customers who have purchased at least one ticket should be included.

    Results should be ordered by total amount spent, from highest to lowest, and limited to a specified number of rows (passed in by the argument `limit`)
    """

    cursor = conn.cursor()
    query = """SELECT customers.customer_name, SUM(tickets.ticket_id)
    FROM customers 
    INNER JOIN tickets ON customers.customer_id = tickets.customer_id
    GROUP BY customers.customer_id, customer_name
    ORDER BY SUM(tickets.price) DESC
    LIMIT ?""" 

    cursor.execute(query,(limit,))
    tuples = cursor.fetchall()
    return tuples

    pass