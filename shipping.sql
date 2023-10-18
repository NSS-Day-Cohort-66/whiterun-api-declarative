-- Run this block if you already have a database and need to re-create it
DELETE FROM Ship;
DELETE FROM Hauler;
DELETE FROM Dock;

DROP TABLE IF EXISTS Ship;
DROP TABLE IF EXISTS Hauler;
DROP TABLE IF EXISTS Dock;
-- End block


-- Run this block to create the tables and seed them with some initial data
CREATE TABLE `Dock` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`location`	TEXT NOT NULL,
	`capacity` INTEGER NOT NULL
);

CREATE TABLE `Hauler` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`dock_id` INTEGER NOT NULL,
	FOREIGN KEY(`dock_id`) REFERENCES `Dock`(`id`)
);

CREATE TABLE `Ship` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`  TEXT NOT NULL,
	`hauler_id` INTEGER NOT NULL,
	FOREIGN KEY(`hauler_id`) REFERENCES `Hauler`(`id`)
);

INSERT INTO `Dock` VALUES (null, 'Antwerp', 1290);
INSERT INTO `Dock` VALUES (null, 'Shanghai', 840);
INSERT INTO `Dock` VALUES (null, 'Los Angeles', 1055);


INSERT INTO `Hauler` VALUES (null, "CTS", 1);
INSERT INTO `Hauler` VALUES (null, "V90", 1);
INSERT INTO `Hauler` VALUES (null, "Hollarad", 1);
INSERT INTO `Hauler` VALUES (null, "TRX-100 F", 2);
INSERT INTO `Hauler` VALUES (null, "Accrio", 3);
INSERT INTO `Hauler` VALUES (null, "Prismium", 2);


INSERT INTO `Ship` VALUES (null, "Schmidt", 1);
INSERT INTO `Ship` VALUES (null, "Baumbach", 1);
INSERT INTO `Ship` VALUES (null, "Haag", 2);
INSERT INTO `Ship` VALUES (null, "Hartmann", 2);
INSERT INTO `Ship` VALUES (null, "Keebler", 3);
INSERT INTO `Ship` VALUES (null, "Ebert", 3);
INSERT INTO `Ship` VALUES (null, "Beatty", 4);
INSERT INTO `Ship` VALUES (null, "Hudson", 4);
INSERT INTO `Ship` VALUES (null, "Becker", 5);
INSERT INTO `Ship` VALUES (null, "Dickens", 6);
INSERT INTO `Ship` VALUES (null, "Kunde", 6);
INSERT INTO `Ship` VALUES (null, "Hermiston", 5);
-- End block