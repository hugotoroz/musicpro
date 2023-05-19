SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema prueba_mp2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema prueba_mp2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `prueba_mp2` DEFAULT CHARACTER SET utf8 ;
USE `prueba_mp2` ;

-- -----------------------------------------------------
-- Table `prueba_mp2`.`permiso`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `prueba_mp2`.`permiso` ;

CREATE TABLE IF NOT EXISTS `prueba_mp2`.`permiso` (
  `id_permiso` INT NOT NULL AUTO_INCREMENT,
  `nombre_permiso` VARCHAR(40) NULL,
  PRIMARY KEY (`id_permiso`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `prueba_mp2`.`rol`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `prueba_mp2`.`rol` ;

CREATE TABLE IF NOT EXISTS `prueba_mp2`.`rol` (
  `id_rol` INT NOT NULL AUTO_INCREMENT,
  `nombre_rol` VARCHAR(30) NOT NULL,
  `fk_id_permiso` INT NOT NULL,
  PRIMARY KEY (`id_rol`),
  INDEX `fk_rol_permiso1_idx` (`fk_id_permiso` ASC) ,
  CONSTRAINT `fk_rol_permiso1`
    FOREIGN KEY (`fk_id_permiso`)
    REFERENCES `prueba_mp2`.`permiso` (`id_permiso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `prueba_mp2`.`comuna`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `prueba_mp2`.`comuna` ;

CREATE TABLE IF NOT EXISTS `prueba_mp2`.`comuna` (
  `id_comuna` INT NOT NULL AUTO_INCREMENT,
  `comuna` VARCHAR(45) NULL,
  PRIMARY KEY (`id_comuna`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `prueba_mp2`.`usuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `prueba_mp2`.`usuario` ;

CREATE TABLE IF NOT EXISTS `prueba_mp2`.`usuario` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `nombre_usuario` VARCHAR(50) NULL,
  `apellido_usuario` VARCHAR(50) NULL,
  `celular` INT NULL,
  `correo` VARCHAR(200) NULL,
  `clave` VARCHAR(100) NULL,
  `direccion` VARCHAR(100) NULL,
  `fk_id_rol` INT NOT NULL,
  `fk_id_comuna` INT NOT NULL,
  PRIMARY KEY (`id_usuario`),
  INDEX `fk_usuario_rol1_idx` (`fk_id_rol` ASC) ,
  INDEX `fk_usuario_comuna` (`fk_id_comuna` ASC) ,
  CONSTRAINT `fk_usuario_rol1`
    FOREIGN KEY (`fk_id_rol`)
    REFERENCES `prueba_mp2`.`rol` (`id_rol`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuario_comuna`
    FOREIGN KEY (`fk_id_comuna`)
    REFERENCES `prueba_mp2`.`comuna` (`id_comuna`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;