import mysql.connector

def convertToBinaryForm(filename):

    with open(filename,'rb') as file:
        Binary_Data = file.read()

        return Binary_Data

def InsertBLOB(cid,name,age,photo,Question,persontest,hobby,Profession,Gender,Location,Email_id,Number,genderpre,password):

    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "NoSignal@0612",database = "rohitdatabase")

    mycursor = mydb.cursor()

    sql_statement = "Insert into DETAILS(Cid,Name,Age,Image,Question,Persontest,hobby,Profession,Gender,Location,Email_id,Number,genderpre,Password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    photo = convertToBinaryForm(photo)

    insert_new_tuple = (cid,name,age,photo,Question,persontest,hobby,Profession,Gender,Location,Email_id,Number,genderpre,password)

    mycursor.execute(sql_statement,insert_new_tuple)
    mydb.commit()

InsertBLOB("Ashutosh","Ashutosh Sharma",20,"C:\\Users\\VIVEK\\Pictures\\Camera Roll\\Himanshu.JPG","What are your Future Plans?","21122","Painting","Working in L&T Company","Male","Mumbai","ashutoshs@gmail.com","9263781667","Female","Ashutosh@2305",)
InsertBLOB("Anushka","Anushka Kadam",19,"C:\\Users\\VIVEK\\Pictures\\Camera Roll\\Nora.JPEG","Which sport do you like the most and why?","22112","Singing","Pursuing MBA in Finland","Female","Mumbai","anushkak@gmail.com","9263784526","Male","Anushka@1912")
InsertBLOB("Sahil","Sahil Ketkar",23,"C:\\Users\\VIVEK\\Pictures\\Camera Roll\\Pushkar.JPG","What are your Education Qualifications?","21222","Reading","Working in Accenture","Male","Mumbai","sahilk@gmail.com","9563725728","Female","Sahil@2110" )
InsertBLOB("Manali","Manali Patil",22,"C:\\Users\\VIVEK\\Pictures\\Camera Roll\\Sakshi.JPG","Which places you like to travel the most?","22222","Nothing","Pursuing MS in IIT Bombay","Female","Mumbai","manalip@gmail.com","9647835482","Male","Manali@9632" )
InsertBLOB("Akhil","Akhil Nair",24,"C:\\Users\\VIVEK\\Pictures\\Camera Roll\\Akhil.JPG","Do you like cooking or not ?","12221","Planting Trees","Working in Capgemini","Male","Mumbai","akhiln@gmail.com","9375342678","Female","Akhil@4545" )
InsertBLOB("Rashmi","Rashmi Naik",25,"C:\\Users\\VIVEK\\Pictures\\Camera Roll\\Rashmi.JPG","Who is your role model and why?","21222","Watching TV","Working in Deloitte","Female","Mumbai","rashmin@gmail.com","9456278344","Male","Rashmi@7834" )
InsertBLOB("Aditya","Aditya Srinivas",30,"C:\\Users\\VIVEK\\Pictures\\Camera Roll\\Aditya.JPG","Are you ambitious?","12121","Painting","Working in Honda","Male","Mumbai","adityas@gmail.com","8624638920","Female","AdityaS@5483" )
InsertBLOB("Karishma","Karishma Tondon",28,"C:\\Users\\VIVEK\\Pictures\\Camera Roll\\Karishma.JPG","Do you like to travel and which place you like the most?","22221","Singing","Working as a Chef","Female","Ahemdabad","karishmat@gmail.com","8279193782","Male","Karishma@6018" )
InsertBLOB("Priyanshu","Priyanshu Patel",25,"C:\\Users\\VIVEK\\Pictures\\Camera Roll\\Priyanshu.JPG","Who is your Favourite actor and actress?","21212","Playing","Working in Railway Sector","Male","Delhi","priyanshup@gmail.com","9716738272","Female","Priyanshu@3412" )
InsertBLOB("Ankita","Ankita Lokhande",23,"C:\\Users\\VIVEK\\Pictures\\Camera Roll\\Ankita.JPG","Do you like to watch Netflix Series?","22211","Dancing","Pursing MS in NIT Mumbai","Female","Mumbai","ankital@gmail.com","8334527819","Male","Ankita@6917" )