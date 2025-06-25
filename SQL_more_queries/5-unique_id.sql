-- creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL UNIQUE,
    name VARCHAR(256)
);