# pemrograman-python-remidi
##  sql untuk database
```sql
CREATE DATABASE test_db;
USE test_db;
CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    warna VARCHAR(30) NOT NULL,
    tahun INT NOT NULL,
    price FLOAT NOT NULL
);
```
