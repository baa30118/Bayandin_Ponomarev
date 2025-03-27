CREATE SCHEMA IF NOT EXISTS Bayandin_Ponomarev;

-- Создание таблицы cars
CREATE TABLE IF NOT EXISTS Bayandin_Ponomarev.cars (
    id SERIAL PRIMARY KEY,
    model TEXT NOT NULL,
    year INT NOT NULL,
    color TEXT NOT NULL,
    plate_number TEXT NOT NULL UNIQUE,
    car_type TEXT NOT NULL
);

-- Создание таблицы accidents
CREATE TABLE IF NOT EXISTS Bayandin_Ponomarev.accidents (
    id_accidence SERIAL PRIMARY KEY,
    id_cars INT NOT NULL REFERENCES Bayandin_Ponomarev.cars(id),
    plate_num_cars TEXT NOT NULL,
    date DATE NOT NULL,
    damage_description TEXT NOT NULL
);
