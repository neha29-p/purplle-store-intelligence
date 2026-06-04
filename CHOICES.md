# Design Choices & Trade-offs

## Introduction

This document explains the major architectural and implementation decisions made during the development of the Purplle Store Intelligence Platform. Multiple approaches were considered for each major component. The final selections were based on simplicity, maintainability, scalability, and suitability for a prototype retail analytics platform.

---

## 1. Detection Model Selection

### Options Considered

* Haar Cascades
* MobileNet SSD
* YOLOv8

### AI Suggestions

AI-assisted evaluation suggested using YOLOv8 due to its strong balance between detection accuracy, inference speed, and ease of integration.

### Final Choice

YOLOv8

### Rationale

YOLOv8 provides:

* High detection accuracy
* Fast inference times
* Easy Python integration
* Active community support
* Strong performance on people detection tasks

Since visitor counting is a core requirement, accurate person detection was prioritized.

### Trade-off

YOLOv8 requires downloading a model file and uses more computational resources than traditional methods, but the improved detection quality justified the additional complexity.

---

## 2. API Framework Selection

### Options Considered

* Flask
* FastAPI

### AI Suggestions

FastAPI was recommended because of its asynchronous capabilities and automatic OpenAPI documentation.

### Final Choice

FastAPI

### Rationale

FastAPI provides:

* High performance
* Built-in validation
* Automatic Swagger UI generation
* Type hint support
* Easy endpoint development

The framework significantly reduced development effort while improving maintainability.

### Trade-off

FastAPI introduces a slightly steeper learning curve compared to Flask, but the long-term benefits outweighed this concern.

---

## 3. Database Selection

### Options Considered

* Flat CSV Storage
* SQLite
* PostgreSQL

### AI Suggestions

SQLite was suggested for the prototype phase due to its simplicity and zero-configuration setup.

### Final Choice

SQLite

### Rationale

SQLite offers:

* Lightweight deployment
* Transactional support
* Easy local testing
* No server management

This makes it ideal for challenge submissions and prototype systems.

### Trade-off

SQLite is not intended for high-concurrency production workloads. Future versions could migrate to PostgreSQL if scaling becomes necessary.

---

## 4. Logging and Observability

### Options Considered

* No logging
* Standard Python logging
* Middleware-based request logging

### AI Suggestions

Middleware-based logging was recommended because it captures request-level metrics automatically.

### Final Choice

Custom FastAPI Middleware

### Rationale

The middleware records:

* Request method
* Request path
* Response status
* Request latency

This improves observability and simplifies debugging.

### Trade-off

Additional logging introduces minimal overhead but provides significant operational value.

---

## 5. Project Architecture

### Options Considered

* Monolithic script
* Modular architecture

### AI Suggestions

AI-assisted reviews consistently recommended separating business logic into dedicated modules.

### Final Choice

Modular Architecture

### Rationale

Separate folders were created for:

* API services
* Analytics pipelines
* Reports
* Tests

Benefits include:

* Better maintainability
* Easier testing
* Improved readability
* Simpler future expansion

### Trade-off

The structure introduces more files and folders, but improves long-term project organization.

---

## 6. AI-Assisted Development Process

AI tools were used during:

* Architecture planning
* Framework evaluation
* Test generation
* Documentation drafting
* Code reviews

AI-generated suggestions were never accepted blindly. All recommendations were reviewed, modified, executed, and validated through testing before being incorporated into the project.

The final implementation reflects engineering judgment combined with AI-assisted productivity.

---
## 7. Event Schema Design

### Options Considered

* Unstructured log files
* CSV-based event storage
* Structured JSONL event schema

### AI Suggestions

AI-assisted reviews recommended using structured JSON events because they are easier to validate, process, and extend for analytics workflows.

### Final Choice

JSONL Event Schema

### Rationale

The platform generates event logs in JSONL format, where each line represents a single event record.

Supported event types include:

* entry
* exit
* zone_entered

Benefits include:

* Human-readable format
* Easy integration with analytics pipelines
* Streaming-friendly processing
* Flexible schema evolution
* Simple validation and debugging

### Trade-off

JSONL files can become large as event volume increases. Future implementations may migrate event storage to dedicated event-streaming or database solutions while preserving schema compatibility.


## Conclusion

The chosen architecture prioritizes clarity, maintainability, rapid development, and demonstrable business value. While certain decisions favor simplicity over enterprise-scale deployment, the design provides a strong foundation for future expansion into a production-grade retail intelligence platform.
