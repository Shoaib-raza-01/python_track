# Messaging 


### What are Messaging Queues?

As the name suggests it is a queue where messages are being stored for processing. It is a system that allows asynchronous communication between multiple applications, systems by exchanging messages.

We have mainly three componets in a messaging queues:
1. **Producer** : It is the system/application that generates and sends the message.
2. **Consumer** :These are the applications that processes the message sent by the producer.
3. **Queue**:  A queue is the place where messages are stored until they can be processed by consumers. The producer places each message onto the end of the queue.

![Messaging Queue image](https://www.cloudamqp.com/img/blog/thumb-mq.jpg "Message Queue"){:height="200px" width="200px"}


### Why they are used? 

In modern cloud architecture, applications are decoupled into smaller, independent building blocks that are easier to develop, deploy and maintain. Message queues provide several benefits in communication and coordination for these distributed applications.

1. **Asynchronous Processing** : The producers can send messages to the queue without waiting for any response from consumers. It just puts the message at the rnd of the queue.

2. **Decoupling** : It makes the components communicate without being tightly coupled. This which makes it a lot more easier in maintaining and modifying the application.

3. **Load Balancing** : It helps to distribute the workload across servers as every component work independent of any other.

4. **Scalability** : It can handle the increasing amount of messages suitable for large scale applications.

5. **Reliable Delivery** : The queue ensures that all the messages get delivered to consumers even if there are failures, the messages return to the queue for processing, ensuring no message is lost.

### Enterprise Message Bus

Message queues and Enterprise Message Bus (EMB) are related concepts,
EMB is the wider version and an EMB often incorporates message queues as a core component. 

EMB is a software architectural pattern that supports real-time data exchange between applications. The EMB makes integration easier by performing operations like data transformation, protocol conversion, message routing. Applications pass relevant data to the EMB, and it converts and forwards the data to other applications that need it.

![EMB](https://www.tutorialspoint.com/soa/images/esb_basics.jpg "Enterprise Message Bus"){:height="200px" width="200px"}


There are several tool available for message queues but some of the most popular tool for messaging queues are:
* **Kafka**  
* **RabbitMQ**
* **Amazon SQS**
* **Celery**
* **ActiveMQ**



## reference 

* [Message Queues](https://aws.amazon.com/message-queue/ "Message queue")
* [What is message queue](https://www.cloudamqp.com/blog/what-is-message-queuing.html "What is message queue")
* [Popular Tools](https://stackshare.io/message-queue "Popular tools")
* [Enterprise Message Bus](https://aws.amazon.com/what-is/enterprise-service-bus/ "Enterprise Messaging Bus (EMB)")