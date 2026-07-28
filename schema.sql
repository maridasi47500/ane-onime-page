CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists bboxzoneouvoyager(
        id integer primary key autoincrement,
        min_lat text,
            min_lon text,
            max_lat text,
            max_lon text,
            name text
                    );
INSERT OR IGNORE INTO bboxzoneouvoyager (min_lat, min_lon,max_lat,max_lon,name)
VALUES( '45.92675064614011', '5.081708599776381', '52.67509283688802', '28.19694284682927', 'voyage en europe');
INSERT OR IGNORE INTO bboxzoneouvoyager (min_lat, min_lon,max_lat,max_lon,name)
VALUES( '33.25676200944641', '-116.31120436622517', '40.755306531960315', '-84.49479817995558', 'voyage en europe');
create table if not exists user(
        id integer primary key autoincrement,
        username text,
            email text,
            password text,
            country_id text,
            phone text,
            pic text,
            bboxzoneouvoyager_id text,
            transport_mode text
                    );
create table if not exists country(
        id integer primary key autoincrement,
        name text
                    );
create table if not exists post(
        id integer primary key autoincrement,
        title text,
            content text,
            lat text,
            lon text,
            location text,
            pic text,
            user_id text
                    );
