CREATE TABLE authors (
  id serial NOT NULL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE genres (
  id serial NOT NULL PRIMARY KEY,
  name VARCHAR(255)
);

INSERT INTO authors (first_name, last_name) 
VALUES
('Дмитрий', 'Глуховский'), ('Чак', 'Паланик'), ('Агата', 'Кристи'),
('Лев', 'Толстой'), ('Сергей', 'Лукьяненко'), ('Борис', 'Акунин');

INSERT INTO genres (name) 
VALUES
('Комедия'), ('Детективы'), ('Триллер'), ('Приключения'), ('Ужасы'),
('Мистика'), ('Постапокалипсис'), ('Научная Фантастика'), ('Киберпанк'), ('Антиутопия');


SELECT id, first_name, last_name FROM authors;
SELECT id, name FROM genres;