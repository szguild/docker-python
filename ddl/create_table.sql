-- create product master
create table if not exists product.tb_product_m(
    site_cd varchar(50) not null,
    product_id bigint not null,
    product_nm varchar(500) not null,
    price int not null,
    img_url varchar(500) not null,
    page_url varchar(500) not null,
    attribute1 varchar(500),
    attribute2 varchar(500),
    attribute3 varchar(500),
    attribute4 varchar(500),
    attribute5 varchar(500),
    create_dt timestamp not null,
    update_dt timestamp,
    primary key (site_cd, product_id)
);

-- create loading table
create table if not exists product.tb_product_if(
    id serial,
    site_cd varchar(50) not null,
    product_id bigint not null,
    product_nm varchar(500) not null,
    price int not null,
    img_url varchar(500) not null,
    page_url varchar(500) not null,
    attribute1 varchar(500),
    attribute2 varchar(500),
    attribute3 varchar(500),
    attribute4 varchar(500),
    attribute5 varchar(500),
    create_dt timestamp,
    work_flag char(1) default 'N',
    work_dt timestamp
);

create index if not exists ix_tb_product_if_01 on product.tb_product_if(work_flag);

-- create job logging table
create table if not exists product.tb_job_log(
    id serial,
    job_name varchar(100) not null,
    status_cd char(1), -- I(ing), S(success), E(error)
    start_dt timestamp,
    end_dt timestamp,
    message varchar(500),
    create_dt timestamp,
    update_dt timestamp
);
create index if not exists ix_tb_job_log_01 on product.tb_job_log(job_name);
create index if not exists ix_tb_job_log_02 on product.tb_job_log(status_cd);

-- create extract target product list (향후 상품정보 수집대상 관리 테이블)
create table if not exists product.tb_product_target(
    site_cd varchar(50) not null,
    product_id bigint not null,
    use_yn char(1),
    create_dt timestamp,
    update_dt timestamp,
    primary key (site_cd, product_id)
);

insert into product.tb_product_target values ('gsshop', 37216130, 'Y', now(), null);
insert into product.tb_product_target values ('gmarket', 242253587, 'Y', now(), null);
insert into product.tb_product_target values ('gsshop', 37216131, 'Y', now(), null);
insert into product.tb_product_target values ('gmarket', 2391361187, 'Y', now(), null);