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

## 0. One Server Setup.
This is when an entire environment resides on a single server. This includes the web server, the application server and the database server.

### What is a server?
It  is a piece of computer hardware or software (computer program) that provides functionality for other programs or devices, called "clients." This architecture is called the client–server model.

### What is the role of the domain name?
The domain name is responsible for mapping human-readable hostnames to their corresponding IP addresses.
In this case; www.foobar.com is the readable domain name while 8.8.8.8 is its current IP address.

### What type of DNS record www is in www.foobar.com
DNS records provide important information about a domain.
www is a CNAME(Canonical Name) DNS record-type in www.foobar.com because it  points to the same IP address as foobar.com.

### What is the role of the web server?
It handles  the HTTP protocol.When it receives a HTTP request, it responds with a HTTP response such as sending back a HTML page.

### Issues with its Infrastructure
1. Poor performance since the application and the database contend for the same server resources ie: CPU, memory.
2. This infrastructure offers little in the way of scalability and component isolation. Using one server isn't horizontally scalable because it can quickly become slow once it starts receiving alot of requests.
3. SPOF- If the database(MySQL)is down, then the entire site would be down.

## 1. Distributed Web Infrastructure
This is a distributed web infrastructure that is designed in an attempt to reduce traffic to the primary server by distributing some of the traffic to the replica server with the aid of a loadbalancer.

### What distribution algorithm your load balancer is configured with and how it works
HAProxy (High Availability Proxy) is open source proxy and load balancing server software. It provides high availability at the network (TCP) and application (HTTP/S) layers, improving speed and performance by distributing workload across multiple servers.
The HAProxy loadbalancer is configured with the Round Robin Algorithm. It works by using each server behind the load balancer in turns, according to their weights. It’s also probably the smoothest and most fair algorithm as the servers’ processing time stays equally distributed. As a dynamic algorithm, Round Robin allows server weights to be adjusted on the go.

### Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
In an active-passive setup, the server load balancer recognizes a failed node and redirects traffic to the next available node. 
In an active-active setup, the load balancer spreads out the workload's traffic among multiple nodes. Distribution may be equal, called symmetrical distribution, or uneven –asymmetrical -- depending on the computing power of each node or how an administrator prefers for the active-active cluster to behave. 
Active-passive setup is a strategy that we can use in the context of HAProxy. It is a prominent open-source load balancer and proxy server, to ensure that if one HAProxy instance fails, another instance may take over its job and continue to serve traffic.
In this setup;two or more HAProxy instances are running parallel to each other. The active node is in charge of processing all incoming traffic and forwarding it to the necessary backend servers. The other instances, referred to as passive nodes, are not actively processing traffic but are ready to take over if the active node fails.

### How a database Primary-Replica (Master-Slave) cluster works and what is the difference between the Primary node and the Replica node in regard to the application
The primary-replica  is a database architecture divided into a primary database and replica databases. The replica database serves as the backup for the primary database.
The primary database is actually the keeper of the data resources and also the place where all the writing requests are performed. The reading operations are spread across multiple replica databases relative to the primary database. This architecture is used to enhance the site's reliability to a greater extent.
Primary-replica replication enables data from one database server (the primary) to be replicated to one or more other database servers (the replicas). The primary logs the updates, which then ripple through to the replicas.
The replica outputs a message stating that it has received the update successfully, thus allowing the sending of subsequent updates. 
Primary-Replica replication can be either synchronous or asynchronous. The difference is simply the timing of propagation of changes. If the changes are made to the primary and replica at the same time, it is synchronous. If changes are queued up and written later, it is asynchronous.

### What are the issues with this infrastructure
1. SPOF- If the primary MySQL database server is down, then the entire site would be down.
2. Write operations to primary are hard to scale - Write requests to primary can hardly be scaled. One of the only few options to scale the writing requests is to increase the compute capacity(CPU and ROM) of the primary database.
3. The data being transmitted isn't encrypted using an SSL certificate making it easier for unauthorized access to the network. unauthorized IP addresses can't be blocked since no firewalls have been setup on the servers.

## 2. Secured and Monitored Web Infrastructure
This is a secured and monitored web infrastructure that is designed to monitor network traffic,encrpt HTTP requests and responses and attempt to reduce traffic to the primary server by distributing some of the traffic to the replica server with the aid of a loadbalancer.

### What are firewalls for 
A firewall is a network security device that monitors incoming and outgoing network traffic and permits or blocks data packets based on a set of security rules. Its purpose is to establish a barrier between your internal network and incoming traffic from external sources (such as the internet) in order to block malicious traffic like viruses and hackers.
Firewalls carefully analyze incoming traffic based on pre-established rules and filter traffic coming from unsecured or suspicious sources to prevent attacks. Firewalls guard traffic at a computer’s entry point, called ports, which is where information is exchanged with external devices. For example, “Source address 172.18.1.1 is allowed to reach destination 172.18.2.1 over port 22."
Think of IP addresses as houses, and port numbers as rooms within the house. Only trusted people (source addresses) are allowed to enter the house (destination address) at all—then it’s further filtered so that people within the house are only allowed to access certain rooms (destination ports), depending on if they're the owner, a child, or a guest. The owner is allowed to any room (any port), while children and guests are allowed into a certain set of rooms (specific ports).

### Why is the traffic served over HTTPS
HTTPS is HTTP with TLS encryption. HTTPS uses TLS (SSL) to encrypt normal HTTP requests and responses, making it safer and more secure. A website that uses HTTPS has https:// in the beginning of its URL instead of http://, like https://www.cloudflare.com.
HTTPS uses the SSL/TLS protocol to encrypt communications so that attackers can't steal data. SSL/TLS also confirms that a website server is who it says it is, preventing impersonations. This stops multiple kinds of cyber attacks.

### What monitoring is used for and how the monitoring tool collects data
Infrastructure monitoring is used to collect health and performance data from servers, virtual machines, containers, databases, and other backend components in a tech stack.
Infrastructure monitoring tracks the availability, performance, and resource utilization of hosts, containers, and other backend components. Engineers typically install software, called an agent, on their hosts. Hosts may include physical servers, also called bare metal servers, or virtual machines which use the resources of a physical server. The agent collects infrastructure metrics from hosts and sends the data to a monitoring platform for analysis and visualization. Infrastructure monitoring provides visibility into the health of backend components that run your applications, allowing you to ensure that critical services are available for users and that they work as expected.

### Explain what to do if you want to monitor your web server QPS
Queries per second is a measure of the rate of traffic going through a particular server in relation to a network that serves a Web domain.
Web servers provide a number of important functions. This means there’s much to keep track of, including:
Connections to clients and other servers on the network
Requests for host resources such as CPU, RAM, and disk access
Traffic being transferred to and from the server at any given time
Availability of other web servers for proxying requests
Since web servers handle user requests for content, their performance has an immediate and noticeable impact on the user experience. If your web servers are slow, users will abandon your service for a competitor’s. 

To monitor your web server QPS you can use:
- Open source tools 
They are a great way to monitor web server QPS. These tools are usually free and can be used to monitor a variety of metrics, including QPS. Popular open source tools for monitoring web server QPS include Nagios, Cacti, and Munin. These tools are easy to install and configure, and they provide detailed information about the performance of the web server. However, they may not be suitable for large-scale monitoring, as they may not be able to handle the load.

- Using Cloud-Based Solutions
Cloud-based solutions are becoming increasingly popular for monitoring web server QPS. These solutions are usually hosted in the cloud and provide a range of features and benefits. Popular cloud-based solutions for monitoring web server QPS include Amazon CloudWatch, Microsoft Azure Monitor, and Google Cloud Monitoring. These solutions are designed to handle large-scale monitoring and provide detailed information about the performance of the web server. They are also usually more cost-effective than open source tools.

- Using Network Monitoring Tools
Network monitoring tools are another option for monitoring web server QPS. These tools are designed to monitor the network traffic of the web server and provide detailed information about the performance of the web server. Popular network monitoring tools for monitoring web server QPS include Wireshark, Nmap, and NetFlow. These tools are designed to handle large-scale monitoring and provide detailed information about the performance of the web server. However, they may require additional training to use and may be more expensive than open source tools and cloud-based solutions.

- Using Application Performance Monitoring Tools
Application performance monitoring tools are another option for monitoring web server QPS. These tools are designed to monitor the performance of the web server applications and provide detailed information about the performance of the web server. Popular application performance monitoring tools for monitoring web server QPS include AppDynamics, New Relic, and Dynatrace. These tools are designed to handle large-scale monitoring and provide detailed information about the performance of the web server. However, they may require additional training to use and may be more expensive than open source tools and cloud-based solutions.

###Issues with this Infrastructure
1. SPOF- Having one MySQL server is an issue since its not scalable.
2. If the SSL was to be terminated; this would leave the traffic between the load balancer and the servers unencrypted.

