-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS people_counts (
    timestamp TEXT,
    in_count INTEGER,
    out_count INTEGER
);

-- Clear any existing data from the table
-- DELETE FROM people_counts;

-- Insert generated data
-- Data for approximately 25-30 minutes, starting at 2025-05-15 09:00:00
-- Timestamps are in 'YYYY-MM-DD HH:MM:SS' format

INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:00:00.000000', 7, 0);
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:01:45.000000', 2, 1);
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:03:03.000000', 1, 0);
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:04:09.000000', 0, 1);
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:05:43.000000', 2, 0); -- Passengers on board (7 - 1 + 2 - 1 + 2 = 9). First entry at 09:00:00. This is 5m43s later.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:07:33.000000', 1, 2); -- On board duration: 7m33s. Still 8 on board.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:08:18.000000', 0, 2); -- On board duration: 8m18s. Still 6 on board.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:10:07.000000', 0, 5); -- On board duration met. Disembarking. 1 left.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:11:08.000000', 0, 1); -- Fully disembarked.

INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:12:49.000000', 9, 0); -- New boarding phase.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:13:58.000000', 3, 0);
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:15:37.000000', 0, 1);
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:16:51.000000', 1, 2); -- On board (9 + 3 - 1 + 1 - 2 = 10). From 09:12:49, this is 4m2s.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:18:24.000000', 2, 0); -- On board duration: 5m35s. Now 12 on board.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:19:40.000000', 0, 2); -- On board duration: 6m51s. Now 10 on board.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:21:28.000000', 0, 6); -- Disembarking. 4 left.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:22:31.000000', 0, 4); -- Fully disembarked.

INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:23:44.000000', 5, 0); -- New boarding phase.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:24:46.000000', 1, 1);
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:26:15.000000', 3, 0);
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:27:50.000000', 0, 2); -- On board (5 + 1 - 1 + 3 - 2 = 6). From 09:23:44, this is 4m6s.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:29:05.000000', 2, 1); -- On board duration: 5m21s. Now 7 on board.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:30:30.000000', 1, 0); -- On board duration: 6m46s. Now 8 on board.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:31:55.000000', 0, 7); -- Disembarking. 1 left.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:33:00.000000', 0, 1); -- Fully disembarked.