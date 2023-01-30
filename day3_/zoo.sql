-- enclosures and animals
-- snow_leopard_id     sumatran_tigers      howler_monkeys     ferrets     raccoons
-- both tables must include a primary key and atleast 4 variables (excluding primary key)
-- animals must belong to an enclosure

-- two dashes to make an SQL comment, SQL reads top to bottom just like python



CREATE TABLE enclosures (
    enclosure_id INT AUTOINCREMENT PRIMARY KEY,
    enclosure_name VARCHAR(30),
    enclosure_area INT(3),
    no_of_animals INT(3),
    wild_type BOOLEAN
);

CREATE TABLE animals (
    animal_id INT AUTOINCREMENT PRIMARY KEY,
    enclosure_id INT,
    animal_name VARCHAR(40),
    no_of_animal CHAR(3),
    FOREIGN KEY(enclosure_id) REFERENCES enclosure(enclosure_id)
);


