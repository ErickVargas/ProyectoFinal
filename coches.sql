create database coches;
use coches;

CREATE TABLE `coches`.`usuarios` (
  `nombre` CHAR(20) NOT NULL,
  `passw` VARCHAR(20) NULL,
  PRIMARY KEY (`nombre`));
;

CREATE TABLE `coches`.`autos` (
  `id_auto` INT NOT NULL AUTO_INCREMENT,
  `Marca` VARCHAR(45) NULL,
  `SubMarca` VARCHAR(45) NULL,
  `Modelo` INT NULL,
  `Descripcion` TEXT(100) NULL,
  PRIMARY KEY (`id_auto`));

INSERT INTO `coches`.`usuarios` (`nombre`, `passw`) VALUES ('erick', '1234');

INSERT INTO `coches`.`autos` (`id_auto`, `Marca`, `SubMarca`, `Modelo`, `Descripcion`) VALUES ('1', 'Ford', 'Mustang', '1964', 'Primer Mustang que salio a la venta ');

ALTER TABLE `coches`.`autos` 
ADD COLUMN `Imagen` VARCHAR(255) NULL AFTER `Descripcion`;

