-- enclosures and animals
-- snow_leopard_id     sumatran_tigers      howler_monkeys     ferrets     raccoons
-- both tables must include a primary key and atleast 4 variables (excluding primary key)
-- animals must belong to an enclosure

-- two dashes to make an SQL comment, SQL reads top to bottom just like python

CREATE TABLE enclosures (
    enclosure_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enclosure_name VARCHAR(30),
    enclosure_area INTEGER(3),
    no_of_animals INTEGER(3),
    wild_type BOOLEAN
);

CREATE TABLE animals (
    animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    enclosure_id INTEGER,
    animal_name VARCHAR(40),
    trophic_level VARCHAR(20),
    life_span INTEGER,
    FOREIGN KEY(enclosure_id) REFERENCES enclosures(enclosure_id)
);


