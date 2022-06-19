-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: kepegawaian
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `jabatan`
--

DROP TABLE IF EXISTS `jabatan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jabatan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama_jabatan` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jabatan`
--

LOCK TABLES `jabatan` WRITE;
/*!40000 ALTER TABLE `jabatan` DISABLE KEYS */;
INSERT INTO `jabatan` VALUES (1,'Direksi'),(2,'Direktur Utama'),(3,'Direktur'),(4,'Manager'),(5,'Supervisor'),(6,'Staff');
/*!40000 ALTER TABLE `jabatan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pegawai`
--

DROP TABLE IF EXISTS `pegawai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pegawai` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(30) NOT NULL,
  `tanggal_lahir` date NOT NULL,
  `id_jabatan` int NOT NULL,
  `jenis_kelamin` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pegawai`
--

LOCK TABLES `pegawai` WRITE;
/*!40000 ALTER TABLE `pegawai` DISABLE KEYS */;
INSERT INTO `pegawai` VALUES (1,'Rizky Hadikusumah','1997-03-16',1,'Laki-Laki'),(2,'Rina Kusdinar','1998-04-17',2,'Perempuan'),(3,'Roni Hardiyanto','1999-05-18',3,'Laki-Laki'),(4,'Renanda Nur Fitriana','2001-08-29',3,'Perempuan'),(5,'Putri Audina','1996-09-24',3,'Perempuan'),(6,'Cassandra Jelita','1997-09-26',4,'Perempuan'),(7,'Pratama Nugraha','2000-01-01',4,'Laki-Laki'),(8,'Tresno Adji','2002-07-23',4,'Laki-Laki'),(9,'Dika Sulistiono','2000-09-25',4,'Laki-Laki'),(10,'Dewi Larasati','1999-10-16',5,'Perempuan'),(11,'Yuniar Maharani','1995-06-17',5,'Perempuan'),(12,'Sri Yuliany','1999-06-16',5,'Perempuan'),(13,'Harum Ningsih','1999-05-20',5,'Perempuan'),(14,'Lita Nasution','1997-09-30',5,'Perempuan'),(15,'Faishal Tri Harjo','2000-08-20',5,'Laki-Laki'),(16,'Bagus Alamsyah','1999-11-25',5,'Laki-Laki'),(17,'Triyono Mulyadi','1997-12-28',6,'Laki-Laki'),(18,'Ilmi Krisnawati','1999-11-29',6,'Perempuan'),(19,'Terra Shapire','1997-10-26',6,'Perempuan'),(20,'Yanto Julius','1999-06-30',6,'Laki-Laki'),(21,'Asep Nugraha','2000-04-24',6,'Laki-Laki'),(22,'Aji Mutoaji','1999-03-07',6,'Laki-Laki'),(23,'Farhan Subagja','1997-08-08',6,'Laki-Laki'),(24,'Reza Tangguh Sagala','2001-05-01',6,'Laki-Laki'),(25,'Uki Mulyadi','2002-03-12',6,'Laki-Laki'),(26,'Wawan Hidayat','1997-06-30',6,'Laki-Laki'),(27,'Taufik Sulistiadi','2000-03-26',6,'Laki-Laki'),(28,'Anjas Ibrahim','1997-09-16',6,'Laki-Laki'),(29,'Ana Natalia','2001-10-29',6,'Perempuan'),(30,'Dita Bunga Harum','2003-10-27',6,'Perempuan');
/*!40000 ALTER TABLE `pegawai` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(15) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `password` varchar(25) NOT NULL,
  `token` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'kusumahadi','Rizky Hadikusumah','123','Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVU0VSTkFNRSI6Imt1c3VtYWhhZGkiLCJOQU1BIjoiUml6a3kgSGFkaWt1c3VtYWgiLCJKYW0iOiIyMDIyLTA2LTE5IDE2OjI4OjU3In0.DCeTh-OyLhzjJDUkJFGjMdIwKf8tsPImzp4j-uoKyYc'),(2,'test01','User Test','123',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-19 18:04:02
