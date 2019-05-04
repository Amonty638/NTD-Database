drop table EMPLOYEE cascade constraints;
drop table PRODUCT cascade constraints;
drop table CUSTOMER cascade constraints;
drop table ITEM cascade constraints;
drop table PRODUCT_IN_ORDER cascade constraints;
drop table CUSTOMER_ORDER cascade constraints ;

drop table EMPLOYEE cascade constraints;

delete from product where ntd# = 'N700';

create table EMPLOYEE(
  fname varchar2(20),
  lname varchar2(20),
  salesperson# varchar2(20) not null,
  primary key(salesperson#)
);
--EMPLOYEES INTO DB
insert into EMPLOYEE values('Robbie','Dutton','11');
insert into EMPLOYEE values('Zander', 'Montano','25');
insert into EMPLOYEE values('Ana Clara', 'Morellato Alcantara', '9');
insert into EMPLOYEE values('Maria', 'Galuna', '4');
insert into EMPLOYEE values('Tony', 'Massaro', '1');
insert into EMPLOYEE values('Lisa', 'Cardillo', '7');



create table PRODUCT(
  dye_lot varchar2(20),
  color varchar2(20),
  location varchar2(10),
  mfg# varchar2(20),
  buying_price number(20,3),
  amt_in_stock number(20,3),
  ntd_description varchar2(100),
  cost_per_sf number(20,3),
  sf_per_carton number(20,3),
  carton_count number,
  size_of_product number,
  piece_count number,
  ntd# varchar2(20) not null,
  primary key(ntd#)
);

select * from PRODUCT;

--TILES IN DATABASE
insert into PRODUCT values('A12','Slate','V-2-1','slatea12',1.50,400.00,'12x12 slate gray floor tile', 3.50, 8, 50, 1, 0, 'N365');---Order 1
insert into PRODUCT values('C','White Carrera','Q-7-3','white/gray 756',4.23,600.00,'12x24 white carrera polished wall tile', 7.50, 60, 10, 2, 0, 'M371');
insert into PRODUCT values('XZ2','Brown','D-3-3','darkbrown721',1.19,150.00,'6x6 slate gray floor tile', 2.50, 10, 15, 0.25, 0, 'S271');
insert into PRODUCT values('HYA','Blue Glass','G-9-3','ocean blue 25', 5.00, 200.00,'12x12 ocean blue glass sheet tile', 10.50, 5, 40, 1, 0, 'GL245');
insert into PRODUCT values('JHG','Lava Black','J-4-2','', 3.99,150.00,'6x12 Lava Black wall tile', 8.55, 5, 30, 0.5, 0, 'GL211');
insert into PRODUCT values('YU16','Diablo Red','S-9-3','diablo red q', 2.00, 800.00,'6x6 quarry tile', 3.50, 8, 50, 0.25, 0, 'Q244');
insert into PRODUCT values('A11','Green','V-7-2','moss green', 2.12, 250.00,'12x24 mossy green stone tile', 4.70, 5, 50, 2, 0, 'N370');
insert into PRODUCT values('DFS2','Brown','G-3-2','brown subway 2',1.20,200.00,'3x6 brown subway wall tile', 2.00, 5, 40, 0.125, 0, 'N260');
insert into PRODUCT values('B2','White','R-6-1','white subway 1',1.20, 300.00,'3x6 white subway wall tile', 2.00, 5, 60, 0.125, 0, 'N261');
insert into PRODUCT values('D2','Wolf Gray','R-8-1','wolf gray subway 1',1.20, 500.00,'3x6 wolf gray subway wall tile', 2.00, 5, 100, 0.125, 0, 'N264');
insert into PRODUCT values('S44','Slate-Gray','N-5-2','slateg4', 3.12, 400.00, '12x12 slate green floor tile', 6.20, 8, 50, 1, 0, 'N372');
insert into PRODUCT values('JJ','Perlato','K-2-3','wm4',6.12, 180.00,'12x12 marble white floor tile', 12.50, 10, 18, 1, 0, 'N369');----Order 1
--GROUTS IN DATABASE
insert into PRODUCT values('17a','Bright White','G-2-2','bright white',3.50,40.00,'10 lb bags of Bright White Sanded Grout', 7.20, 1, 40, 10, 0, 'SABRIWHI10');---Order 1
insert into PRODUCT values('17a','Dove Gray','G-2-1','dove gray',3.50,15.00,'10 lb bags of Dove Gray Sanded Grout', 7.20, 1, 15, 10, 0, 'SADOVGRA10');
insert into PRODUCT values('18b','Silverado','G-2-1','silverado',9.00,10.00,'25 lb bags of Silverado Sanded Grout', 18.20, 1, 10, 25, 0, 'SASIL25');
insert into PRODUCT values('18b','Mocha','H-2-2','mocha',3.50,21.00,'10lb bags of Mocha UnSanded Grout', 7.20, 1, 21, 10, 0, 'UNSAMOC10');
insert into PRODUCT values('19c','Standard Gray','H-1-2','standard gray',3.50,16.00,'10lb bags of Standard Gray UnSanded Grout', 7.20, 1, 16, 10, 0, 'SASTAGRA10');




create table ITEM(
  ntd# varchar2(20) not null,
  quantity number(13,3),
  total_cost number(13,3),
  hold# number not null,

  primary key (ntd#,hold#),
  foreign key (ntd#) references PRODUCT(ntd#),
  foreign key (hold#) references CUSTOMER_ORDER(hold#)
);

--ORDER 1
INSERT INTO ITEM values('N369', 20.0, 250.00, 18095);
INSERT INTO ITEM values('SABRIWHI10', 4.0, 28.80, 18095);
INSERT INTO ITEM values('N365', 64.0, 224.00, 18095);
--ORDER 2
INSERT INTO ITEM VALUES ('N372', 50, 310.00, 17101);
INSERT INTO ITEM VALUES ('SASIL25', 1, 18.20, 17101);

select * from ITEM;

create table CUSTOMER(
  fname varchar2(20),
  lname varchar2(20),
  city varchar2(20),
  zip varchar2(15),
  state varchar2(20),
  email varchar2(100),
  phone varchar2(30) not null ,
  street_address varchar2(30),
  primary key(phone)
);

INSERT INTO CUSTOMER values ('Harry', 'Potter', 'London', 01234, 'United Kingdon', 'potterWizard@hotmail.com', '555-555-5555', '4 Privet Drive');
INSERT INTO CUSTOMER VALUES ('O.J.', 'Simpson', 'San Francisco', 56783, 'California', 'footballandkilling@gmail.com', '123-123-1234', '6 foot drive');

select * from CUSTOMER;

create table CUSTOMER_ORDER(
  date_made varchar2(50),
  total_cost number(13,3),
  description varchar2(50),
  hold# number not null,
  delivery_address varchar2(50),
  phone# varchar2(30),
  salesperson# varchar2(20),
  primary key (hold#),
  foreign key (phone#) references CUSTOMER(phone),
  foreign key (salesperson#) references EMPLOYEE(salesperson#)
);

drop table CUSTOMER_ORDER;
INSERT into CUSTOMER_ORDER values ('10-2-1995', 502.80, 'For upstairs bathroom', 18095, 'Customer Picking up', '123-123-1234','25');
INSERT into CUSTOMER_ORDER values ('11-2-2019', 328.20, 'Mud room', 17101, 'Customer picking up', '555-555-5555','11');
INSERT into CUSTOMER_ORDER values ('10-3-1996', 0.00, 'Killing room', 19999, 'His mansion', '123-123-1234','11');
select * from CUSTOMER_ORDER;

delete from CUSTOMER_ORDER where hold# = 67737;
delete from item where hold# = 67737;

create table PRODUCT_IN_ORDER(
  cost number(13,3),
  amount_of_product number(13,3),
  ntd# varchar2(20) not null,
  date_made date,
  total_cost number(13,3),
  description varchar2(50),
  hold# number not null,
  delivery_address varchar2(50),
  salesperson# number not null,
  customer_phone varchar2(30) not null,

primary key(hold#),
foreign key (salesperson#) references EMPLOYEE(salesperson#),
foreign key (customer_phone) references CUSTOMER(phone),
foreign key (ntd#) references PRODUCT(ntd#)

);



--SOME TESTING STUFF
select * from EMPLOYEE;

select fname
from EMPLOYEE
where salesperson# = 11;


delete from PRODUCT where dye_lot = 'test'
