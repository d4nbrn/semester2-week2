You are working with a database used by a university library system.  
The system tracks library members, books, and borrowing activity.

The database contains the following tables:

members(<u>member_id</u>, member_name, join_date)  
books(<u>book_id</u>, title, author)  
loans(<u>loan_id</u>, member_id, book_id, loan_date, return_date)

---

a) For each pair of tables below, state the type of relationship  
(one-to-one, one-to-many, or many-to-many) and briefly explain your reasoning.

i. Members and loans [2] - one to many, a member can have many many loans, however these loans all relate to just one member.
ii. Books and loans [2]  - one to many, a book can have many previous loans in its history and a loan can only relate to one book
iii. Members and books [2]  - many-to-many, many books can be borrowed by many members and books can be borrowed by different members

---

b) A query joins members to loans using an INNER JOIN.

i. Explain what happens to members who have never borrowed a book. [2]  - Those who have never borrowed a book will be left out of the query results, due to an inner join returning only exact matches of both tables
ii. Explain how the results of the query would change if a LEFT JOIN were used instead. [2]  - Those who have never borrowed a book will be included in the query results with a null value in the loans column of the results

---

c) The head librarian would like to see how many books have been borrowed by each library member.

i. Write an SQL query which would show the name of each library member and how many loans they have taken out. [5]  

SELECT members.member_name, COUNT(loans.loan_id)
FROM members
LEFT JOIN loans ON members.member_id=loans.member_id
GROUP BY members.member_name;

---

d) The head librarian asks:  
“Why don’t you store the book title with the loan? Wouldn’t that make it easier to see the data?”

i. Explain, using appropriate non-technical language, why this would be bad database design. [5]

If the book title was stored with the loan, every time someone took out the book this would create a new instance of the book title in the loans table, this would create larger amounts of redundant data in the loans table due to repeated entries of the book name, this could be problematic for the library since they may not the storage space to hold all the extra instances of the book name. Furthermore, if the title of the book was entered incorrectly it would take longer to change the name in all the instances of the loan table compared to changing one instance in the book table.
