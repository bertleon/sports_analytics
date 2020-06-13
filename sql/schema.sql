CREATE TABLE season(
  playerid INTEGER PRIMARY KEY autoincrement, 
  fullname VARCHAR(40) NOT NULL,
  points INTEGER NOT NULL, 
  assists INTEGER NOT NULL, 
  rebounds INTEGER NOT NULL, 
  steals INTEGER NOT NULL,
  blocks INTEGER NOT NULL
);
