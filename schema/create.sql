-- create table to store users
create table if not exists users (
  id         serial    not null primary key,
  name       varchar   not null,
  email      varchar   not null,
  password   varchar   not null,
  notify     int       default 0,
  created_at timestamp not null default now(),
  updated_at timestamp          default current_timestamp
);

-- create table to handle entries
create table if not exists entries (
  id         serial    not null primary key,
  title      varchar   not null,
  body       text      not null,
  created_by integer   not null references users (id),
  created_at timestamp not null default now(),
  updated_at timestamp          default current_timestamp
);

-- create table to handle revoked tokens
create table if not exists revoked_tokens (
  id         serial    not null primary key,
  jti     varchar   

);