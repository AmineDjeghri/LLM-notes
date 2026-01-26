---
date modified: Thursday, October 30th 2025, 6:56:42 pm
---


```table-of-contents
```
## News and updates
- item 1
## Easy guides
### When should I use databases instead of files 

**Why not using JSON instead of a database ?**
- moving to SQLite as your first step. It’s local, so you don’t need to deal with remote connections and so on, but it’s optimised much more than a single JSON file.
- It is immediately slower. JSON is for representing data, not storing it. Additionally, if you have multiple users, how are you going to handle them reading and writing to the same file at the same time? Databases will handle data integrity, concurrency etc and they are heavily optimized. JSON is a data transfer format, not a storage format
- There's no real benefit to using a Json file rather than a database.

1. When durable writes matter
    
2. When more than one thing is updating it
    
3. When you're dealing with large data and updating it
    
4. When you want to have marketable life skills
    
5. When you need to ask the data complex questions

[source](https://www.reddit.com/r/node/comments/dfmrlj/when_should_i_consider_a_database_instead_of/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) 

### When to use what?

#### A. JSON Files (`config.json`, `data.json`)

**Concept:** Not a database. It is a serialization format stored on a file system.

- **When to use:**
    
    - **Config:** Hyperparameters for ML models (`learning_rate`, `batch_size`).1
        
    - **Cold Storage:** Saving a dataset to S3 / disk after cleaning.
        
    - **Interchange:** Sending data between two services.
        
- **When NOT to use:**
    
    - **Concurrency:** If two processes write to it, the file corrupts.
        
    - **Search:** You cannot query "Give me users where age > 20" without loading the _entire_ file into RAM ($O(N)$).
        

#### B. Redis (In-Memory Key-Value)

**Concept:** RAM-based structure server.

- **When to use:**
    
    - **Latency is King:** You need data in $< 1ms$.
        
    - **Volatile Data:** If the power goes out and you lose the last 5 seconds of data, it's okay (e.g., a user's session token, a "views" counter).
        
    - **Queues:** Connecting your API to your ML Workers (Celery/BullMQ).
        
- **When NOT to use:**
    
    - **Relational Data:** "Find all orders belonging to User X" is painful in Redis.
        
    - **Large Datasets:** RAM is expensive.2 Storing 1TB of data in Redis costs a fortune; storing it in SQL/Disk is cheap.
        

#### C. SQL (Relational - PostgreSQL/MySQL)

**Concept:** Structured data based on Set Theory. Enforces schemas.

- **When to use:**
    
    - **The "Truth":** User accounts, billing/invoices, inventory.
        
    - **Complex Relations:** "Show me the average revenue per user, grouped by country, joined with the marketing table."
        
    - **Data Integrity:** You need strict constraints (e.g., "You cannot create an Order if the User ID doesn't exist").
        
- **When NOT to use:**
    
    - **Dynamic Schema:** If every row has completely different fields (e.g., scraping different websites with different structures), managing `ALTER TABLE` is a nightmare.
        
    - **Massive Write Ingestion:** SQL struggles with inserting millions of logs per second compared to NoSQL.
        

#### D. NoSQL (Document - MongoDB/DynamoDB)

**Concept:** Schemaless storage (JSON-like documents).

- **When to use:**
    
    - **Unstructured Data:** Storing raw HTML scrapes, chat logs, or JSON responses from external APIs where fields change often.
        
    - **Write Heavy:** Great for logging events or sensor data where write speed > read consistency.
        
    - **Horizontal Scaling:** Sharding (splitting data across servers) is generally easier in NoSQL than SQL.3
        
- **When NOT to use:**
    
    - **Complex Transactions:** "If A pays B, deduct from A and add to B." Doing this safely in NoSQL is much harder than in SQL (ACID).4

### The Architecture Integration (The "Full Stack" View)

In a modern AI production system, you usually use **all of them** together.

**Scenario: Building a ChatGPT Clone**

1. **JSON:**
    
    - `model_config.json`: Stores the temperature and max_tokens settings for the LLM.
        
2. **SQL (PostgreSQL):**
    
    - Stores `Users` (email, password hash) and `SubscriptionPlan` (Free/Pro).
        
    - _Why?_ We cannot afford to lose user data or mess up payments.
        
3. **NoSQL (MongoDB/Cassandra):**
    
    - Stores `ChatHistory`.
        
    - _Why?_ Chats vary in length, have no fixed schema, and grow infinitely. We just dump the conversation logs here.
        
4. **Redis:**
    
    - **Caching:** Stores the context of the _current_ active conversation so the LLM responds instantly.
        
    - **Rate Limiting:** Counts how many requests a user made in the last minute to prevent abuse.
## Tools / libraries 
- item 1

## Papers and research
- item 1

## Other resources 
- item 1