# 通过Django+本地mysql调试！
Terminal进入mysql方式：

➜  ~ sudo su

sh-3.2# /usr/local/mysql/bin/mysql -u root -p

Enter password:（your password）

Welcome to the MySQL monitor.  Commands end with ; or \g.

Your MySQL connection id is 23

Server version: 5.7.18

</br>

Copyright (c) 2000, 2017, Oracle and/or its affiliates. All rights reserved.

</br>

Oracle is a registered trademark of Oracle Corporation and/or its

affiliates. Other names may be trademarks of their respective

owners.

</br>

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>

</br>
</br>
</br>
</br>

<h2>MySQL简单用法</h2>

<h3>1、数据库（database）管理</h3>

<h4>1.1 create 创建数据库</h4>

mysql> CREATE DATABASE TESTDB1;
 
<h4>1.2 show 查看所有数据库</h4>

mysql> SHOW DATABASES;
 
<h4>1.3 alter 修改数据库</h4>

alter 命令修改数据库编码：

默认创建的数据库默认不支持中文字符，如果我们需要它支持中文字符，则将它的编码设置为utf8格式：

mysql> ALTER DATABASE TESTDB1 CHARACTER SET UTF8;
 
<h4>1.4 use 使用数据库</h4>

mysql> USE TESTDB1
 
<h4>1.5 查看当前使用的数据库</h4>

mysql> SELECT DATABASE();
 
<h4>1.6 drop 删除数据库</h4>

mysql> DROP DATABASE TESTDB1;

</br>
 
<h3>2、数据表（table）管理</h3>

我们首先创建一个数据库，提供我们往后的使用：

mysql> CREATE DATABASE TESTDB1;

创建后记得用use命令进入（使用）数据库，不然后面的操作都会不成功的。
 
<h4>2.1 create 创建表</h4>

mysql> CREATE TABLE PERSON(
    -> ID INT AUTO_INCREMENT PRIMARY KEY,
    -> NAME VARCHAR(20) NOT NULL,
    -> AGE INT NOT NULL,
    -> BIRTHDAY DATETIME);
 
<h4>2.2 show 显示表</h4>

显示当前数据库所有的数据表

mysql> SHOW TABLES;
 
<h4>2.3 desc 查看表结构</h4>

mysql> DESC PERSON;
 
<h4>2.4 alter 修改表结构（增、删、改）</h4>

默认创建的表不支持中文字符，所以需将表编码设置为utf8：

mysql> ALTER TABLE KEYCHAIN CONVERT TO CHARACTER SET UTF8;
 
<h5>2.4.1 insert 在表中添加列（字段）</h5>

mysql> ALTER TABLE PERSON ADD STAR BOOL;

提示：在MySQL里，布尔类型会自动转换为tinyint(1)类型。
 
<h5>2.4.2 alter 修改表（列）字段</h5>

mysql> ALTER TABLE PERSON MODIFY STAR INT
 
<h5>2.4.3 delete 删除表（列）字段</h5>

mysql> ALTER TABLE PERSON DROP COLUMN STAR;
 
删除字段成功后，我们就不能看到star的字段了。
 
<h5>2.4.4 rename 重命名表名</h5>

mysql> RENAME TABLE PERSON TO NEW_PERSON;
 
<h4>2.5 create 利用已有数据创建新表</h4>

mysql> CREATE TABLE NEW_PERSON SELECT * FROM PERSON;
 
</br>
 
<h3>3、数据的操作及管理</h3>

数据表的基本操作，包含增、删、改、查数据。
 
以下命令均在PERSON表上操作。
 
<h4>3.1 增加数据（增）</h4>

PERSON表目前是没有数据的，它是空的数据表，我们现在先添加一些数据。

insert into 命令添加数据：

mysql> INSERT INTO PERSON VALUES (NULL, 'Lucy', 18, '1999-07-05');

<h4>3.2 删除数据（删）</h4>

delete 命令删除数据：

mysql> DELETE FROM PERSON WHERE NAME = 'Elkins';
 
已经看不到名为“Elkins”的数据了。
 
<h4>3.3 修改数据（改）</h4>

update 命令修改数据：

mysql> UPDATE PERSON SET NAME = 'Gakkiii' WHERE NAME = 'Gakki';
 
查询PEOPLE表内容：

名为“Gakki”的记录已经修改为“Gakkiii”。
 
<h4>3.4 查询数据（查）</h4>

select 命令查询数据，最简单的就是查询表的所有数据：

mysql> SELECT * FROM PERSON;

格式：select * from <表名>，*代表所有字段。 
 
查询数据时也可指定显示的（列）字段：

mysql> SELECT ID, NAME, AGE FROM PERSON;

格式：select <字段名,字段名,...> from <表名>。

