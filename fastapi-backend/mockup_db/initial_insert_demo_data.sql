insert into roles(role_description) values
("Customer"),
("Admin");

insert into amenities_category(amenities_category_description) values
("Room Amenities"),
("Convenience & Services"),
("Dining & Kitchen Facilities"),
("Health & Wellness"),
("Social & Community Spaces");

insert into amenities(amenities_description,id_amenities_category) values
("Fully furnished rooms (bed, desk, chair, wardrobe)",1),
("Air conditioning & heating",1),
("High-speed Wi-Fi",1),
("Private & shared bathrooms",1),
("Smart locks & keycard access",1),
("Personal storage space",1),

("24/7 security & CCTV surveillance",2),
("Housekeeping & room cleaning services",2),
("Laundry facilities (self-service & paid services)",2),
("Study rooms & co-working spaces",2),
("Parcel & mail delivery service",2),
("Vending machines & convenience store",2),
("On-site maintenance & repair requests",2),

("Shared kitchen with cooking equipment",3),
("Refrigerator & microwave access",3),
("Coffee & snack lounge",3),

("Fitness center / gym",4),
("Bike storage & rental services",4),

("Rooftop terrace & garden space",5),
("Community events & workshops",5);

insert into room_types(room_types_description,room_price) values
("Normal",5500),
("Premium",7500),
("Deluxe",10000);

insert into room_features(id_room_types,id_amenities) values
-- Normal Room Features
(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), -- Room Amenities
(1,7), (1,8), (1,9), -- Convenience & Services
(1,13), (1,14), -- Dining & Kitchen Facilities

-- Premium Room Features (includes all Normal features + more)
(2,1), (2,2), (2,3), (2,4), (2,5), (2,6),
(2,7), (2,8), (2,9), (2,10), (2,11), (2,12),
(2,13), (2,14), (2,15), -- Coffee & snack lounge
(2,16), (2,17), -- Health & Wellness

-- Deluxe Room Features (includes all Premium features + all amenities)
(3,1), (3,2), (3,3), (3,4), (3,5), (3,6),
(3,7), (3,8), (3,9), (3,10), (3,11), (3,12),
(3,13), (3,14), (3,15), (3,16), (3,17),
(3,18), (3,19); -- Social & Community Spaces

insert into room_status(room_status_description) values
("Available"),
("Occupied"),
("Under Maintenance");

insert into rooms (id_room, id_room_types, id_room_status) values
-- Floor 1
-- Normal
(101, 1, 1), (102, 1, 1), (103, 1, 1), (104, 1, 1), (105, 1, 1), 
(106, 1, 1), (107, 1, 1), (108, 1, 1), (109, 1, 1), (110, 1, 1),
(111, 1, 1), (112, 1, 1), 
-- Premium
(113, 2, 1), (114, 2, 1), (115, 2, 1), (116, 2, 1), (117, 2, 1), 
-- Deluxe
(118, 3, 1), (119, 3, 1), (120, 3, 1),

-- Floor 2
-- Normal
(201, 1, 1), (202, 1, 1), (203, 1, 1), (204, 1, 1), (205, 1, 1), 
(206, 1, 1), (207, 1, 1), (208, 1, 1), (209, 1, 1), (210, 1, 1),
(211, 1, 1), (212, 1, 1), 
-- Premium
(213, 2, 1), (214, 2, 1), (215, 2, 1), (216, 2, 1), (217, 2, 1), 
-- Deluxe
(218, 3, 1), (219, 3, 1), (220, 3, 1),

-- Floor 3
-- Normal
(301, 1, 1), (302, 1, 1), (303, 1, 1), (304, 1, 1), (305, 1, 1), 
(306, 1, 1), (307, 1, 1), (308, 1, 1), (309, 1, 1), (310, 1, 1),
(311, 1, 1), (312, 1, 1), 
-- Premium
(313, 2, 1), (314, 2, 1), (315, 2, 1), (316, 2, 1), (317, 2, 1), 
-- Deluxe
(318, 3, 1), (319, 3, 1), (320, 3, 1),

-- Floor 4
-- Normal
(401, 1, 1), (402, 1, 1), (403, 1, 1), (404, 1, 1), (405, 1, 1), 
(406, 1, 1), (407, 1, 1), (408, 1, 1), (409, 1, 1), (410, 1, 1),
(411, 1, 1), (412, 1, 1), 
-- Premium
(413, 2, 1), (414, 2, 1), (415, 2, 1), (416, 2, 1), (417, 2, 1), 
-- Deluxe
(418, 3, 1), (419, 3, 1), (420, 3, 1),

-- Floor 5
-- Normal
(501, 1, 1), (502, 1, 1), (503, 1, 1), (504, 1, 1), (505, 1, 1), 
(506, 1, 1), (507, 1, 1), (508, 1, 1), (509, 1, 1), (510, 1, 1),
(511, 1, 1), (512, 1, 1), 
-- Premium
(513, 2, 1), (514, 2, 1), (515, 2, 1), (516, 2, 1), (517, 2, 1), 
-- Deluxe
(518, 3, 1), (519, 3, 1), (520, 3, 1);

insert into contacts_duration(contacts_duration_description) values
("1 Year");

insert into contacts_status(contacts_status_description) values
("Waiting"),
("Accept"),
("Expired");

insert into bill_status(bill_status_description) values
("Pending"),
("Paid");

insert into unit(water,electricity) values
(20,8)