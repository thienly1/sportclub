CREATE DATABASE sportclub;
use sportclub;

CREATE TABLE classes (
  classID INT PRIMARY KEY AUTO_INCREMENT,
  className VARCHAR(50),
  class_description VARCHAR(255)
);

CREATE TABLE comments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    person VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    content VARCHAR(255) NOT NULL
);
CREATE TABLE members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    member_name VARCHAR(100) NOT NULL ,
    person_number VARCHAR(11) NOT NULL UNIQUE ,
    phone VARCHAR(10) NOT NULL ,
    address VARCHAR(100),
    email VARCHAR(100) NOT NULL UNIQUE ,
    classID INT,
    FOREIGN KEY (classID) REFERENCES classes(classID)
);