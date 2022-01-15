DROP TABLE IF EXISTS sensors;

CREATE TABLE sensors (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      country VARCHAR(255) NOT NULL,
                      city VARCHAR(255) NOT NULL);
