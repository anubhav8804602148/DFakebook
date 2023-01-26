-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: fakebook
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$390000$pKKQsFqX4QuPj4pxz9R9Go$sedx0L+r9RA7bYz4nh4xWCuU8OqTFYX49Tx3pkN2MY0=','2023-01-26 06:59:14.899972',1,'anubhav.sharma','Anubhav','Sharma','anubhav.sharma@fakebook.com',1,1,'2023-01-24 17:52:39.000000'),(6,'pbkdf2_sha256$390000$pKKQsFqX4QuPj4pxz9R9Go$sedx0L+r9RA7bYz4nh4xWCuU8OqTFYX49Tx3pkN2MY0=',NULL,0,'AnubhavSharma','Anubhav','Sharma','anubhav.sharma@gmail.com',0,1,'2023-01-24 19:22:28.900856'),(12,'pbkdf2_sha256$390000$pKKQsFqX4QuPj4pxz9R9Go$sedx0L+r9RA7bYz4nh4xWCuU8OqTFYX49Tx3pkN2MY0=',NULL,0,'AnubhavSharma23','Anubhav','Sharma','anubhav.sharma@biharib.com',0,1,'2023-01-26 03:25:44.229585'),(13,'pbkdf2_sha256$390000$pKKQsFqX4QuPj4pxz9R9Go$sedx0L+r9RA7bYz4nh4xWCuU8OqTFYX49Tx3pkN2MY0=',NULL,0,'anubhav3sharma','','','anubhav3.sharma@gmail.com',0,1,'2023-01-26 03:51:36.748324'),(16,'pbkdf2_sha256$390000$pKKQsFqX4QuPj4pxz9R9Go$sedx0L+r9RA7bYz4nh4xWCuU8OqTFYX49Tx3pkN2MY0=','2023-01-26 03:56:37.919172',0,'anubhav4sharma','','','anubhav4.sharma@gmail.com',0,1,'2023-01-26 03:52:36.129608');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-26 12:38:34
