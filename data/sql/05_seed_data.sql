-- Insert sample voyages
INSERT INTO wov.wov_voyages (voyage_id, name, start_date, end_date, region, notes) VALUES
('VOY001', 'Antarctic Expedition 2025', '2025-01-15', '2025-03-15', 'Antarctica', 'Summer research voyage.'),
('VOY002', 'Southern Ocean Transect', '2025-06-01', '2025-07-01', 'Southern Ocean', 'Winter survey.');

-- Insert sample users
-- Generate UUIDs for users, or use fixed ones for consistency
INSERT INTO wov.wov_users (user_id, username, role, email) VALUES
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'jules', 'scientist', 'jules@example.com'),
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 'captain', 'crew', 'captain@example.com');

-- Insert sample observations
-- Link to voyages and users, and add some inaturalist_observation_ids
INSERT INTO wov.wov_observations (voyage_id, user_id, species_guess, common_name, scientific_name, latitude, longitude, observed_on, inaturalist_observation_id) VALUES
('VOY001', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'Emperor Penguin', 'Emperor Penguin', 'Aptenodytes forsteri', -77.846, 166.686, '2025-02-20', 179331853),
('VOY001', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'Orca', 'Killer Whale', 'Orcinus orca', -64.5, 120.0, '2025-02-22', 179331839),
('VOY002', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 'Albatross', 'Wandering Albatross', 'Diomedea exulans', -50.0, 100.0, '2025-06-10', null);
