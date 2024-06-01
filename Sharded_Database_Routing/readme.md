Design Problem:
You have multiple upstream services, each handling different business use cases. There is also a sharded database, where data is distributed across different shards based on user ID. You need to build a new microservice that will sit between the sharded database and the upstream services. The role of this microservice is to provide the correct connection string for the
corresponding shard of the database based on the user ID.
Requirements:
1. The upstream services will request a connection string by passing a user ID to the new microservice.
2. The microservice should return the connection string for the appropriate database shard based on the provided user ID.
Design Question:
Service Interface Design:
- How would you design the API for the new microservice?
What endpoints and request/response formats would you use?
Shard Mapping Logic:
- How would you implement the logic to map a user ID to the corresponding database shard and its connection string? Describe any data structures or algorithms you would use.
3. Scalability and Fault Tolerance:
- How would you ensure that your microservice can handle high traffic and remain reliable? Discuss any strategies for load balancing, caching, or failover mechanisms.
4. Security:
- How would you secure the communication between the upstream services and your microservice, as well as between your microservice and the database shards?          
5. Deployment and Monitoring:
- What deployment strategies would you recommend for this microservice? How would you monitor the health and performance of the service in a production environment?

I need a detailed system design with hld, lld including design diagram​​​​​​​​​​​​​​​​