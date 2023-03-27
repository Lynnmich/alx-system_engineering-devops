# 0x09-web_infrastructure_design
A large number of websites are powered by web infrastructures comprising of a single or multiple servers with **LAMP** stacks.

## LAMP(Linux, Apache, MySQL, PHP/Perl/Python)
It is an acronym denoting one of the most common software stacks for many of the web's most popular applications.
Linux for the operating system
Apache HTTP Server
MySQL for the relational database management system
PHP/Perl/Python as the programming language


This project covers designing:
- A one server web infrastructure that hosts the website www.foobar.com
- A three server web infrastructure that hosts the  website www.foobar.com
- A three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored

## 1. One Server Setup.
This is when an entire environment resides on a single server. This includes the web server, the application server and the database server.

### What is a server?

### What is the role of the domain name
The domain name is responsible for mapping human-readable hostnames to their corresponding IP addresses.
In this case; www.foobar.com is the readable domain name while 8.8.8.8 is its current IP address.

### What type of DNS record www is in www.foobar.com
DNS records provide important information about a domain.
www is a CNAME(Canonical Name) DNS record-type in www.foobar.com because it  points to the same IP address as foobar.com.

### What is the role of the web server
It handles  the HTTP protocol.
When it receives a HTTP request, it responds with a HTTP response such as sending back a HTML page or image, send a redirect or delegate the dynamic response generation to some other program.

### Issues with its Infrastructure
1. Poor performance since the application and the database contend for the same server resources ie: CPU, memory.
2. This infrastructure offers little in the way of scalability and component isolation.
3. Using one server isn't horizontally scalable.

### What is the role of the application server

### What is the role of the database

### What is the server using to communicate with the computer of the user requesting the website

