create table if not exists restaurants
(
    id   serial
        constraint restaurants_pk
            primary key,
    name text
);

create table if not exists rankings
(
    id              serial,
    name            text,
    restaurants_ids text
);

create table users
(
    id       serial
        constraint users_pk
            primary key,
    email    text,
    password text
);