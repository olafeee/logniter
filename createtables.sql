-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema accesslog
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema accesslog
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `accesslog` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `accesslog` ;

-- -----------------------------------------------------
-- Table `accesslog`.`request`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `accesslog`.`request` (
  `host` VARCHAR(20) NOT NULL,
  `datetime` DATETIME NOT NULL,
  `request` LONGTEXT NULL,
  `statuscode` VARCHAR(3) NULL,
  `bot` TINYINT(1) NULL,
  `os` TINYTEXT NULL,
  `platformname` TINYTEXT NULL,
  `platformversion` TINYTEXT NULL,
  `browsername` TINYTEXT NULL,
  `browserversion` TINYTEXT NULL,
  `countryname` TINYTEXT NULL,
  `countrycode` VARCHAR(2) NULL,
  `isPageview` TINYINT(1) NULL,
  PRIMARY KEY (`host`, `datetime`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `accesslog`.`dailypageviews_cache`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `accesslog`.`dailypageviews_cache` (
  `iddailypageviews_cache` INT NOT NULL,
  `daystartdate` DATETIME NULL,
  `dayenddate` DATETIME NULL,
  `pageviews` INT NULL,
  PRIMARY KEY (`iddailypageviews_cache`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `accesslog`.`weeklypageviews_cache`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `accesslog`.`weeklypageviews_cache` (
  `idweeklypageviews_cache` INT NOT NULL,
  `weekstartdate` DATETIME NULL,
  `weekenddate` DATETIME NULL,
  `pageviews` INT NULL,
  PRIMARY KEY (`idweeklypageviews_cache`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `accesslog`.`monthlypageviews_cache`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `accesslog`.`monthlypageviews_cache` (
  `idmonthlypageviews_cache` INT NOT NULL,
  `monthstartdate` DATETIME NULL,
  `monthenddate` DATETIME NULL,
  `pageviews` INT NULL,
  PRIMARY KEY (`idmonthlypageviews_cache`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `accesslog`.`yearlypageviews_cache`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `accesslog`.`yearlypageviews_cache` (
  `idyearlypageviews_cache` INT NOT NULL,
  `yearstartdate` DATETIME NULL,
  `yearenddate` DATETIME NULL,
  `pageviews` INT NULL,
  PRIMARY KEY (`idyearlypageviews_cache`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `accesslog`.`dailypageviewspercountry_cache`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `accesslog`.`dailypageviewspercountry_cache` (
  `iddailypageviewspercountry_cache` INT NOT NULL,
  `daystartdate` DATETIME NULL,
  `dayenddate` DATETIME NULL,
  `countrycode` VARCHAR(2) NULL,
  `pageviews` INT NULL,
  `totalPageviews` INT NULL,
  PRIMARY KEY (`iddailypageviewspercountry_cache`),
  INDEX `totalPageviews_idx` (`totalPageviews` ASC),
  CONSTRAINT `totalDailyPageviews`
    FOREIGN KEY (`totalPageviews`)
    REFERENCES `accesslog`.`dailypageviews_cache` (`iddailypageviews_cache`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `accesslog`.`weeklypageviewspercountry_cache`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `accesslog`.`weeklypageviewspercountry_cache` (
  `idweeklypageviewspercountry_cache` INT NOT NULL,
  `weekstartdate` DATETIME NULL,
  `weekenddate` DATETIME NULL,
  `countrycode` VARCHAR(2) NULL,
  `pageviews` INT NULL,
  `totalPageviews` INT NULL,
  PRIMARY KEY (`idweeklypageviewspercountry_cache`),
  INDEX `totalPageviews_idx` (`totalPageviews` ASC),
  CONSTRAINT `totalWeeklyPageviews`
    FOREIGN KEY (`totalPageviews`)
    REFERENCES `accesslog`.`weeklypageviews_cache` (`idweeklypageviews_cache`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `accesslog`.`monthlypageviewspercountry_cache`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `accesslog`.`monthlypageviewspercountry_cache` (
  `idmonthlypageviewspercountry_cache` INT NOT NULL,
  `monthstartdate` DATETIME NULL,
  `monthenddate` DATETIME NULL,
  `countrycode` VARCHAR(2) NULL,
  `pageviews` INT NULL,
  `totalPageviews` INT NULL,
  PRIMARY KEY (`idmonthlypageviewspercountry_cache`),
  INDEX `totalPageviews_idx` (`totalPageviews` ASC),
  CONSTRAINT `totalMonthlyPageviews`
    FOREIGN KEY (`totalPageviews`)
    REFERENCES `accesslog`.`monthlypageviews_cache` (`idmonthlypageviews_cache`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `accesslog`.`yearlypageviewspercountry_cache`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `accesslog`.`yearlypageviewspercountry_cache` (
  `idyearlypageviewspercountry_cache` INT NOT NULL,
  `yearstartdate` DATETIME NULL,
  `yearenddate` DATETIME NULL,
  `countrycode` VARCHAR(2) NULL,
  `pageviews` INT NULL,
  `totalPageviews` INT NULL,
  PRIMARY KEY (`idyearlypageviewspercountry_cache`),
  INDEX `totalPageviews_idx` (`totalPageviews` ASC),
  CONSTRAINT `totalYearlyPageviews`
    FOREIGN KEY (`totalPageviews`)
    REFERENCES `accesslog`.`yearlypageviews_cache` (`idyearlypageviews_cache`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
