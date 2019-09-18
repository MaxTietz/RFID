-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 18. Sep 2019 um 10:24
-- Server Version: 5.5.16
-- PHP-Version: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Datenbank: `rfid`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `action`
--

CREATE TABLE IF NOT EXISTS `action` (
  `ActionID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Description` text NOT NULL,
  `CreatedAt` date NOT NULL,
  `Path` text NOT NULL,
  `UpdatedAt` date NOT NULL,
  `Enabled` int(11) NOT NULL,
  PRIMARY KEY (`ActionID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `rfid`
--

CREATE TABLE IF NOT EXISTS `rfid` (
  `RFID` int(11) NOT NULL,
  `UserID` int(11) NOT NULL,
  PRIMARY KEY (`RFID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `rfidaction`
--

CREATE TABLE IF NOT EXISTS `rfidaction` (
  `ActionID` int(11) NOT NULL,
  `RFID` int(11) NOT NULL,
  PRIMARY KEY (`ActionID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `UserID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `LastName` text NOT NULL,
  `Email` text NOT NULL,
  `Username` text NOT NULL,
  `Password` text NOT NULL,
  `CreatedAt` date NOT NULL,
  `UpdatedAt` date NOT NULL,
  `Enabled` int(11) NOT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
