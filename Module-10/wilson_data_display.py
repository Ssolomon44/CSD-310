import mysql.connector
from mysql.connector import errorcode

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

    ## Step 1: Set up queries ##
    query1 = "select * from assets;"

    query2 = "select * from billing;"

    query3 = "select * from clients;"

    query4 = "select * from compliance;"

    # This is the main table with information
    query5 = "select * from employees;"

    query6 = "select * from transactions;"

    ## Step 2/3: Execute queries/print the results
    cursor.execute(query1)
    assetsResults = cursor.fetchall()

    print("\n-- DISPLAYING Assets RECORDS --")
    for asset in assetsResults:
        print("Asset ID: {}\nAsset Type: {}\nAsset Value: {}\nAcquired Date: {}\n".format(asset[0], asset[1], asset[2], asset[3]))

    cursor.execute(query2)
    billingResults = cursor.fetchall()

    print("\n-- DISPLAYING Billing RECORDS --")
    for bills in billingResults:
        print("Billing ID: {}\nBilling Date: {}\nBilling Type: {}\nBilling Amount: {}\n".format(bills[0], bills[1], bills[2], bills[3]))

    cursor.execute(query3)
    clientsResults = cursor.fetchall()

    print("\n-- DISPLAYING Clients RECORDS --")
    for clients in clientsResults:
        print("Client ID: {}\nClient Name: {}\nContact Info: {}\n".format(clients[0], clients[1], clients[2]))

    cursor.execute(query4)
    complianceResults = cursor.fetchall()

    print("\n-- DISPLAYING Compliance RECORDS --")
    for compliance in complianceResults:
        print("Compliance ID: {}\nCompliance Date: {}\nRegulation: {}\nCompliance Status: {}\n".format(compliance[0], compliance[1], compliance[2], compliance[3]))

    cursor.execute(query5)
    employeesResults = cursor.fetchall()

    print("\n-- DISPLAYING Employee RECORDS --")
    for employee in employeesResults:
        print("Employee ID: {}\nEmployee Name: {}\nEmployee Role: {}\nResponsibilities: {}\n".format(employee[0], employee[1], employee[2], employee[3]))

    cursor.execute(query6)
    transactionsResults = cursor.fetchall()

    print("\n-- DISPLAYING Transactions RECORDS --")
    for transaction in transactionsResults:
        print("Transaction ID: {}\nTransaction Amount: {}\nTransaction Date: {}\n".format(transaction[0], transaction[1], transaction[2]))
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

finally:
    db.close()