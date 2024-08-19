-- if database exists, drop it
DROP USER IF EXISTS 'wilson_user'@'localhost';

-- create wilson_user and grant all privilages to the new database
-- grant all privileges to the wilson financial database to user wilson_user on localhost
CREATE USER 'wilson_user'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON wilsonfinancial.* TO 'wilson_user'@'localhost';
FLUSH PRIVILEGES;

USE WilsonFinancial;

/*
    ADD RECORDS
*/

/*
    Clients
*/
    INSERT INTO Clients (ClientID, Name, ContactInfo, EmployeeID)
    VALUES(1, 'John Smith', "johnsmith123@gmail.com", NULL);

    INSERT INTO Clients (ClientID, Name, ContactInfo, EmployeeID)
    VALUES(2, 'Jane Doe', "janedoe456@gmail.com", NULL);

/*
    Assets
*/

    INSERT INTO Assets (AssetID, AssetType, AssetValue, AcquisitionDate, ClientID)
    VALUES(1, 'Painting', 5000.0, '2023-05-25', 1);

    INSERT INTO Assets (AssetID, AssetType, AssetValue, AcquisitionDate, ClientID)
    VALUES (2, 'Computer', 1999.99, '2024-01-12', 1);

    INSERT INTO Assets (AssetID, AssetType, AssetValue, AcquisitionDate, ClientID)
    VALUES (3, 'Desk', 500.0, '2024-04-08', 2);

    INSERT INTO Assets (AssetID, AssetType, AssetValue, AcquisitionDate, ClientID)
    VALUES (4, 'Painting', 1200.0, '2023-12-31', 2);

    INSERT INTO Assets (AssetID, AssetType, AssetValue, AcquisitionDate, ClientID)
    VALUES (5, '4k-TV', 2000.0, '2024-06-12', 1);

/*
    Transactions
*/
    INSERT INTO Transactions (TransactionID, TransactionAmount, TransactionDate, ClientID)
    VALUES (1, 5000.0, '2023-05-25', 1);

    INSERT INTO Transactions (TransactionID, TransactionAmount, TransactionDate, ClientID)
    VALUES (2, 1999.99, '2024-01-12', 1);

    INSERT INTO Transactions (TransactionID, TransactionAmount, TransactionDate, ClientID)
    VALUES (3, 500.0, '2024-04-12', 2);

    INSERT INTO Transactions (TransactionID, TransactionAmount, TransactionDate, ClientID)
    VALUES (4, 1200.0, '2024-01-02', 2);

    INSERT INTO Transactions (TransactionID, TransactionAmount, TransactionDate, ClientID)
    VALUES (5, 2000.0, '2024-06-14', 1);
