create table if not exists restaurants
(
    id   serial
        constraint restaurants_pk
            primary key,
    name text
);