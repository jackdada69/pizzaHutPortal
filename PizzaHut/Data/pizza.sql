-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: pizza
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('admin','admin');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `pid` int(11) NOT NULL,
  `pname` varchar(30) DEFAULT NULL,
  `description` varchar(150) DEFAULT NULL,
  `vnv` varchar(7) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `size` varchar(10) DEFAULT NULL,
  `cost` int(11) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Margherita','(Classic Cheese)','V','World Famous Pan Pizzas','Personal',100),(2,'Margherita','(Classic Cheese)','V','World Famous Pan Pizzas','Medium',245),(3,'Double Cheese','(Extra Cheese On Cheese)','V','World Famous Pan Pizzas','Personal',170),(4,'Double Cheese','(Extra Cheese On Cheese)','V','World Famous Pan Pizzas','Medium',340),(5,'Veggie Feast','(Capsicum, Onion, Sweet Corn)','V','World Famous Pan Pizzas','Personal',170),(6,'Veggie Feast','(Capsicum, Onion, Sweet Corn)','V','World Famous Pan Pizzas','Medium',340),(7,'Rawalpindi Chana','(Chana, Onion, Green Capsicum, Tomato in a Tandoori Sauce)','V','World Famous Pan Pizzas','Personal',170),(8,'Rawalpindi Chana','(Chana, Onion, Green Capsicum, Tomato in a Tandoori Sauce)','V','World Famous Pan Pizzas','Medium',340),(9,'Tandoori Paneer','(Paneer, Onion, Capsicum, Red Paprika, Tomato in a Tandoori Sauce)','V','World Famous Pan Pizzas','Personal',230),(10,'Tandoori Paneer','(Paneer, Onion, Capsicum, Red Paprika, Tomato in a Tandoori Sauce)','V','World Famous Pan Pizzas','Medium',425),(11,'Veggie Lover','(Onion, Capsicum, Mushroom, Tomato, Red Paprika)','V','World Famous Pan Pizzas','Personal',230),(12,'Veggie Lover','(Onion, Capsicum, Mushroom, Tomato, Red Paprika)','V','World Famous Pan Pizzas','Medium',425),(13,'Country Feast','(Onion, Capsicum, Mushroom, Sweet Corn, Tomato))','V','World Famous Pan Pizzas','Personal',230),(14,'Country Feast','(Onion, Capsicum, Mushroom, Sweet Corn, Tomato)','v','World Famous Pan Pizzas','Medium',425),(15,'Veggie Supreme','(Onion, Capsicum, Mushroom, Red Paprika, Black Olives, Sweet Corn)','V','World Famous Pan Pizzas','Personal',265),(16,'Veggie Supreme','(Onion, Capsicum, Mushroom, Red Paprika, Black Olives, Sweet Corn)','V','World Famous Pan Pizzas','Medium',480),(17,'Paneer Vegorama','(Paneer, Onion, Capsicum, Black Olives, Red Paprika)','V','World Famous Pan Pizzas','Personal',265),(18,'Paneer Vegorama','(Paneer, Onion, Capsicum, Black Olives, Red Paprika)','V','World Famous Pan Pizzas','Medium',480),(19,'Exotica','(Red Capsicum, Green Capsicum, Baby Corn, Black Olives, Jalapeno)','V','World Famous Pan Pizzas','Personal',265),(20,'Exotica','(Red Capsicum, Green Capsicum, Baby Corn, Black Olives, Jalapeno)','V','World Famous Pan Pizzas','Personal',480),(21,'Chicken Sausage','(Chicken Sausage & Onion)','NV','World Famous Pan Pizzas','Personal',170),(22,'Chicken Sausage','(Chicken Sausage & Onion)','NV','World Famous Pan Pizzas','Medium',340),(23,'Chick N Spicy','(Chicken Hot & Chilli, Capsicum, Mushroom)','NV','World Famous Pan Pizzas','Personal',230),(24,'Chick N Spicy','(Chicken Hot & Chilli, Capsicum, Mushroom)','NV','World Famous Pan Pizzas','Medium',425),(25,'Keema Masala','(Chicken Keema, Onion, Capsicum in a Tandoori Sauce)','NV','World Famous Pan Pizzas','Personal',230),(26,'Keema Masala','(Chicken Keema, Onion, Capsicum in a Tandoori Sauce)','NV','World Famous Pan Pizzas','Medium',425),(27,'Chicken Pepperoni','(Chicken Pepperoni & Cheese)','NV','World Famous Pan Pizzas','Personal',265),(28,'Chicken Pepperoni','(Chicken Pepperoni & Cheese)','NV','World Famous Pan Pizzas','Medium',480),(29,'Chicken Tikka','(Chicken Tikka, Onion, Tomato in a Tandoori Sauce)','NV','World Famous Pan Pizzas','Personal',265),(30,'Chicken Tikka','(Chicken Tikka, Onion, Tomato in a Tandoori Sauce)','NV','World Famous Pan Pizzas','Medium',480),(31,'Chicken Double Trouble','(Chicken Sausage, Chicken Tikka, Capsicum, Jalapeno, Red Paprika)','NV','World Famous Pan Pizzas','Personal',265),(32,'Chicken Double Trouble','(Chicken Sausage, Chicken Tikka, Capsicum, Jalapeno, Red Paprika)','NV','World Famous Pan Pizzas','Medium',480),(33,'Chicken Supreme','(Chicken Tikka, Chicken Hot & Chilli, Chicken Meatball)','NV','World Famous Pan Pizzas','Personal',300);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `norder`
--

DROP TABLE IF EXISTS `norder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `norder` (
  `ono` int(11) DEFAULT NULL,
  `pname` varchar(30) DEFAULT NULL,
  `size` varchar(10) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `mode` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `norder`
--

LOCK TABLES `norder` WRITE;
/*!40000 ALTER TABLE `norder` DISABLE KEYS */;
INSERT INTO `norder` VALUES (1,'Double Cheese','Personal',2,'Credit Card');
/*!40000 ALTER TABLE `norder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordhst`
--

DROP TABLE IF EXISTS `ordhst`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordhst` (
  `date` varchar(20) DEFAULT NULL,
  `ono` int(11) NOT NULL,
  `disc` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  PRIMARY KEY (`ono`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordhst`
--

LOCK TABLES `ordhst` WRITE;
/*!40000 ALTER TABLE `ordhst` DISABLE KEYS */;
INSERT INTO `ordhst` VALUES ('2020-01-18',1,50,290);
/*!40000 ALTER TABLE `ordhst` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'pizza'
--

--
-- Dumping routines for database 'pizza'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-19  0:02:33
