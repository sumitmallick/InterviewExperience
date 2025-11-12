````markdown
# 🧩 Ratings & Review System – Product Delisting Architecture

This document explains the **architecture design** for handling **product delisting** in an e-commerce **Ratings & Reviews system**, ensuring consistency, scalability, and data cleanup across microservices, cache, and analytics.

---

## 🧠 Problem Statement

In an e-commerce platform:

- Each product can have multiple **reviews and ratings** submitted by verified users after order delivery.
- Over time, products can get **delisted** due to end-of-life, compliance, or supplier issues.
- Once delisted:
  - The product should no longer appear in listings.
  - Its reviews and ratings should be **hidden or deleted**.
  - All cached data and aggregates (in Redis, DB, search index, etc.) should be cleaned up.
  - Historical data may need to be archived for **auditing or analytics**.

The challenge is to:
- Maintain **data integrity** across services.
- Handle **asynchronous cleanup** efficiently.
- Keep the system **scalable**, **event-driven**, and **resilient** to partial failures.

---

## 🧩 Solution Overview

The design uses an **event-driven microservices architecture** powered by **Kafka/SNS** and distributed caching (Redis).

### 🏗️ Key Goals

| Goal | Approach |
|------|-----------|
| ✅ Data consistency | Soft delete + event-driven hard cleanup |
| ⚡ Fast updates | Asynchronous events via Kafka |
| 🧠 Scalable reads | Cached aggregates in Redis |
| 💾 Safe archival | Cold storage (S3 / Glacier) |
| 🔁 Resilience | Idempotent cleanup + retries via DLQs |

---

## 🧮 High-Level Architecture (Mermaid.js)

```mermaid
flowchart TD
    %% Main Components
    subgraph ProductDomain["Product Domain"]
        PS[Product Service]
    end
    
    subgraph Messaging["Event Bus"]
        EB[(Kafka / SNS / PubSub)]
    end
    
    subgraph ReviewDomain["Review Domain"]
        RS[Review Service]
        RD[(ReviewDB)]
        RC[(Redis Cache)]
        RW[Review Cleanup Worker]
    end
    
    subgraph RatingDomain["Rating Domain"]
        RA[Rating Aggregator]
        RG[(RatingDB)]
    end
    
    subgraph SearchDomain["Search & Indexing"]
        SI[Search Index - Elasticsearch]
    end
    
    subgraph AnalyticsDomain["Analytics & Archival"]
        ADW[(Data Lake / Analytics DB)]
        ARW[Archive Worker - S3 / Glacier]
    end
    
    subgraph Client["Frontend / User Side"]
        UI[Product Page / Admin Console]
    end
    
    %% Normal Review Flow
    RS -->|Write Reviews| RD
    RS -->|Cache Ratings & Top Reviews| RC
    RS -->|Emit ReviewCreated| EB
    EB --> RA
    RA --> RG
    RA --> RC
    
    %% Product Delist Flow
    PS -->|ProductDelisted Event| EB
    EB -->|ProductDelisted| RS
    EB -->|ProductDelisted| RA
    EB -->|ProductDelisted| SI
    EB -->|ProductDelisted| ADW
    
    %% Review Service Handles Delist
    RS -->|Mark reviews as DELETED| RD
    RS -->|Delete keys - ratings, reviews| RC
    RS -->|Emit ReviewsPurged Event| EB
    RS --> RW
    
    %% Rating Aggregator Cleanup
    RA -->|Remove product ratings| RG
    RA -->|Delete rating cache| RC
    
    %% Search Cleanup
    SI -->|Delete indexed reviews| SI
    
    %% Analytics Cleanup & Archive
    ADW -->|Update aggregates| ADW
    ADW --> ARW
    
    %% Archive Worker
    ARW -->|Upload deleted reviews to cold storage| ARW
    
    %% Users & UI
    UI -->|View reviews - active products only| RS
    UI -->|Trigger manual delist| PS
````

🔗 **Live Editor:** [View Diagram in Mermaid Live Editor](https://mermaid.live/edit#pako:eNqFVm1v2jAQ_iuWpU2tBB2F8vphEgTaobUVIjCkwT64sRsskhjZDm1X-t93iZ1A0q7wocK-u-ce391z5RV7gjLcw4-BePLWRGo0G64iBJ8vX9Ad4RFyRLgVEYu0MvcqfvAl2a7RRAoae3ooQnBbrrA9I3Oxwn-Mf_KZuMvM6jK54x6zRhZR86WEfceUIj6PfMAd7SA5GsSqADkaLM9-kscNQd-Qe-_C30n84MYP5yeQp2zH2VNO2hw_4jx1l9ZYpJzahsszCzQ4P753knvKFXKIt2YF0yKDcwJGoniLFkJumDxFl2iowoFuevyQbn9pjX3fl8wnWshj8w0wM1iDUyVyGZHeOs9pjugrGkeUPQNCIa87XlqH1IyqaBQQpbmn0tsTqfoRCV4S5zxbfgMJ-wDAdyQoJOwPF8uzIdEE3ZINg74fIorN6EPJDQKztQZybgMibgLi8ZOldwIOgweUrqWINHhB5FwBisspK1Caj_PxnhA_5UTDVDqREsF_Zh30dS9kSAI7kugaJGhMUxdVq9_3C8k1s1a1h6ErWNMJs_ORFGsmtke-TsF3FHJtjY5kRDO6BwEZl9EgcYH5sRF9c7wpHp0S9VzsLOBKH3GfmIzZckjNjKJUxOWkZS_g7Z6w9z-3u-PP7TA8pYcUNY5-kIgGTNl3FYp4R-QGSVNhRMBldDuajYbvGgOhDPq2YS8KBk6aBlWyyM96oyax9N8XyzjCBilTL-s9Wy3HrdtPWShAAVvbMMtnX-pwxtqYkZcM1_59263UC3nc8TEAT7YAvCF_btaSHOOg12wTZkpnxgealCLOtxRGFRH7PqaO-md9EpGX4QuSt97TDDEQhCKaUs05Ii2QJwKKFNQQ9Lv_ADURfqKyuX3N3Dz6VzI7GUwVEU_zQ60VElHwchhqGzOT3PdhjYTwdlA_TSdtD8LBFexLTnFPy5hVcMhgOyRH_JrEr7BesxAWTw--UpjFFV5FbxCzJdFvIcIsTIrYX-PeIwkUnOK0hkNOYKeF-a2EXcSkI-JI495lvZuC4N4rfsa9evui2a11ms3LVr3dbtY7VxX8Atf1xkWjftW9ana79fZlq9l5q-C_ad7aRbdVb9ZqtUazDTGdFuDBP0Eo5p35cZH-xnj7B_q7mMw)

---

## ⚙️ Workflow Summary

### **1. Product Delisting**

* `Product Service` publishes a `ProductDelisted` event.
* The event is broadcast through **Kafka / SNS** to all consuming services.

### **2. Review Service Actions**

* Marks all product reviews as `DELETED`.
* Clears relevant cache keys:

  * `ratings:<product_id>`
  * `reviews:<product_id>:latest`
* Emits a secondary event `ReviewsPurged` for downstream sync.

### **3. Rating Aggregator**

* Removes product-level aggregates from `RatingDB` and Redis.

### **4. Search Service**

* Deletes the product’s indexed reviews from Elasticsearch.

### **5. Analytics & Archive**

* Updates historical aggregates.
* Moves deleted reviews to **S3 / Glacier** via Archive Worker.

---

## 🧠 Technical Highlights

| Component                 | Responsibility                                          |
| ------------------------- | ------------------------------------------------------- |
| **Review Service**        | Review CRUD, cache invalidation, deletion orchestration |
| **Rating Aggregator**     | Rating summary maintenance                              |
| **Review Cleanup Worker** | Batch hard-deletes reviews post-retention               |
| **Event Bus (Kafka/SNS)** | Reliable asynchronous communication                     |
| **Redis Cache**           | Caches hot data (reviews, ratings)                      |
| **Elasticsearch**         | Search index for review discovery                       |
| **S3 / Glacier**          | Cold storage for archived reviews                       |
| **Data Lake / Analytics** | Maintains historical insights and reports               |

---

## 🔁 Improvisations Implemented

1. **Event-Driven Cleanup:**

   * Instead of synchronous DB and cache cleanup, uses `ProductDelisted` → multi-subscriber pattern.
2. **Soft + Hard Delete Combo:**

   * Safe rollback via soft delete, permanent cleanup via background worker.
3. **Tag-based Redis Keys:**

   * Enables pattern-based bulk cache deletion (`{product:ID}` tagging).
4. **Cold Storage Archival:**

   * Historical review data preserved for BI/compliance.
5. **Idempotent Event Handling:**

   * All deletion operations are idempotent to prevent double-processing.

---

## 🚀 Improvement Opportunities

| Area                  | Enhancement                                        | Impact                            |
| --------------------- | -------------------------------------------------- | --------------------------------- |
| **Cache Consistency** | Implement Redis Streams for async refresh tracking | Faster cache rebuild after delist |
| **Observability**     | Add distributed tracing (Jaeger / OpenTelemetry)   | End-to-end visibility             |
| **Compliance**        | Integrate PII masking in archive layer             | GDPR & privacy compliance         |
| **Disaster Recovery** | Enable multi-region data replication               | Fault tolerance                   |
| **Performance**       | Use Redis Cluster with keyslot hashing             | Sub-millisecond cache lookups     |
| **Automation**        | Scheduled cleanup pipelines                        | Reduced ops overhead              |

---

## ✅ Summary

This architecture provides a **scalable**, **event-driven**, and **self-healing** approach to handling **product delisting** and **review cleanup** in an e-commerce ecosystem.

**Core Principles:**

* Event-driven microservices
* Cache-first reads
* Asynchronous cleanup
* Auditable and reversible data management

---

### 🧩 System Characteristics

| Attribute              | Value                                         |
| ---------------------- | --------------------------------------------- |
| **Architecture Style** | Event-Driven Microservices                    |
| **Communication**      | Asynchronous via Kafka/SNS                    |
| **Storage**            | Polyglot (Postgres, Redis, Elasticsearch, S3) |
| **Consistency Model**  | Eventual consistency                          |
| **Data Retention**     | Configurable (e.g., 30-day soft delete)       |
| **Security**           | Role-based admin delist actions, audit logs   |
| **Scalability**        | Horizontally scalable per domain service      |

---

### 👨‍💻 Author

**Designed by:** System Design GPT (Architecture & Scalability Specialist)
**Last Updated:** November 2025

---

```

---

Would you like me to add a **section showing cache schema (Redis key design + invalidation flow)** at the bottom of this `README.md` for completeness?
```
