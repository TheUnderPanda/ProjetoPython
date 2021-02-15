import MySQLdb

con = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="projeto")
con.select_db('projeto')
con = MySQLdb.connect(user='root', db='projeto')
cursor = con.cursor()

sql = "INSERT INTO cliente(nome,sexo,Email,cpf,Telefone,Endereco) VALUES(%s,%s,%s,%s,%s,%s)"
val = ("Lucia",'F',"Corpi@ject.com","85433479373","980843345","Rua liz de lima")
cursor.execute(sql,val)

con.commit()
