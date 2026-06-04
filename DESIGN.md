# Apex Retail Store Intelligence API - Design

## Overview

The Apex Retail Store Intelligence Platform is an AI-powered analytics system designed to convert raw CCTV footage and retail operational data into actionable business intelligence. The platform combines computer vision, event-driven processing, and REST APIs to provide insights into customer behavior, occupancy patterns, store performance, and operational anomalies.

The primary objective is to help retail operators understand how customers interact with the store environment, monitor occupancy levels, identify bottlenecks, and improve decision-making through data-driven analytics.

---

## System Architecture

The solution is organized into three major layers:

### 1. Computer Vision Layer

This layer processes CCTV footage using YOLOv8 object detection models. Video frames are analyzed to identify people within the store environment. The output from the detection stage is passed to visitor tracking and occupancy analysis modules.

Key responsibilities:

* Person detection
* Frame processing
* Visitor counting
* Camera-wise analytics
* Occupancy estimation

### 2. Analytics Pipeline Layer

The analytics pipeline transforms raw detections into meaningful business events.

Responsibilities include:

* Visitor tracking
* Occupancy monitoring
* Entry and exit analysis
* Event generation
* Funnel analytics
* Camera aggregation

This modular design allows additional analytics modules to be integrated without affecting the rest of the system.

### 3. API Layer

The FastAPI backend exposes analytics through REST endpoints.

Supported services include:

* Store metrics
* Funnel analytics
* Anomaly detection
* Health monitoring
* Event ingestion

The API layer acts as the interface between analytics services and client applications such as dashboards and reporting systems.

---

## Data Flow

1. CCTV footage is processed frame by frame.
2. YOLOv8 detects individuals in each frame.
3. Tracking modules associate detections across frames.
4. Occupancy statistics are calculated.
5. Events are generated and stored.
6. Metrics and analytics are computed.
7. FastAPI endpoints expose the results.
8. Dashboards consume API responses for visualization.

---

## Storage Strategy

SQLite was selected as the persistence layer for the prototype implementation.

Advantages:

* Zero configuration
* Lightweight deployment
* Easy portability
* Reliable transactional support

For large-scale deployments, the design can be extended to PostgreSQL or cloud-native storage solutions without significant architectural changes.

---
## Staff Exclusion Strategy

Store employees can generate large amounts of movement data that may distort customer analytics.

To prevent inaccurate business metrics, all analytics queries exclude events where:

is_staff = true

This ensures that occupancy counts, funnel analytics, zone engagement metrics, and conversion calculations represent customer behavior only.

Staff events remain available for operational analysis but are excluded from customer-facing business intelligence metrics.
---
## Re-entry Handling

Visitors may leave the store and return later during the same day.

The platform maintains a visitor registry and tracks visit counts for previously observed visitors.

When a known visitor re-enters the store, an additional entry event is generated while preserving the visitor identity and visit history.

This approach supports:

* Repeat visitor analysis
* Accurate footfall measurement
* Visit frequency analytics
* Customer journey reconstruction
---
## Edge-Case Handling

Several edge cases were considered during system design.

### Temporary Occlusion

Visitors may briefly disappear behind shelves or other shoppers. Tracking logic attempts to maintain identity continuity across short gaps.

### Counting Line Boundary Conditions

Visitors moving near the counting boundary are only counted when crossing direction is detected, reducing duplicate entries and exits.

### Empty Store Conditions

Analytics modules safely handle scenarios with zero visitors without causing divide-by-zero errors.

### Queue Abandonment

Visitors leaving the billing queue before service completion generate queue_abandoned events and are excluded from purchase conversions.

### Staff Exclusion

Employee movements are excluded from customer analytics using the is_staff flag.

### Visitor Re-entry

Returning visitors are tracked through persistent visitor identifiers to support repeat visit analytics.
---

### Observability and Monitoring

Production readiness is improved through middleware-based request logging.

Each API request records:

* Request method
* Request path
* Response status code
* Request latency

Example:

2026-06-02 13:19:26 - retail_api - INFO - GET /stores/ST1008/metrics 200 - 0.0057s

This improves debugging, performance monitoring, and operational visibility.

---

## Scalability Considerations

The system is designed with modularity in mind.

Future improvements may include:

* Multi-camera synchronization
* Distributed event processing
* Cloud deployment
* Real-time streaming analytics
* Advanced visitor re-identification
* PostgreSQL migration
* Message queue integration

---

## AI-Assisted Decisions

AI-assisted engineering tools were used throughout the development lifecycle to accelerate implementation and evaluate architectural alternatives.

AI support was used for:

* Evaluating FastAPI versus Flask
* Reviewing database options
* Generating test case ideas
* Improving API structure
* Reviewing middleware implementations
* Enhancing documentation quality

All generated recommendations were reviewed, modified, validated, and tested before inclusion in the final project.

The final implementation decisions remained under developer control and were validated through execution and testing.

## Event Logging Strategy

The platform generates structured event logs in JSONL (JSON Lines) format to support analytics, reporting, auditing, and downstream processing workflows.

Event logs are stored at:

data/events/events.jsonl

Each line in the file represents a single event record encoded as a valid JSON object. This approach enables efficient event streaming, easy validation, and compatibility with analytics pipelines.

### Supported Event Types

* entry
* exit
* zone_entered

### Example Event

```json
{"event_type":"entry","id_token":"ID_1001","store_code":"store_1076","camera_id":"cam1","event_timestamp":"2026-06-04T18:00:00","is_staff":false}
