/*
Описание:

Есть таблица с двумя полями Id и Timestamp, где Id- возрастающая последовательность, каждая вставка новой записи в таблицу
приводит к генерации ID(n)=ID(n-1) + 1
Timestamp – временная метка, в стандартном процессе текущее время, при вставке
задним числом может принимать любые значения меньше максимума времени всех
предыдущих записей
Вставка задним числом – операция вставки записи в таблицу при которой
ID(n) > ID(n-1)
Timestamp(n) > max(timestamp(1):timestamp(n-1))
*/


CREATE TABLE Dates(
	id serial,
	timestamp Date
);

INSERT INTO Dates(timestamp)
VALUES ('2023-01-04'),
    ('2023-01-05'),
    ('2023-01-03'), -- backdate
    ('2023-01-04'), -- backdate
    ('2023-01-08'),
    ('2023-01-09'),
    ('2023-01-01'), --backdate
    ('2023-02-01'),
    ('2023-01-10'), --backdate
    ('2023-01-12')  --backdate



SELECT t1.id
FROM dates t1
WHERE (
	select count(*) from dates t2
	where t2.id < t1.id and t2.timestamp > t1.timestamp
) > 0