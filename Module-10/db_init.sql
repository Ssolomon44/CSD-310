-- if database exists, drop it
DROP USER IF EXISTS 'wilson_user'@'localhost';

-- Create the database
CREATE DATABASE wilsonfinancial;

-- create wilson_user and grant all privilages to the new database
-- grant all privileges to the wilson financial database to user wilson_user on localhost
CREATE USER 'wilson_user'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON wilsonfinancial.* TO 'wilson_user'@'localhost';
FLUSH PRIVILEGES;

USE WilsonFinancial;

/*
    Create the tables
*/

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Role VARCHAR(50),
    Responsibilities TEXT
);

CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    ContactInfo VARCHAR(255),
    EmployeeID INT,
    FOREIGN KEY (EmployeeID) REFERENCES Employees (EmployeeID)
);

CREATE TABLE Transactions(
    TransactionID INT NOT NULL AUTO_INCREMENT,
    TransactionAmount DECIMAL(15, 2), -- Reference for Decimal: https://www.w3schools.com/sql/sql_datatypes.asp
    TransactionDate DATE,
    ClientID INT,

    PRIMARY KEY (TransactionID),
    FOREIGN KEY (ClientID) REFERENCES Clients (ClientID)
);

CREATE TABLE Compliance(
    ComplianceID INT NOT NULL AUTO_INCREMENT,
    ComplianceDate DATE,
    Regulation VARCHAR(250),
    ComplianceStatus VARCHAR(100),
    EmployeeID INT,

    PRIMARY KEY (ComplianceID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees (EmployeeID)
);

CREATE TABLE Assets(
    AssetID INT NOT NULL AUTO_INCREMENT,
    AssetType VARCHAR(250),
    AssetValue DECIMAL(15,2) NOT NULL,
    AcquisitionDate DATE,
    ClientID INT NOT NULL,

    PRIMARY KEY (AssetID),
    FOREIGN KEY (ClientID) REFERENCES Clients (ClientID)
);

CREATE TABLE Billing(
    BillingID INT NOT NULL AUTO_INCREMENT,
    BillingDate DATE,
    BillingType VARCHAR(250) NOT NULL,
    BillingAmount DECIMAL(15,2) NOT NULL,
    ClientID INT NOT NULL,

    PRIMARY KEY (BillingID),
    FOREIGN KEY (ClientID) REFERENCES Clients (ClientID)
);

/*
    ADD RECORDS
*/
    INSERT INTO Employees (Name, Role, Responsibilities)
    VALUES('Phoenix Two Star', 'Office Clerk', "Handle client appointments, office supplies, and other office duties.");

    INSERT INTO Employees (Name, Role, Responsibilities)
    VALUES('June Santos', 'Compliance Manager', "Works Part-time handling employee compliance and regulations required by SEC.");
