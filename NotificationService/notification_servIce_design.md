**Design a serverless architecture for a notification service that efficiently sends personalized notifications to users, ensuring exactly-once delivery and scalability to handle high traffic.**

## ⌛ Max time: 30 mins

## 📜 **Requirements:**

1. **Notification Processing:**
    - Design a serverless architecture to process notification requests, including message transformation, filtering, and delivery.
2. **Idempotence:**
    - Ensure exactly-once delivery of notifications using idempotent design patterns to prevent duplicate notifications.
3. **Decoupling:**
    - Utilize design patterns to decouple notification processing from notification delivery, promoting modularity and flexibility.
4. **Scalability and Performance:**
    - Ensure the architecture can handle a throughput of 500 requests per second and provide a responsive user experience.
5. **Fault Tolerance:**
    - Implement fault-tolerant mechanisms to handle failures gracefully.

Steps:

1. **Functional Requirements:**
- Exactly-Once Delivery
- Personalized
- Serverless Services
- Types of Notification - Push, SMS, WhatsApp, Email


2. **Non Functional Requirements:**
- Idempotency
- Highly Scalable [May be scalable for around 10 M Requests per day]
- Near to Real-time processing
- Scheduling of notification

3. **Services:**
- Producer -> Producer will send notification requests to the SMS/Email Client. I have to construct a dynamic notification request
- SMS Service -> We can use AWS lambda to process any business communication
- AWS SNS -> This will be used to send any notification to any consumer with high availability and scalability
- AWS SES -> This will be used in case sending email notifications
- 3rd Party SMS Service -> Like Infobip or Twilio we can use it as default sms service or respective such process related services which will be invoke AWS SNS if anything goes wrong
- FCM - Like Firebase to send push notification to target devices with device token
- API Gateway - This will provide an API to producer and route requests to notification service(lambdas) with proper parameters
- DB Schema - For Notification I need notification consumer's details like in this schema:

**Users Schema:**

* userId: PK
* email: to send email
* phone_number: to send SMS and whatsapp
* device_token: to send push notification
* created_at:
* updated_at:

