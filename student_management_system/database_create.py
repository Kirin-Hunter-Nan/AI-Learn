import pymysql
import yaml
with open('config.yml', 'r') as ymlfile:
    config = yaml.safe_load(ymlfile)

conn = pymysql.connect(**config['mysql'])

cursor = conn.cursor()

create_student_table = """
create table if not exists student(
    id int primary key auto_increment,
    stu_id char(10) unique,
    stu_name varchar(30),
    stu_phone char(15) unique,
    stu_class varchar(30),
    stu_password varchar(30)
)"""

create_teacher_table = """
create table if not exists teacher(
    id int primary key auto_increment,
    tea_id char(10) unique,
    tea_name varchar(30),
    tea_phone char(15) unique,
    tea_class varchar(30),
    tea_password varchar(30)
)"""

create_class_table = """
create table if not exists class(
    id int primary key auto_increment,
    cla_id char(10) unique,
    cla_name varchar(30),
    cla_teacher_id char(10) unique
)"""

create_admin_table = """
create table if not exists admin(
    id int primary key auto_increment,
    admin_id char(10) unique,
    admin_name varchar(30),
    admin_phone char(15) unique,
    admin_password varchar(30)
)"""

cursor.execute(create_student_table)
cursor.execute(create_teacher_table)
cursor.execute(create_class_table)
cursor.execute(create_admin_table)

conn.commit()