INSERT INTO `Security`(id_security, `name`, `weight`) values
(1, 'APPLE', 0.6),
(2, 'MSFT', 0.4);

INSERT INTO `Security_price`(id_security, `price`, `date`) values
(1, 123, '2021-05-15'),
(1, 124, '2021-05-15 01:00:00'),
(2, 245, '2021-05-15 01:00:00'),
(2, 244, '2021-05-15'),
(2, 243, curdate()),
(1, 124, curdate());