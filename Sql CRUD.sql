create table DETAILS(Cid VARCHAR(100) primary key,Name VARCHAR(50),Age INT NOT NULL,Image LONGBLOB,
Question VARCHAR(150),Persontest varchar(20),hobby VARCHAR(100),Profession VARCHAR(100),
Gender Varchar(15),Location Varchar(50),Email_id varchar(50),Number varchar(12),
genderpre varchar(15),Password varchar(100) NOT NULL);

create table Requests(Cidr VARCHAR(100),Cida VARCHAR(100),rel bool,answer VARCHAR(200),
PRIMARY KEY(Cidr,Cida)); 

select * from DETAILS;

Drop table DETAILS

Select * from Requests

Drop table Requests

Drop table DETAILS;

insert into Requests values("Ankita","Ashutosh",false,"I want to pursue my MBA from Pennyslevenia");
insert into Requests values("Karishma","Ashutosh",false,"I want to complete my Post Graduation that's my future plan");
insert into Requests values("Rashmi","Ashutosh",true,"I want to travel Seven Wonders of the World");
insert into Requests values("Anushka","Ashutosh",true,"I want to establish a startup");
insert into Requests values("Ishika","Ashutosh",false,"I want to go in Kashmir once in a lifetime");
insert into Requests values("Sanjana","Ashutosh",true,"I want to pursue my MS in India");


insert into Requests values("Karishma","Priyanshu",false,"My favourite actor is Zayn and actress is Katherine");
insert into Requests values("Sahil","Karishma",false,"I would like to travel Australia as its surrounded by sea");
insert into Requests values("Ankita","Akhil",false,"Yes,I like cooking");
insert into Requests values("Aditya","Ankita",false,"Yes,I like to watch Netflix Series");

