PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
	id INTEGER NOT NULL, 
	full_name VARCHAR NOT NULL, 
	email VARCHAR NOT NULL, 
	password_hash VARCHAR NOT NULL, 
	role VARCHAR, 
	profile_picture VARCHAR, 
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP, 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
INSERT INTO users VALUES(1,'Miguel_Bruce','miguelfouenanf@gmail.com','$2b$12$kYIxXFWzQs./LDQyj16VAO8FRYNCN9c994uNpenNfTJV9zVp/I3Vu','student',NULL,'2026-09-08 18:26:16');
INSERT INTO users VALUES(2,'admin','bfouenang237@gmail.com','$2b$12$gMggVjLekX7Rs7YmWjW/EevfuaaPCeIP0i96yKTbyRavoIXAf2OaK','admin',NULL,'2026-09-08 18:26:41');
CREATE TABLE hostels (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	location VARCHAR NOT NULL, 
	gender VARCHAR NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
CREATE TABLE rooms (
	id INTEGER NOT NULL, 
	room_number VARCHAR NOT NULL, 
	capacity VARCHAR NOT NULL, 
	current_occupancy INTEGER, 
	is_available BOOLEAN, 
	hostel_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(hostel_id) REFERENCES hostels (id)
);
CREATE TABLE complaints (
	id INTEGER NOT NULL, 
	title VARCHAR NOT NULL, 
	description VARCHAR NOT NULL, 
	status VARCHAR(10), 
	priority VARCHAR(6), 
	proof_image VARCHAR, 
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
);
CREATE TABLE notices (
	id INTEGER NOT NULL, 
	title VARCHAR NOT NULL, 
	content VARCHAR NOT NULL, 
	is_pinned BOOLEAN, 
	is_active BOOLEAN, 
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP, 
	author_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(author_id) REFERENCES users (id)
);
INSERT INTO notices VALUES(1,'string','string',0,1,'2026-09-08 18:34:23',2);
CREATE UNIQUE INDEX ix_users_id ON users (id);
CREATE INDEX ix_hostels_id ON hostels (id);
CREATE INDEX ix_rooms_id ON rooms (id);
CREATE INDEX ix_complaints_id ON complaints (id);
CREATE INDEX ix_notices_id ON notices (id);
COMMIT;
