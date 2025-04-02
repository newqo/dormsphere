drop table if exists `roles`;
create table `roles` (
    id_role tinyint auto_increment not null,
    role_description varchar(255),

    primary key (id_role)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `users`;
create table `users` (
    email varchar(255) not null,
    name varchar(255) not null,
    lastname varchar(255) not null,
    birthDate date not null,
    password varchar(255) not null,
    id_role tinyint not null,
    isEmailVerified boolean DEFAULT 0 not null,

    primary key (email),
    foreign key (id_role) references roles(id_role)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `amenities_category`;
create table `amenities_category` (
    id_amenities_category tinyint auto_increment not null,
    amenities_category_description varchar(255),

    primary key (id_amenities_category)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `amenities`;
create table `amenities` (
    id_amenities tinyint auto_increment not null,
    amenities_description varchar(255),
    id_amenities_category tinyint not null,

    primary key (id_amenities),
    foreign key (id_amenities_category) references amenities_category(id_amenities_category)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `room_types`;
create table `room_types` (
    id_room_types tinyint auto_increment not null,
    room_types_description varchar(255),
    room_price float not null,

    primary key (id_room_types)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `room_features`;
create table `room_features` (
    id_room_types tinyint not null,
    id_amenities tinyint not null,

    primary key (id_room_types, id_amenities),
    foreign key (id_room_types) references room_types(id_room_types),
    foreign key (id_amenities) references amenities(id_amenities)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `room_status`;
create table `room_status` (
    id_room_status tinyint auto_increment not null,
    room_status_description varchar(255),

    primary key (id_room_status)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `rooms`;
create table `rooms` (
    id_room smallint not null,
    id_room_types tinyint not null,
    id_room_status tinyint not null,

    primary key (id_room),
    foreign key (id_room_types) references room_types(id_room_types),
    foreign key (id_room_status) references room_status(id_room_status)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `rent`;
create table `rent` (
    id_rent smallint auto_increment not null,
    email varchar(255) not null,

    primary key (id_rent),
    foreign key (email) references users(email)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `rent_selected_room`;
create table `rent_selected_room` (
    id_rent smallint not null,
    id_room smallint not null,

    primary key (id_rent, id_room),
    foreign key (id_rent) references rent(id_rent),
    foreign key (id_room) references rooms(id_room)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `contacts_duration`;
create table `contacts_duration` (
    id_contacts_duration tinyint auto_increment not null,
    contacts_duration_description varchar(255),

    primary key (id_contacts_duration)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `contacts_status`;
create table `contacts_status` (
    id_contacts_status tinyint auto_increment not null,
    contacts_status_description varchar(255),  

    primary key (id_contacts_status)    
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `contacts`;
create table `contacts` (
    id_contacts smallint auto_increment not null,
    sign_date date not null,
    contacts_file_name varchar(255) not null,
    id_contacts_duration tinyint not null,
    id_contacts_status tinyint not null,
    email varchar(255) not null,

    primary key (id_contacts),

    foreign key (id_contacts_duration) references contacts_duration(id_contacts_duration),
    foreign key (id_contacts_status) references contacts_status(id_contacts_status),
    foreign key (email) references users(email)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `unit`;
create table `unit` (
    id_unit smallint auto_increment not null,
    water float not null,
    electricity float not null,

    primary key (id_unit)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `bill_status`;
create table `bill_status` (
    id_bill_status tinyint auto_increment not null,
    bill_status_description varchar(255),

    primary key (id_bill_status)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

drop table if exists `bills`;
create table `bills` (
    id_bill smallint auto_increment not null,
    id_unit smallint not null,
    id_bill_status tinyint not null,

    primary key (id_bill),
    foreign key (id_unit) references unit(id_unit),
    foreign key (id_bill_status) references bill_status(id_bill_status)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;
