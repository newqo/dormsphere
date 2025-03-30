drop table if exists `Roles`;
create table `Roles` (
    id_role tinyint auto_increment not null,
    role_description varchar(255),

    primary key (id_role)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `Users`;
create table `Users` (
    email varchar(255) not null,
    name varchar(255) not null,
    lastname varchar(255) not null,
    birthDate date not null,
    password varchar(255) not null,
    id_role tinyint not null,
    isEmailVerified boolean DEFAULT 0 not null,

    primary key (email),
    foreign key (id_role) references Roles(id_role)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `AmenitiesCategory`;
create table `AmenitiesCategory` (
    id_amenities_category tinyint auto_increment not null,
    amenities_category_description varchar(255),

    primary key (id_amenities_category)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `Amenities`;
create table `Amenities` (
    id_amenities tinyint auto_increment not null,
    amenities_description varchar(255),
    id_amenities_category tinyint not null,

    primary key (id_amenities),
    foreign key (id_amenities_category) references AmenitiesCategory(id_amenities_category)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `RoomTypes`;
create table `RoomTypes` (
    id_room_types tinyint auto_increment not null,
    room_types_description varchar(255),
    room_price float not null,

    primary key (id_room_types)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `RoomFeatures`;
create table `RoomFeatures` (
    id_room_types tinyint not null,
    id_amenities tinyint not null,

    primary key (id_room_types, id_amenities),
    foreign key (id_room_types) references RoomTypes(id_room_types),
    foreign key (id_amenities) references Amenities(id_amenities)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `RoomStatus`;
create table `RoomStatus` (
    id_room_status tinyint auto_increment not null,
    room_status_description varchar(255),

    primary key (id_room_status)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `Rooms`;
create table `Rooms` (
    id_room smallint not null,
    id_room_types tinyint not null,
    id_room_status tinyint not null,

    primary key (id_room),
    foreign key (id_room_types) references RoomTypes(id_room_types),
    foreign key (id_room_status) references RoomStatus(id_room_status)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `Rent`;
create table `Rent` (
    id_rent smallint auto_increment not null,
    email varchar(255) not null,

    primary key (id_rent),
    foreign key (email) references Users(email)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `RentSelectedRoom`;
create table `RentSelectedRoom` (
    id_rent smallint not null,
    id_room smallint not null,

    primary key (id_rent, id_room),
    foreign key (id_rent) references Rent(id_rent),
    foreign key (id_room) references Rooms(id_room)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `ContactsDuration`;
create table `ContactsDuration` (
    id_contacts_duration tinyint auto_increment not null,
    contacts_duration_description varchar(255),

    primary key (id_contacts_duration)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `ContactsStatus`;
create table `ContactsStatus` (
    id_contacts_status tinyint auto_increment not null,
    contacts_status_description varchar(255),  

    primary key (id_contacts_status)    
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `Contacts`;
create table `Contacts` (
    id_contacts smallint auto_increment not null,
    sign_date date not null,
    contacts_file_name varchar(255) not null,
    id_contacts_duration tinyint not null,
    id_contacts_status tinyint not null,
    email varchar(255) not null,

    primary key (id_contacts),

    foreign key (id_contacts_duration) references ContactsDuration(id_contacts_duration),
    foreign key (id_contacts_status) references ContactsStatus(id_contacts_status),
    foreign key (email) references Users(email)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `Unit`;
create table `Unit` (
    id_unit smallint auto_increment not null,
    water float not null,
    electricity float not null,

    primary key (id_unit)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `BillStatus`;
create table `BillStatus` (
    id_bill_status tinyint auto_increment not null,
    bill_status_description varchar(255),

    primary key (id_bill_status)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `Bills`;
create table `Bills` (
    id_bill smallint auto_increment not null,
    id_unit smallint not null,
    id_bill_status tinyint not null,

    primary key (id_bill),
    foreign key (id_unit) references Unit(id_unit),
    foreign key (id_bill_status) references BillStatus(id_bill_status)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
