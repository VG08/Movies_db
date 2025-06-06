-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: imdb_db
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `movie_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `genre` varchar(100) NOT NULL,
  `release_date` date NOT NULL,
  `description` text,
  `cast` varchar(255) DEFAULT NULL,
  `rating` float DEFAULT '0',
  `likes` int DEFAULT '0',
  PRIMARY KEY (`movie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'Notting Hill','Romance','1999-05-12','William Thacker (Hugh Grant) is a London bookstore owner whose humdrum existence is thrown into romantic turmoil when famous American actress Anna Scott (Julia Roberts) appears in his shop','Hugh Grant',8.7,2),(2,'Shawshank Redemption','Drama','1994-08-12','A banker convicted of uxoricide forms a friendship over a quarter century with a hardened convict, while maintaining his innocence and trying to remain hopeful through simple compassion.','Tim Robbins',9.5,0),(3,'The Godfather','Action','1972-03-24','The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.','Marlon Brando',9.1,0),(4,'The Dark Knight','Action','2008-07-18','When a menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman, James Gordon and Harvey Dent must work together to put an end to the madness.','Christian Bale',8.9,0),(5,'12 Angry Men','Drama','1957-04-15','The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.','Henry Fonda',8.9,0),(6,'The Lord of the Rings: The Return of the King','Fantasy','2002-03-15','Gandalf and Aragorn lead the World of Men against Sauron\'s army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.','Elijah Wood',8.5,0),(7,'Forrest Gump','Comedy','1994-07-06','The history of the United States from the 1950s to the \'70s unfolds from the perspective of an Alabama man with an IQ of 75, who yearns to be reunited with his childhood sweetheart.','Tom Hanks, Robin Wright',8.7,0),(8,'The Good, the Bad and the Ugly','Adventure','1966-12-23','A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.','Clint Eastwood',8.7,0),(9,'Star Wars:- The Empire Strikes Back','Adventure','1980-05-21','After the Empire overpowers the Rebel Alliance, Luke Skywalker begins his Jedi training with Yoda. At the same time, Darth Vader and bounty hunter Boba Fett pursue his friends across the galaxy.','Mark Hamil, Harrison Ford, Carrie Fisher',8.66667,0),(10,'The Matrix','Sci-Fi','1999-03-31','When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.','Keanu Reeves, Carrie-Anne Moss',9.25,2),(11,'Stree 2','Horror','2024-08-15','The town of Chanderi is being haunted again. This time, women are mysteriously abducted by a terrifying headless entity. Once again, it is up to Vicky and his friends to save their town and loved ones.','Rajkumar Rao, Shraddha Kapoor, Aparshakti  Khurrana',7.9,0),(12,'3 Idiots','Comedy','2009-12-25','Two friends are searchng for their long lost companion. They revisit their college days and recall the memories of thei friend who inspired them to think differently, even as the rest of the world called them \'idiots\'.','Aamir Khan, Madhavan, Sharman Joshi',8.7,0),(13,'Hindi Medium','Comedy','2017-05-19','Raj and Mita yearn to get Pia, their daughter, educated from a reputed school. When they learn that their background is holding her back, they do everything to ensure that she gets into the school.','Irrfan Khan, Saba Qamar',8.9,0),(14,'Krrish 3','Action','2013-11-01','Krrish and his father must defeat human-animal mutants created by an evil genius, Kaal, who is hell-bent on destroying the world. His vile army is led by a chameleon mutant, Kaya.','Hrithik Roshan, Kangana Ranaut',6.9,0),(15,'Star Wars Episode IV','Sci-Fi','1978-07-01','Luke Skywalker joins forces with a Jedi Knght, a pilot, a Wookiee and two droids to save the galaxy from the Empire\'s world-destroying battle station, while attempting to rescue Princess Leia from the mysterious Darth Vader.','Harrisson Ford, Mark Hamil, Carrie Fisher',0,0),(17,'DDLJ','Romance','1990-12-02','dsfsfa','Shahrukh Khan',0,0);
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `review_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `movie_id` int DEFAULT NULL,
  `review_text` text,
  `rating` float NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`review_id`),
  KEY `user_id` (`user_id`),
  KEY `movie_id` (`movie_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`movie_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,1,1,'Great Movie, with very great acting by Hugh Grant as well as Julia Roberts, amazing chemistry',8.7,'2024-10-20 13:33:06'),(2,1,1,'nice',8.7,'2024-10-22 05:21:47'),(3,1,2,'\"The Shawshank Redemption\" is a cinematic masterpiece that has stood the test of time since its release in 1994. Directed by Frank Darabont and based on Stephen King\'s novella, this film is a testament to the power of storytelling and the indomitable human spirit.',9.5,'2024-12-02 17:41:33'),(4,1,2,'\"The Shawshank Redemption\" is a timeless masterpiece that transcends the boundaries of genre and leaves a profound impact on its audience. Adapted from Stephen King\'s novella, this film is a testament to the power of hope, resilience, and the human spirit.',8.5,'2024-12-02 17:48:20'),(5,1,4,'The Dark Knight is Christopher Nolan\'s magnum opus and a gripping, unforgettable thrill ride from start to finish.',8.9,'2024-12-02 17:51:26'),(6,4,4,'Honestly one of the worst movies ever made by Christopher Nolan',4.5,'2024-12-02 17:55:17'),(7,4,3,'I have seen many amazing movies, as well as some clunkers, but The Godfather was beyond amazing. There are so many images, details and scenes that I seriously cannot get out of my head since watching it for the first time just nine hours ago.',9.1,'2024-12-02 17:55:48'),(8,4,5,'12 Angry Men was my first black and white movie which I sat through from the start till the end. Personally, I found the movie intriguing - even though I was watching it from a third person\'s perspective, there were many moments where I resonated deeply with some of the characters and felt the emotions they were probably feeling during that point of negotiation.',8.9,'2024-12-02 17:57:40'),(9,1,5,'There are a few wonderful courtroom dramas out there, Anatomy of a Murder, To Kill a Mockingbird and Witness for the Prosecution immediately springing to mind. 12 Angry Men is so brilliant, it could very well be the definitive courtroom drama on film. Sidney Lumet\'s direction is masterly',8.9,'2024-12-02 18:00:08'),(10,1,3,'When using the word \'epic\' one should never use it lightly where movies are concerned. This is an epic, in every sense of the word.',9.6,'2024-12-02 18:00:48'),(11,1,8,'4/4 Right from the get-go, my jaw dropped, my eyes were bulging, and my attention was grasped. As for the grand finale, It was an exquisite way to end such an epic film like this, and the overall outcome gave me an impressive sense of delight. \"The Good, The Bad, and The Ugly\" is not to be watched, but to be experienced.',8.7,'2024-12-02 18:03:22'),(12,4,10,'A movie that change the cinema industry forever in its day this was the ultimate movie with the best special effects ever put on film .',9.6,'2024-12-03 09:54:00'),(13,4,10,'The Matrix is a landmark in the canon of science-fiction films. Its special effects were (and still are) cutting-edge, and its story is unsettling, intriguing, complex, and philosophical all at once.',8.9,'2024-12-03 09:54:35'),(14,4,10,'Despite the immense hype behind the movie, I found this at best.',6.8,'2024-12-03 09:56:03'),(15,4,7,'Movies that make you laugh, movies that make you ponder,movies that may excite you, but only a few can make you cry. Forrest Gump does it all Boy, tears rolled down for the first time after watching a movie of course there are other movies that followed but surely none of those were even close to this phenomenal motion picture.',8.7,'2024-12-03 09:56:38'),(16,4,7,'I saw the trailer and found it interesting. I knew Tom Hanks was a great actor in Hollywood and the First time I watched him in Grey Hound Movie Trailer. Now coming to the movie, SPLENDID that is the word that I have to say. The movie has action, drama and most importantly comedy.',8.7,'2024-12-03 09:57:40'),(17,4,11,'This is the first sequel where I am not able to decide between part 1 and part 2 but still i would say Stree Part 1 is slightly better than this in terms of ≡ƒÄ¡ comedy',7.6,'2024-12-03 09:58:42'),(18,4,11,'Rajkumar Rao is once again in top form, delivering his signature performance with strong support from Aparshakti Khurana and Abhishek Banerjee. Great Movie, Must watch',8.2,'2024-12-03 09:59:23'),(19,4,11,'a perfect Horror comedy with all the elements right in place with horror comedy blend, Emotions, Fun , Great BGM , Excellent Cinematography, top notch VFX, Superb Production design and the powerful MaddockΓÇÖs supernatural universe coming together giving chilling feels in the adrenaline pumping climax.',8.9,'2024-12-03 09:59:51'),(20,4,12,'Three IdiotsΓÇÖ is a remarkable ahead of its time Bollywood blockbuster. This film is a comedy movie with strong acting, memorable characters, a perplexing storyline and most importantly, highly motivational movie to choose the right path in your life.',8.7,'2024-12-03 10:01:35'),(21,4,12,'\"3 Idiots,\" directed by Rajkumar Hirani, is a vibrant and thought-provoking film that delves into the pressures of the Indian education system. Following the lives of three engineering studentsΓÇöRancho, Farhan, and RajuΓÇöthe movie masterfully blends humor, drama, and social commentary.',8.9,'2024-12-03 10:02:49'),(22,4,13,'So many reviews on this movie have previously been written. So why another review? Well, itΓÇÖs because I couldnΓÇÖt resist from scripting few lines about this movie. Hindi Medium isnΓÇÖt really a movie. This is real; the real story of todayΓÇÖs elite parents who think studying in an English Medium school can promise a good life for their children.',8.9,'2024-12-03 10:03:58'),(23,4,13,'This movie is a heartfelt and thought-provoking film that left a profound impact on me. The movie, with Irrfan Khan\'s exceptional and natural acting, pays tribute to his remarkable legacy as an actor. Directed by Homi Adajania, the film presents a poignant reminder of Irrfan Khan\'s immense talent.',8.5,'2024-12-03 10:05:41'),(24,4,14,'The very first thing that made the entire Hindi audience kind of cringe was its title numbering that despite coming after krrish 1, how come it is numbered krrish 3 and even i thought they made a mistake but the logic was this is the 3rd film in the originally Koi Mil Gya franchise. Still, the fact that makers changed the name of the franchise and then gave the 2nd film of the superhero a title Krrish 3 still makes no sense.',6.7,'2024-12-03 10:07:32'),(25,4,14,'Movie has a normal story, but charecters are very nice on screen. Kangana Ranaut and priyanka chopra are ultimate in this film, by their acting. Hrithik Roshan, as usal impresses with his nice acting. Vivek Oberoi is shown less comparatively to others, but does make an impact. People compare the elevation of the film, that is fights, with Hollywood like marvel, ... But, see this film like you had not seen any Hollywood action film.',7.1,'2024-12-03 10:08:13'),(26,4,14,'I wish i could give this movie zero star. For this kind of movies to be good the vfx team requires a huge budget. But since in india people are actor oriented a huge amount of the total budget of the movie is paid to the big league actors like hrithik srk and all and only a tiny amount is provided for vfx. Which explains this kind of results.',0.1,'2024-12-03 10:09:05'),(27,4,6,'-Peter Jackson\'s The Fellowship of the Ring movie has successfully opened the door into Tolkien\'s world of Middle Earth for me. The plot tells of the quest of a hobbit, Frodo Baggins, to destroy an evil ring of power. He is aided in his quest by his friends and other companions who accompany him and protect him on his journey. The costumes, weapons, armor, the One Ring and the props are so rich and very well crafted by the film crew.',8.7,'2024-12-03 10:09:25'),(28,4,6,'4/4 Of the several fantasy film franchises that are based on a series of classic novels, \"The Lord of the Rings\" trilogy is probably my favorite fantasy franchise for valid reason; It\'s a breathtaking and influential epic fantasy adventure that delivers escapism that feels personal and profound as it takes itself seriously with so much passion on display, and it tackles some serious themes involving war, friendship, and heroism.',9,'2024-12-03 10:11:29'),(29,4,6,'The fellowship is just the perfect blend of setting the story, fleshing out characters and introducing us to the world of middle earth!Ian McKellen as Gandalf is just legendary.... mysterious, loveable, occasionally hilarious and in THAT iconic scene, completely immortalised.',7.8,'2024-12-03 10:12:24'),(30,4,9,'4/4 Growing up, I\'ve always thought that \"Star Wars\" is exceedingly overrated, and overtime, everyone would not take it seriously at all; ruining it\'s reputation as what could\'ve been an epic force to be reckoned with (which it is). Now, after seeing this classic masterpiece, I can see where everybody is coming from. I am astounded by what George Lucas (director/writer) had spawned as a director and as a storyteller, and I loved it. The tone of the movie overall was superbly executed.',9.6,'2024-12-03 10:15:26'),(31,4,9,'After the brooding meditation on oppression and rebellion that was Andor, and the eulogy to the futility of sacrifice that was Rogue One, the Star Wars franchise comes crashing down to earth with this tonally jarring sequel that injects high-jinks, wizardry and laser swords into what had until now been a uniquely grounded, dark-edged sci-fi universe.',7.5,'2024-12-03 10:16:51'),(32,4,8,'The Good, the Better, the Best.Brutal, brilliant, and one of the best Westerns ever made!!',8.8,'2024-12-03 10:17:49'),(33,4,9,'One of the best in the starwars franchise.',8.9,'2024-12-03 12:12:30'),(34,4,9,'Great Movie, I really like the acting of Harrison Ford',7.9,'2024-12-03 14:42:23'),(35,1,6,'Great Movie, one of the best fromthe LOTR franchise',9.5,'2025-01-30 08:56:32'),(36,1,17,'Great Movie',5.6,'2025-01-30 09:01:27');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `is_admin` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',1),(2,'t1','628b49d96dcde97a430dd4f597705899e09a968f793491e4b704cae33a40dc02',0),(4,'v','4c94485e0c21ae6c41ce1dfe7b6bfaceea5ab68e40a2476f50208e526f506080',0),(5,'t_user','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',0);
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

-- Dump completed on 2025-02-05 15:48:22
