-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: class_attendance_system_v2
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `attendances`
--

DROP TABLE IF EXISTS `attendances`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendances` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time DEFAULT NULL,
  `student_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `attendances_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=296 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendances`
--

LOCK TABLES `attendances` WRITE;
/*!40000 ALTER TABLE `attendances` DISABLE KEYS */;
INSERT INTO `attendances` VALUES (1,'2024-06-21','04:13:45',1),(2,'2024-07-13','04:50:43',1),(3,'2024-07-13','04:50:44',1),(4,'2024-07-13','04:50:46',1),(5,'2024-07-13','04:50:47',1),(6,'2024-07-13','04:50:59',1),(7,'2024-07-13','04:51:04',1),(8,'2024-07-13','04:51:05',1),(9,'2024-07-13','04:55:02',4),(10,'2024-07-13','04:55:04',4),(11,'2024-07-13','04:55:05',4),(12,'2024-07-13','04:55:06',4),(13,'2024-07-13','04:55:07',4),(14,'2024-07-18','16:39:15',2),(15,'2024-07-18','16:39:16',2),(16,'2024-07-18','16:39:17',2),(17,'2024-07-18','16:39:18',2),(18,'2024-07-18','16:39:36',2),(19,'2024-07-18','16:39:37',2),(20,'2024-07-18','16:39:38',2),(21,'2024-07-18','16:39:39',2),(22,'2024-07-18','16:39:39',2),(23,'2024-07-18','16:39:40',2),(24,'2024-07-18','16:41:31',3),(25,'2024-07-18','16:41:32',2),(26,'2024-07-18','16:41:32',3),(27,'2024-07-18','16:41:33',3),(28,'2024-07-18','16:41:34',3),(29,'2024-07-18','16:41:34',3),(30,'2024-07-18','16:41:37',3),(31,'2024-07-18','16:41:38',3),(32,'2024-07-18','16:41:40',2),(33,'2024-07-18','16:41:40',3),(34,'2024-07-18','16:41:40',2),(35,'2024-07-18','16:41:41',3),(36,'2024-07-18','16:41:42',3),(37,'2024-07-18','16:41:43',3),(38,'2024-07-18','16:41:43',3),(39,'2024-07-18','16:41:44',3),(40,'2024-07-18','16:41:45',3),(41,'2024-07-18','16:41:46',3),(42,'2024-07-18','16:41:47',3),(43,'2024-07-18','16:41:47',3),(44,'2024-07-18','16:41:48',3),(45,'2024-07-18','16:41:49',3),(46,'2024-07-18','16:41:50',3),(47,'2024-07-18','16:41:51',2),(48,'2024-07-18','16:41:54',3),(49,'2024-07-18','16:41:55',3),(50,'2024-07-18','16:41:56',3),(51,'2024-07-18','16:41:58',3),(52,'2024-07-18','16:41:58',2),(53,'2024-07-18','16:41:59',3),(54,'2024-07-18','16:42:00',3),(55,'2024-07-18','16:42:02',3),(56,'2024-07-18','16:42:02',1),(57,'2024-07-18','16:42:04',3),(58,'2024-07-18','16:43:39',3),(59,'2024-07-18','16:43:40',3),(60,'2024-07-18','16:43:41',3),(61,'2024-07-18','16:43:42',3),(62,'2024-07-18','16:43:46',3),(63,'2024-07-18','16:43:46',3),(64,'2024-07-18','16:43:47',3),(65,'2024-07-18','16:43:48',3),(66,'2024-07-18','16:43:49',3),(67,'2024-07-18','16:43:53',2),(68,'2024-07-18','16:43:54',3),(69,'2024-07-18','16:43:55',3),(70,'2024-07-18','16:43:55',3),(71,'2024-07-18','16:43:56',3),(72,'2024-07-18','16:43:57',3),(73,'2024-07-18','16:43:58',3),(74,'2024-07-18','16:43:59',3),(75,'2024-07-18','16:44:03',2),(76,'2024-07-18','16:44:04',3),(77,'2024-07-18','16:44:04',2),(78,'2024-07-18','16:44:05',2),(79,'2024-07-18','16:44:06',1),(80,'2024-07-18','16:44:06',2),(81,'2024-07-18','16:44:07',2),(82,'2024-07-18','16:44:09',3),(83,'2024-07-18','16:44:09',3),(84,'2024-07-18','16:44:09',3),(85,'2024-07-18','16:44:10',3),(86,'2024-07-18','16:44:11',3),(87,'2024-07-18','16:44:12',3),(88,'2024-07-18','16:44:13',2),(89,'2024-07-18','16:44:14',2),(90,'2024-07-18','16:44:14',2),(91,'2024-07-18','16:44:15',2),(92,'2024-07-18','16:44:17',3),(93,'2024-07-18','16:44:18',3),(94,'2024-07-18','16:44:18',2),(95,'2024-07-18','16:44:19',2),(96,'2024-07-18','16:44:20',2),(97,'2024-07-18','16:44:21',2),(98,'2024-07-18','16:44:21',3),(99,'2024-07-18','16:44:22',2),(100,'2024-07-18','16:44:23',2),(101,'2024-07-18','16:44:23',3),(102,'2024-07-18','16:44:25',2),(103,'2024-07-18','16:44:25',3),(104,'2024-07-18','16:44:25',2),(105,'2024-07-18','16:44:26',2),(106,'2024-07-18','16:44:27',2),(107,'2024-07-18','16:44:28',2),(108,'2024-07-18','16:44:28',2),(109,'2024-07-18','16:44:30',2),(110,'2024-07-18','16:44:31',2),(111,'2024-07-18','16:44:32',2),(112,'2024-07-18','16:44:34',2),(113,'2024-07-18','16:44:35',2),(114,'2024-07-18','16:44:35',3),(115,'2024-07-18','16:44:36',3),(116,'2024-07-18','16:44:36',2),(117,'2024-07-18','16:44:38',3),(118,'2024-07-18','16:44:38',2),(119,'2024-07-18','16:44:39',2),(120,'2024-07-18','16:44:39',2),(121,'2024-07-18','16:44:40',2),(122,'2024-07-18','16:44:41',2),(123,'2024-07-18','16:44:42',2),(124,'2024-07-18','16:44:42',2),(125,'2024-07-18','16:44:43',2),(126,'2024-07-18','16:44:44',2),(127,'2024-07-18','16:44:44',2),(128,'2024-07-18','16:44:45',2),(129,'2024-07-18','16:44:46',2),(130,'2024-07-18','16:44:47',2),(131,'2024-07-18','16:44:47',2),(132,'2024-07-18','16:44:48',2),(133,'2024-07-18','16:44:49',2),(134,'2024-07-18','16:44:49',2),(135,'2024-07-18','16:44:51',2),(136,'2024-07-18','16:44:51',3),(137,'2024-07-18','16:44:52',2),(138,'2024-07-18','16:44:52',3),(139,'2024-07-18','16:44:53',2),(140,'2024-07-18','16:44:53',2),(141,'2024-07-18','16:44:54',3),(142,'2024-07-18','16:44:56',3),(143,'2024-07-18','16:45:02',1),(144,'2024-07-18','16:45:03',1),(145,'2024-07-18','23:58:01',1),(146,'2024-07-18','23:58:03',1),(147,'2024-07-18','23:58:04',1),(148,'2024-07-18','23:58:04',1),(149,'2024-07-18','23:58:05',1),(150,'2024-07-18','23:58:06',1),(151,'2024-07-19','11:50:52',1),(152,'2024-07-19','11:50:53',1),(153,'2024-07-19','11:50:53',1),(154,'2024-07-19','11:50:55',1),(155,'2024-07-19','14:56:49',4),(156,'2024-07-19','14:56:50',1),(157,'2024-07-19','14:56:51',3),(158,'2024-07-19','14:56:55',1),(159,'2024-07-19','14:56:56',1),(160,'2024-07-19','14:56:57',1),(161,'2024-07-19','14:56:59',1),(162,'2024-07-19','14:57:00',1),(163,'2024-07-19','14:57:01',1),(164,'2024-07-19','14:57:03',1),(165,'2024-07-19','14:57:04',1),(166,'2024-07-19','14:57:05',1),(167,'2024-07-19','14:57:05',1),(168,'2024-07-19','14:57:06',1),(169,'2024-07-19','14:57:07',1),(170,'2024-07-19','14:57:08',1),(171,'2024-07-19','14:57:10',1),(172,'2024-07-19','14:57:33',1),(173,'2024-07-19','14:57:41',1),(174,'2024-07-19','14:57:43',1),(175,'2024-07-19','14:57:45',3),(176,'2024-07-19','14:57:49',1),(177,'2024-07-19','14:57:50',1),(178,'2024-07-19','14:57:56',1),(179,'2024-07-19','14:57:59',3),(180,'2024-07-19','14:58:02',1),(181,'2024-07-19','14:58:05',1),(182,'2024-07-19','14:58:07',1),(183,'2024-07-22','11:23:35',1),(184,'2024-07-22','11:23:37',1),(185,'2024-07-22','11:23:37',1),(186,'2024-07-22','11:23:38',1),(187,'2024-07-22','11:23:39',1),(188,'2024-07-22','11:26:35',1),(264,'2024-07-22','17:50:46',1),(265,'2024-07-22','17:50:50',1),(266,'2024-07-22','17:50:51',1),(267,'2024-07-22','17:50:51',1),(268,'2024-07-22','17:50:52',1),(269,'2024-07-22','17:50:56',1),(270,'2024-07-22','17:51:03',1),(271,'2024-07-23','01:57:38',1),(272,'2024-07-23','01:57:39',1),(273,'2024-07-23','01:57:40',1),(274,'2024-07-23','01:57:41',1),(275,'2024-07-23','01:57:41',1),(276,'2024-07-24','01:32:22',1),(277,'2024-07-24','01:32:28',1),(278,'2024-07-24','01:32:30',1),(279,'2024-07-24','01:32:31',1),(280,'2024-07-24','01:32:33',1),(281,'2024-07-24','01:32:34',1),(282,'2024-07-24','01:32:36',1),(283,'2024-07-24','01:32:38',1),(284,'2024-07-24','01:32:40',1),(285,'2024-07-24','01:32:41',1),(286,'2024-07-24','01:38:23',1),(287,'2024-07-24','01:38:28',1),(288,'2024-07-24','01:38:33',1),(289,'2024-07-24','01:38:34',1),(290,'2024-07-24','01:38:38',1),(291,'2024-07-24','01:40:58',1),(292,'2024-07-24','01:40:59',1),(293,'2024-07-24','01:41:02',1),(294,'2024-07-24','01:41:07',1),(295,'2024-07-24','01:41:14',1);
/*!40000 ALTER TABLE `attendances` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `course_code` varchar(15) NOT NULL,
  `course_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `course_code` (`course_code`),
  UNIQUE KEY `course_name` (`course_name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES (1,'CSC211','Computer Organization and Architecture'),(2,'CSC301','Operating Systems'),(3,'ELE201','Circuit Theory'),(4,'ELE311','Digital Electronics'),(5,'ELE401','Control Systems'),(6,'COE371','Linear Electronics'),(7,'COE271','Semiconductor Devices');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lecturer_courses`
--

DROP TABLE IF EXISTS `lecturer_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lecturer_courses` (
  `lecturer_id` int DEFAULT NULL,
  `course_id` int DEFAULT NULL,
  KEY `lecturer_id` (`lecturer_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `lecturer_courses_ibfk_1` FOREIGN KEY (`lecturer_id`) REFERENCES `lecturers` (`id`),
  CONSTRAINT `lecturer_courses_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lecturer_courses`
--

LOCK TABLES `lecturer_courses` WRITE;
/*!40000 ALTER TABLE `lecturer_courses` DISABLE KEYS */;
INSERT INTO `lecturer_courses` VALUES (1,1),(1,2),(2,3),(2,4),(3,3),(3,5),(4,2),(4,4),(5,3),(5,4),(6,5),(6,2),(7,6),(7,7);
/*!40000 ALTER TABLE `lecturer_courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lecturers`
--

DROP TABLE IF EXISTS `lecturers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lecturers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `email` varchar(45) NOT NULL,
  `phone` int NOT NULL,
  `address` varchar(45) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lecturers`
--

LOCK TABLES `lecturers` WRITE;
/*!40000 ALTER TABLE `lecturers` DISABLE KEYS */;
INSERT INTO `lecturers` VALUES (1,'Bob','Titan','nharnharyhaw984@gmail.com',506609243,'Obuasi','scrypt:32768:8:1$tB0R2jjOg89Dxadu$9bb9349efb548d75874ca34008aab36f220eef9fa2697ed2fce37cd062699437dcb49b3a2bce6d0fd114e772f8bd2b1cda3a8ed0ad099fc2bf8dd382a7c06da5'),(2,'Alice','Wonderland','awonderland@gmail.com',557894321,'Kumasi','scrypt:32768:8:1$fNestkNj6hIuHOB0$b23f1216abd4bc30a378e5242cff8fd5473c0b5ae02300b3537be83b610874fed284d5bcb95453bab9e4e104c663f2cce0f67591c4e2027c8c0570c34844e87b'),(3,'Charlie','Chaplin','cchaplin@gmail.com',567891234,'Takoradi','scrypt:32768:8:1$09gAivGLhHCL2uB2$ec6f64f9d937bd44f582ea5a264f08371b4dfce601124f87e77e06ccc2357ad436aef870b9c6e6188c849c620731676edccc25ce94e8ad2bed5b9579c33016fa'),(4,'David','Livingstone','dlivingstone@gmail.com',577890321,'Tamale','scrypt:32768:8:1$CKQFFG9B9TnamHMS$c55f6c35dc7ee7022137af31660a8bcf60306aa2044d73a3b4362d394d6767f57caeec22c77b93750602665fa16e8814753e11bd21b841f6531fa2e029b14ef6'),(5,'Emily','Bronte','ebronte@gmail.com',587893210,'Cape Coast','scrypt:32768:8:1$QIQnqj9D9wiAgkck$8c951aa1752c4047e61b450a07f0066a5fe50ef2746d37359e3d97f7c4c15c720df026f08d09940ae75b7f479e4e82a5f81bff215fd5afd64f6082eda637f714'),(6,'Frank','Sinatra','fsinatra@gmail.com',597812345,'Accra','scrypt:32768:8:1$1mRKfroLGyCys70w$3a30fc67ff1bd74c7d660be49143ea9595f33b5437b86de4408a6fdf172fbab8de9b65e1cc9e8f4518de4a099904ae01e22688dd6546507701439e4a377f4280'),(7,'Benjamin','Kommey','nokommey2017@gmail.com',507703286,'Berlin, Germany','scrypt:32768:8:1$dzMXvpTogsMBo8dc$35170b4e316894e63de549d4328e24abff63f4bf49b26e84306d4653a36888e79417ec7ce00ef3e57cf4bdbb0dfc3a1c854237e38875d9314272b2a6e478b127');
/*!40000 ALTER TABLE `lecturers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registered_courses`
--

DROP TABLE IF EXISTS `registered_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registered_courses` (
  `student_id` int DEFAULT NULL,
  `course_id` int DEFAULT NULL,
  KEY `student_id` (`student_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `registered_courses_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`),
  CONSTRAINT `registered_courses_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registered_courses`
--

LOCK TABLES `registered_courses` WRITE;
/*!40000 ALTER TABLE `registered_courses` DISABLE KEYS */;
INSERT INTO `registered_courses` VALUES (1,1),(1,2),(1,5),(2,2),(2,3),(2,5),(3,1),(3,5),(3,3),(4,4),(4,5),(4,3),(1,6),(1,7),(2,6),(2,7),(3,6),(3,7);
/*!40000 ALTER TABLE `registered_courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `email` varchar(45) NOT NULL,
  `programme` varchar(45) NOT NULL,
  `index_number` int NOT NULL,
  `address` varchar(45) NOT NULL,
  `phone` int NOT NULL,
  `image_url` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `index_number` (`index_number`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `image_url` (`image_url`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Magnus','Tetteh','mt@gmail.com','Computer Engineering',3040621,'Brunei',245612314,'Images/Magnus_Tetteh.jpg'),(2,'Daniel','Otchere','Do@gmail.com','Computer Engineering',3045223,'Ayeduase',552647894,'Images/Daniel_Otchere.jpg'),(3,'Marvin','Selasi','Ms@gmail.com','Electrical Engineering',3145223,'Ayeduase',541237865,'Images/Marvin_Selasi.jpg'),(4,'Bill','Gates','gates123@gmail.com','Electrical Engineering',3045237,'Seattle',208241234,'Images/Bill_Gates_photo.jpg');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-27  1:37:22
