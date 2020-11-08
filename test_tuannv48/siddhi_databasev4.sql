DROP SCHEMA IF EXISTS `performace_threshold`;

CREATE DATABASE  IF NOT EXISTS `performace_threshold` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `performace_threshold`;
-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 172.20.3.73    Database: performace_threshold
-- ------------------------------------------------------
-- Server version	5.7.27-30-57-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alert`
--

DROP TABLE IF EXISTS `performace_threshold`.`alert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `performace_threshold`.`alert` (
  `alertid` varchar(45) NOT NULL,
  `alarmRaisedTime` bigint(8) DEFAULT '0',
  `alarmChangedTime` bigint(8) DEFAULT '0',
  `alarmClearedTime` bigint(8) DEFAULT '0',
  `state` varchar(45) DEFAULT 'null',
  `perceivedSeverity` varchar(45) DEFAULT 'null',
  `eventTime` bigint(8) DEFAULT '0',
  `eventType` varchar(45) DEFAULT 'null',
  `faultType` varchar(45) DEFAULT 'null',
  `probableCause` varchar(45) DEFAULT 'null',
  `isRootCause` tinyint(1) DEFAULT '0',
  `correlatedAlarmId` int(11) DEFAULT '0',
  `faultDetails` varchar(45) DEFAULT 'null',
  `deviceid` int(11) NOT NULL,
  `metricid` int(11) NOT NULL,
  PRIMARY KEY (`alertid`),
  UNIQUE KEY `idalert_UNIQUE` (`alertid`),
  KEY `fk_alert_1_idx` (`deviceid`),
  KEY `fk_alert_2_idx` (`metricid`),
  CONSTRAINT `fk_alert_1` FOREIGN KEY (`deviceid`) REFERENCES `devicedetails` (`did`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_alert_2` FOREIGN KEY (`metricid`) REFERENCES `metricdetails` (`metricid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alert`
--


--
-- Table structure for table `devicedetails`
--

DROP TABLE IF EXISTS `performace_threshold`.`devicedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `performace_threshold`.`devicedetails` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `mode` varchar(255) DEFAULT NULL,
  `status` text,
  `errorstring` varchar(255) DEFAULT NULL,
  `timeinterval` varchar(255) DEFAULT NULL,
  `last_updated_on` datetime DEFAULT NULL,
  `isprofilebased` tinyint(1) DEFAULT NULL,
  `fetch_rules` tinyint(1) DEFAULT NULL,
  `ip` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devicedetails`
--


--
-- Table structure for table `groupalerts`
--

DROP TABLE IF EXISTS `performace_threshold`.`groupalerts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `performace_threshold`.`groupalerts` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(255) DEFAULT NULL,
  `group_desc` text,
  PRIMARY KEY (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groupalerts`
--



--
-- Table structure for table `groupdevicepolledatatemplate`
--

DROP TABLE IF EXISTS `performace_threshold`.`groupdevicepolledatatemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `performace_threshold`.`groupdevicepolledatatemplate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `groupdevices_group_id` int(11) NOT NULL,
  `polldatatemplate_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`groupdevices_group_id`),
  KEY `fk_groupdevicepolledatatemplate_groupdevices1_idx` (`groupdevices_group_id`),
  KEY `fk_groupdevicepolledatatemplate_polldatatemplate1_idx` (`polldatatemplate_id`),
  CONSTRAINT `fk_groupdevicepolledatatemplate_groupdevices1` FOREIGN KEY (`groupdevices_group_id`) REFERENCES `groupdevices` (`group_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_groupdevicepolledatatemplate_polldatatemplate1` FOREIGN KEY (`polldatatemplate_id`) REFERENCES `polldatatemplate` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groupdevicepolledatatemplate`
--


--
-- Table structure for table `groupdevices`
--

DROP TABLE IF EXISTS `performace_threshold`.`groupdevices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `performace_threshold`.`groupdevices` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(255) DEFAULT NULL,
  `group_desc` text,
  `is_manual` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groupdevices`
--



--
-- Table structure for table `groupdevicesdevicedetails`
--

DROP TABLE IF EXISTS `performace_threshold`.`groupdevicesdevicedetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `performace_threshold`.`groupdevicesdevicedetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `devicedetail_did` int(11) NOT NULL,
  `groupdevice_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`devicedetail_did`,`groupdevice_id`),
  KEY `fk_groupdevicesdevicedetails_devicedetails1_idx` (`devicedetail_did`),
  KEY `fk_groupdevicesdevicedetails_groupdevices1_idx` (`groupdevice_id`),
  CONSTRAINT `fk_groupdevicesdevicedetails_devicedetails1` FOREIGN KEY (`devicedetail_did`) REFERENCES `devicedetails` (`did`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_groupdevicesdevicedetails_groupdevices1` FOREIGN KEY (`groupdevice_id`) REFERENCES `groupdevices` (`group_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groupdevicesdevicedetails`
--


--
-- Table structure for table `metricdetails`
--

DROP TABLE IF EXISTS `performace_threshold`.`metricdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `performace_threshold`.`metricdetails` (
  `metricid` int(11) NOT NULL AUTO_INCREMENT,
  `metricname` text,
  `description` text,
  `displayname` text,
  `metrictype` int(11) DEFAULT NULL,
  `datatype` varchar(255) DEFAULT NULL,
  `protocolid` int(11) NOT NULL,
  PRIMARY KEY (`metricid`),
  KEY `fk_metricdetails_protocoldetails1_idx` (`protocolid`),
  CONSTRAINT `fk_metricdetails_protocoldetails1` FOREIGN KEY (`protocolid`) REFERENCES `protocoldetails` (`protocolid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `metricdetails`
--



--
-- Table structure for table `polldatatemplate`
--

DROP TABLE IF EXISTS `performace_threshold`.`polldatatemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `performace_threshold`.`polldatatemplate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `agent` varchar(255) DEFAULT NULL,
  `period` int(11) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `oid` varchar(255) DEFAULT NULL,
  `threshold_activate` tinyint(1) DEFAULT NULL,
  `protocol` varchar(255) DEFAULT NULL,
  `metricdetail_id` int(11) NOT NULL,
  `threshold_list_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`metricdetail_id`),
  KEY `fk_polldatatemplate_metricdetails1_idx` (`metricdetail_id`),
  KEY `fk_polldatatemplate_threshold_lists1_idx` (`threshold_list_id`),
  CONSTRAINT `fk_polldatatemplate_metricdetails1` FOREIGN KEY (`metricdetail_id`) REFERENCES `metricdetails` (`metricid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_polldatatemplate_threshold_lists1` FOREIGN KEY (`threshold_list_id`) REFERENCES `threshold_lists` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polldatatemplate`
--


--
-- Table structure for table `polleddata`
--

DROP TABLE IF EXISTS `performace_threshold`.`polleddata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `performace_threshold`.`polleddata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `agent` varchar(255) DEFAULT NULL,
  `period` int(11) DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `threshold_activate` tinyint(1) DEFAULT NULL,
  `devicedetails_did` int(11) NOT NULL,
  `groupdevices_group_id` int(11) NOT NULL,
  `threshold_lists_id` int(11) NOT NULL,
  `metricdetails_metricid` int(11) NOT NULL,
  PRIMARY KEY (`id`,`devicedetails_did`,`groupdevices_group_id`,`threshold_lists_id`,`metricdetails_metricid`),
  KEY `fk_polleddata_devicedetails1_idx` (`devicedetails_did`),
  KEY `fk_polleddata_groupdevices1_idx` (`groupdevices_group_id`),
  KEY `fk_polleddata_threshold_lists1_idx` (`threshold_lists_id`),
  KEY `fk_polleddata_metricdetails1_idx` (`metricdetails_metricid`),
  CONSTRAINT `fk_polleddata_devicedetails1` FOREIGN KEY (`devicedetails_did`) REFERENCES `devicedetails` (`did`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_polleddata_groupdevices1` FOREIGN KEY (`groupdevices_group_id`) REFERENCES `groupdevices` (`group_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_polleddata_metricdetails1` FOREIGN KEY (`metricdetails_metricid`) REFERENCES `metricdetails` (`metricid`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_polleddata_threshold_lists1` FOREIGN KEY (`threshold_lists_id`) REFERENCES `threshold_lists` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polleddata`
--


--
-- Table structure for table `protocoldetails`
--

DROP TABLE IF EXISTS `performace_threshold`.`protocoldetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `performace_threshold`.`protocoldetails` (
  `protocolid` int(11) NOT NULL AUTO_INCREMENT,
  `protocolname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`protocolid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `protocoldetails`
--


--
-- Table structure for table `threshold_lists`
--

DROP TABLE IF EXISTS `performace_threshold`.`threshold_lists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `performace_threshold`.`threshold_lists` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `threshold_lists`
--



--
-- Table structure for table `thresholdobjects`
--

DROP TABLE IF EXISTS `performace_threshold`.`thresholdobjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `performace_threshold`.`thresholdobjects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `kind` varchar(255) DEFAULT NULL,
  `priority` int(11) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `thresholdvalue` int(11) NOT NULL,
  `rearmvalue` int(11) DEFAULT NULL,
  `mmessage` varchar(255) DEFAULT NULL,
  `allowed` tinyint(1) DEFAULT NULL,
  `is_customize` tinyint(1) DEFAULT NULL,
  `consecutive_time` int(11) DEFAULT NULL,
  `threshold_lists_id` int(11) NOT NULL,
  `operator` varchar(45) DEFAULT NULL,
  `severity` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_thresholdobjects_threshold_lists1_idx` (`threshold_lists_id`),
  CONSTRAINT `fk_thresholdobjects_threshold_lists1` FOREIGN KEY (`threshold_lists_id`) REFERENCES `threshold_lists` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thresholdobjects`
--

