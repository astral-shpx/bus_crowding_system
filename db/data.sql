-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS people_counts (
    timestamp TEXT,
    in_count INTEGER,
    out_count INTEGER
);

-- Clear any existing data from the table
-- DELETE FROM people_counts;

-- Insert data

-- Start of Journey (Approx. 09:00)
-- Stop 1: Initial Boarding (Bus was likely empty)
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:00:10.000000', 20, 0); -- Initial large boarding
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:01:00.000000', 5, 0);  -- A few more board. Onboard: 25.

-- Travel 1 (~5 mins)

-- Stop 2 (Approx. 09:06) - Mix of getting off and on
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:06:35.000000', 2, 3);  -- 2 board, 3 get off. Net: -1. Onboard: 24.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:07:15.000000', 5, 1);  -- 5 board, 1 gets off. Net: +4. Onboard: 28.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:07:50.000000', 3, 2);  -- 3 board, 2 get off. Net: +1. Onboard: 29.

-- Travel 2 (~8 mins)
-- Onboard: 29

-- Stop 3 (Approx. 09:16) - More disembarking as some reach their destination (~15-16 mins journey)
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:16:20.000000', 1, 8);  -- 1 boards, 8 get off. Net: -7. Onboard: 22.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:17:05.000000', 3, 5);  -- 3 board, 5 get off. Net: -2. Onboard: 20.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:17:45.000000', 6, 2);  -- 6 board, 2 get off. Net: +4. Onboard: 24.

-- Travel 3 (~6 mins)
-- Onboard: 24

-- Stop 4 (Approx. 09:24) - Mix of disembarking and boarding
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:24:30.000000', 2, 7);  -- 2 board, 7 get off. Net: -5. Onboard: 19.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:25:00.000000', 4, 3);  -- 4 board, 3 get off. Net: +1. Onboard: 20.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:25:35.000000', 5, 1);  -- 5 board, 1 gets off. Net: +4. Onboard: 24.

-- Travel 4 (~11 mins) - Longer travel segment

-- Stop 5 (Approx. 09:37) - More disembarking (~19-20 mins journey)
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:37:10.000000', 1, 6);  -- 1 board, 6 get off. Net: -5. Onboard: 19.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:37:50.000000', 3, 4);  -- 3 board, 4 get off. Net: -1. Onboard: 18.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:38:25.000000', 7, 2);  -- 7 board, 2 get off. Net: +5. Onboard: 23.

-- Travel 5 (~7 mins)

-- Stop 6 (Approx. 09:46) - Mix of disembarking and boarding
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:46:00.000000', 2, 5);  -- 2 board, 5 get off. Net: -3. Onboard: 20.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:46:40.000000', 4, 3);  -- 4 board, 3 get off. Net: +1. Onboard: 21.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:47:15.000000', 6, 1);  -- 6 board, 1 gets off. Net: +5. Onboard: 26.

-- Travel 7 (~9 mins)

-- Stop 8 (Approx. 09:57) - More disembarking (~19-20 mins journey)
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:57:05.000000', 1, 5);  -- 1 board, 5 get off. Net: -4. Onboard: 22.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:57:45.000000', 2, 4);  -- 2 board, 4 get off. Net: -2. Onboard: 20.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T09:58:20.000000', 5, 1);  -- 5 board, 1 gets off. Net: +4. Onboard: 24.

-- Travel 8 (~6 mins)

-- Stop 9 (Approx. 10:05) - Mix of disembarking and boarding
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T10:05:35.000000', 2, 6);  -- 2 board, 6 get off. Net: -4. Onboard: 20.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T10:06:15.000000', 3, 3);  -- 3 board, 3 get off. Net: 0. Onboard: 20.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T10:06:50.000000', 4, 1);  -- 4 board, 1 gets off. Net: +3. Onboard: 23.

-- Travel 9 (~8 mins)

-- Stop 10 (Approx. 10:15) - More disembarking (~17-18 mins journey)
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T10:15:00.000000', 1, 5);  -- 1 board, 5 get off. Net: -4. Onboard: 19.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T10:15:40.000000', 2, 4);  -- 2 board, 4 get off. Net: -2. Onboard: 17.
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T10:16:20.000000', 3, 1);  -- 3 board, 1 gets off. Net: +2. Onboard: 19.

-- End of ~1 hour and 16 minutes journey (Approx. 10:16)
-- Bus might continue or arrive at a terminal and empty out.

-- Travel 10 (~7 mins)

-- Final Stop (Approx. 10:24) - Majority disembark
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T10:24:00.000000', 0, 10); -- Significant number get off
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T10:24:40.000000', 0, 5);  -- More get off
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T10:25:15.000000', 0, 4);  -- Remaining off. Onboard: 0.

-- Bus is now empty (or starts a new route)
INSERT INTO people_counts (timestamp, in_count, out_count) VALUES ('2025-05-15T10:30:00.000000', 15, 0); -- New journey begins