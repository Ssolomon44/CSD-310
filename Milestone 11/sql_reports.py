import mysql.connector
from mysql.connector import errorcode
import prettytable
from prettytable import PrettyTable 
# Reference(s) for PrettyTable:
#   https://tech.joellemena.com/python/python-print-sql-query-results-as-table/
#   https://www.geeksforgeeks.org/creating-tables-with-prettytable-library-python/

config = {
    "user": "root",
    "password": "7#x2X_p?q35x6!X",
    "host": "127.0.0.1",
    "database": "wilsonfinancial",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n  Press any key to continue...")

    cursor = db.cursor()

    ## Report 1: List of Employees and their Roles and Responsibilities ##
    query1 = "SELECT EmployeeID, Name, Role, Responsibilities FROM Employees;"
    

    ## Report 2: Client total Transaction Amount ##
    query2 = "SELECT c.ClientID, c.Name, SUM(t.TransactionAmount) AS TotalTransactionAmount FROM Clients c JOIN Transactions t ON c.ClientID = t.ClientID GROUP BY c.ClientID, c.Name ORDER BY TotalTransactionAmount DESC;"

    # ## Report 3: Clients with High Transaction Volume ##
    query3= "SELECT c.ClientID, c.Name, COUNT(t.TransactionID) AS TransactionCount FROM Clients c JOIN Transactions t on c.ClientID = t.ClientID GROUP BY c.ClientID, c.Name HAVING TransactionCount < 10 ORDER BY TransactionCount DESC;"

    ## Report 4: Number of Assets each client has Aquired ##
    query4 = "SELECT a.ClientID, c.Name, COUNT(a.AssetID) AS NumberOfAssets FROM Assets a JOIN Clients c ON a.ClientID = c.ClientID GROUP BY a.ClientID, c.Name ORDER BY NumberOfAssets DESC;"

    employeeTable = PrettyTable()
    transactionsTable = PrettyTable()
    countTable = PrettyTable()
    assetTable = PrettyTable()

    cursor.execute(query1)
    employeeReport = cursor.fetchall()

    ## EMPLOYEE REPORT ##
    print("-- EMPLOYEE REPORT --")
    employeeTable.field_names = ["Employee ID", "Name", "Role", "Responsibilities"]
    for employee in employeeReport:
        employeeTable.add_row(employee)
    
    print(employeeTable)
    print("\n")

    ## TOTAL TRANSACTION AMOUNT REPORT ##
    cursor.execute(query2)
    totalReport = cursor.fetchall()

    print("-- TOTAL TRANSACTIONS AMOUNT REPORT --")
    transactionsTable.field_names = ["Client ID", "Client Name", "Total Transactions"]
    for total in totalReport:
        transactionsTable.add_row(total)
    
    print(transactionsTable)
    print("\n")

    ## TOTAL TRANSACTION COUNT REPORT ##
    cursor.execute(query3)
    countReport = cursor.fetchall()

    print("-- TRANSACTION COUNT REPORT --")
    countTable.field_names = ["Client ID", "Client Name", "Transaction Count"]
    for count in countReport:
        countTable.add_row(count)
    
    print(countTable)
    print("\n")

    ## Total numnber of assets per client ##
    cursor.execute(query4)
    assetReport = cursor.fetchall()

    print("-- Asset Count REPORT --")
    assetTable.field_names = ["Client ID", "Client Name", "Number of Assets"]
    for asset in assetReport:
        assetTable.add_row(asset)
    
    print(assetTable)



except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

finally:
    cursor.close()
    db.close()