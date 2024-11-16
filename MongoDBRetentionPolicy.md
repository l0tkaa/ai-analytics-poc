# MongoDB Retention Policy for Raw Data

This document outlines the retention policy for the raw data stored in the `rawDataDB` database. The policy ensures that data is retained only for a specified duration, improving storage efficiency and maintaining compliance with data management practices.

---

## **Purpose**
The retention policy is designed to:
1. Automatically delete raw data older than 90 days.
2. Manage data efficiently while maintaining relevant records.
3. Provide flexibility for advanced retention rules using custom scripts.

---

## **Implementation**

### **1. Retention Period**
- **Duration**: 90 days
- **Target Collection**: `rawData`

### **2. Adding a Timestamp Field**
Ensure every document in the collection has a `createdAt` field that represents its insertion time.

```javascript
db.rawData.insertOne({
    data: "Sample raw data",
    source: "Sensor1",
    createdAt: new Date() // Automatically add timestamp
});
```

Create TTL index
Create Custom Retention Logic
Monitor with MongoDB Atlas, Prometheus, or Grafana
