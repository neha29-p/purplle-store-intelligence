# Apex Retail Store Intelligence API - Design

## Overview
A high-performance analytics backend designed to ingest real-time CCTV event data, compute retail KPIs, and detect operational anomalies.

## Architecture
- **Framework:** FastAPI (Asynchronous, Type-safe).
- **Storage:** SQLite for lightweight, transactional event storage.
- **Middleware:** Custom request logging for production-grade observability.

## Key Features
- **Metrics Engine:** Real-time calculation of footfall, conversion, and dwell time.
- **Funnel Analysis:** Tracks visitor journey from entrance to checkout.
- **Anomaly Detection:** Identifies critical issues like billing queue spikes.
