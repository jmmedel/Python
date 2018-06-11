


"""

SELECT
In SQL, selection is done using a comma-separated list of columns that you select (or a * to select all columns) −

SELECT total_bill, tip, smoker, time
FROM tips
LIMIT 5;
With Pandas, column selection is done by passing a list of column names to your DataFrame −

tips[['total_bill', 'tip', 'smoker', 'time']].head(5)
Let’s check the full program −


"""
