create schema if not exists azure_bd;
use azure_bd;

select * from information_schema.table_constraints
	where constraint_schema = 'azure_bd';

-- restrição atribuida a um domínio
-- create domain D_num as int check(D_num> 0 and D_num< 21);

CREATE TABLE employee(
	  first_name varchar(15) not null,
    minit char,
    last_name varchar(15) not null,
    ssn char(9) not null, 
    birthday date,
    address varchar(30),
    gender char,
    salary decimal(10,2),
    super_ssn char(9),
    dept_num int not null,
    constraint chk_salary_employee check (salary> 2000.0),
    constraint pk_employee primary key (ssn)
);

alter table employee 
	add constraint fk_employee 
	foreign key(super_ssn) references employee(ssn)
    on delete set null
    on update cascade;

alter table employee modify dept_num int not null default 1;

desc employee;

create table departament(
	  dept_name varchar(15) not null,
    dept_num int not null,
    mgr_ssn char(9) not null,
    mgr_start_date date, 
    dept_create_date date,
    constraint chk_date_dept check (dept_create_date < mgr_start_date),
    constraint pk_dept primary key (dept_num),
    constraint unique_name_dept unique(dept_name),
    foreign key (mgr_ssn) references employee(ssn)
);

-- 'def', 'company_constraints', 'departament_ibfk_1', 'company_constraints', 'departament', 'FOREIGN KEY', 'YES'
-- modificar uma constraint: drop e add
alter table departament drop  departament_ibfk_1;
alter table departament 
		add constraint fk_dept foreign key(mgr_ssn) references employee(ssn)
        on update cascade;

desc departament;

create table dept_locations(
	dept_num int not null,
	dept_location varchar(15) not null,
    constraint pk_dept_locations primary key (dept_number, dept_location),
    constraint fk_dept_locations foreign key (dept_number) references departament (dept_number)
);

alter table dept_locations drop fk_dept_locations;

alter table dept_locations 
	add constraint fk_dept_locations foreign key (dept_num) references departament(dept_number)
	on delete cascade
    on update cascade;

create table project(
	project_ame varchar(15) not null,
	project_number int not null,
    project_location varchar(15),
    dept_num int not null,
    primary key (project_number),
    constraint unique_project unique (project_name),
    constraint fk_project foreign key (depart_num) references departament(dept_number)
);


create table works_on(
	  e_ssn char(9) not null,
    project_num int not null,
    hours decimal(3,1) not null,
    primary key (e_ssn, project_num),
    constraint fk_employee_works_on foreign key (e_ssn) references employee(ssn),
    constraint fk_project_works_on foreign key (project_num) references project(project_number)
);

drop table dependent;
create table dependent(
	  e_ssn char(9) not null,
    dependent_name varchar(15) not null,
    gender char,
    birthday date,
    relationship varchar(8),
    primary key (e_ssn, dependent_name),
    constraint fk_dependent foreign key (Essn) references employee(ssn)
);

show tables;
desc dependent;
