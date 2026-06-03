### Purplle Store Intelligence Platform

### Project Overview:
Purplle Store Intelligence Platform is an AI-powered retail analytics solution designed to transform raw CCTV footage and store activity into actionable business intelligence.

The system combines Computer Vision, Visitor Tracking, Occupancy Analytics, Event Processing, and FastAPI-based services to provide real-time visibility into store operations. The platform processes video streams using YOLOv8 person detection, tracks visitor movement, analyzes occupancy trends, and exposes business metrics through REST APIs.

The objective is to help retail operators understand customer behavior, monitor store performance, identify operational bottlenecks, and improve decision-making using data-driven insights.

### Key Features

### Computer Vision Analytics

- YOLOv8-based person detection
- CCTV footage processing
- Visitor counting and tracking
- Camera-wise traffic analysis
- Occupancy monitoring
- Entry and exit analytics

### Retail Intelligence

- Footfall analytics
- Conversion funnel analysis
- Visitor behavior insights
- Queue monitoring
- Anomaly detection
- Store performance metrics

### Data Engineering & Observability

- Automated analytics pipelines
- Structured event generation
- SQLite-based event storage
- Request logging middleware
- Health monitoring endpoints
- Modular and scalable architecture

### API Services

- FastAPI REST APIs
- Store metrics endpoints
- Funnel analytics endpoints
- Anomaly detection endpoints
- Event ingestion APIs

---

### Project Structure

app/
│
├── main.py
├── metrics.py
├── funnel.py
├── anomalies.py
├── database.py
├── health.py
├── logger.py
└── models.py

pipeline/
│
├── detector.py
├── person_counter.py
├── tracker.py
├── occupancy_analyzer.py
├── camera_analyzer.py
├── process_video.py
└── event_generator.py

reports/
tests/

DESIGN.md
CHOICES.md
requirements.txt
README.md



### Technology Stack

- Python
- FastAPI
- OpenCV
- YOLOv8 (Ultralytics)
- SQLite
- Pandas
- NumPy
- Streamlit

---

### Installation

### Clone Repository

git clone https://github.com/neha29-p/purplle-store-intelligence.git
cd purplle-store-intelligence

Install Dependencies

pip install -r requirements.txt

---

Running the API

Start the FastAPI server:

python -m uvicorn app.main:app --reload --port 8000

API:

http://localhost:8501

Swagger Documentation:

http://localhost:8000/docs

---

Running the Analytics Pipeline

Extract CCTV sample frames:

python tests/extract_first_frames.py

Run YOLO detection:

python tests/test_yolo_frame.py

Run video analytics:

python tests/test_video_detection.py

Run visitor tracking:

python tests/test_tracker.py

Run occupancy analytics:

python tests/test_occupancy_analyzer.py

---

API Endpoints

Health Check:
GET /health

Store Metrics:
GET /stores/{store_id}/metrics

Funnel Analytics:
GET /stores/{store_id}/funnel

AnomalyDetection: GET/stores/{store_id}/anomalies

Event Ingestion:
POST /api/events

---

### Data Observability

The platform includes request-level observability through custom middleware logging.

Example log output:

2026-06-02 13:19:26 - retail_api - INFO - GET /stores/ST1008/metrics 200 - 0.0057s

This enables monitoring of:

- API latency
- Request paths
- HTTP status codes
- Service availability

---

### Documentation

DESIGN.md

### Contains:

- System architecture
- Data flow design
- Processing pipeline overview
- AI-assisted engineering decisions

CHOICES.md

### Contains:

- Technology selection rationale
- Architectural trade-offs
- Detection model evaluation
- API design decisions

---

### AI-Assisted Development

AI tools were used to accelerate development, generate implementation alternatives, review architectural decisions, improve documentation, and assist with testing workflows. All generated code and recommendations were reviewed, validated, modified, and tested before inclusion in the final solution.

---

### Author

Neha Pulamarasetti

Purplle Tech Challenge 2026 Submission 
