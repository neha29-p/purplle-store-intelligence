### Purplle Store Intelligence Platform

### Project Overview

Purplle Store Intelligence Platform is an AI-powered retail analytics solution designed to transform raw CCTV footage and store activity into actionable business intelligence.

The system combines Computer Vision, Visitor Tracking, Occupancy Analytics, Event Processing, and FastAPI-based services to provide real-time visibility into store operations. The platform processes video streams using YOLOv8 person detection, tracks visitor movement, analyzes occupancy trends, and exposes business metrics through REST APIs.

The objective is to help retail operators understand customer behavior, monitor store performance, identify operational bottlenecks, and improve decision-making using data-driven insights.

---

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
├── main.py
├── metrics.py
├── funnel.py
├── anomalies.py
├── database.py
├── health.py
├── logger.py
└── models.py

pipeline/
├── detector.py
├── person_counter.py
├── tracker.py
├── occupancy_analyzer.py
├── camera_analyzer.py
├── process_video.py
├── event_generator.py
├── event_router.py
├── visitor_registry.py
└── zone_manager.py

dashboard/
reports/
tests/

DESIGN.md
CHOICES.md
Dockerfile
docker-compose.yml
requirements.txt
README.md

---

### Technology Stack

### Backend
- Python
- FastAPI
- SQLite

### Computer Vision

- OpenCV
- YOLOv8 (Ultralytics)

### Analytics

- Pandas
- NumPy

### Dashboard

- Streamlit

### Deployment

- Docker
- Docker Compose

---

### Installation

### Clone Repository

git clone https://github.com/neha29-p/purplle-store-intelligence.git
cd purplle-store-intelligence

### Create Virtual Environment

python -m venv .venv

### Activate Environment

Windows PowerShell:

.venv\Scripts\Activate.ps1

### Install Dependencies

pip install -r requirements.txt

---

### Running the API Locally

### Start the FastAPI server:

python -m uvicorn app.main:app --reload --port 8000

### Available URLs (while the application is running):

### API Root:

http://localhost:8000

### Swagger Documentation:

http://localhost:8000/docs

### Health Check:

http://localhost:8000/health

### Example:

curl http://localhost:8000/health

### Expected Response:

{
  "status": "healthy",
  "database": "connected"
}

---

### Running with Docker

## Build and start the application:

docker compose up --build

## After startup:

## API Root:

http://localhost:8000

## Swagger Documentation:

http://localhost:8000/docs

## Health Check:

http://localhost:8000/health

## Stop containers:

docker compose down

---

Running the Analytics Pipeline

Extract CCTV Sample Frames

python tests/extract_first_frames.py

Run YOLO Detection

python tests/test_yolo_frame.py

Run Video Analytics

python tests/test_video_detection.py

Run Visitor Tracking

python tests/test_tracker.py

Run Occupancy Analytics

python tests/test_occupancy_analyzer.py

Generate Store KPI Reports

python tests/store_kpi_report.py

---

API Endpoints

Health Check

GET /health

Store Metrics

GET /stores/{store_id}/metrics

Funnel Analytics

GET /stores/{store_id}/funnel

Anomaly Detection

GET /stores/{store_id}/anomalies

Event Ingestion

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
- Endpoint performance
- Operational debugging

---

### Documentation:

DESIGN.md

### Contains:

- System architecture
- Data flow design
- Processing pipeline overview
- Analytics workflow
- API architecture
- Deployment design
- AI-assisted engineering decisions

CHOICES.md

### Contains:

- Technology selection rationale
- Architectural trade-offs
- Detection model evaluation
- API design decisions
- Storage decisions
- Scalability considerations

---

### AI-Assisted Development

This project was developed using a human-in-the-loop AI-assisted engineering workflow.

AI tools were utilized throughout the development lifecycle to accelerate implementation, explore architectural alternatives, improve documentation quality, generate test scenarios, and review system design decisions.

### Areas Where AI Assistance Was Used

- FastAPI service structure and endpoint design
- Analytics pipeline architecture exploration
- Computer vision workflow planning
- Event ingestion and processing patterns
- Request logging and observability approaches
- Test case generation and validation strategies
- Documentation drafting and refinement
- Dockerization and deployment configuration
- Code review and debugging assistance
- Edge-case identification and validation

### Human Contributions

All AI-generated outputs were manually reviewed, validated, modified, and integrated into the final solution.

The following activities were performed manually:

- System architecture decisions
- Project organization and module design
- Feature selection and prioritization
- Integration of computer vision components
- Validation of analytics workflows
- Testing and debugging
- Documentation verification
- Repository management and deployment
- Final implementation review

### Prompt Engineering Process

### Prompts were iteratively refined to:

- Generate production-oriented code structures
- Improve API design consistency
- Create realistic test scenarios
- Evaluate alternative implementation approaches
- Improve maintainability and readability
- Enhance documentation quality

Prompt histories and modifications have been documented where applicable, particularly within testing and validation workflows.

### Verification

All generated code, configurations, documentation, and recommendations were manually inspected and executed before inclusion in the final repository.

### Functional validation was performed through:

- API testing
- Analytics pipeline execution
- Computer vision processing
- Docker deployment verification
- End-to-end workflow testing

AI assistance accelerated development, while final engineering decisions, validation, and ownership remained the responsibility of the project author.

---

### Author

Neha Pulamarasetti

Purplle Tech Challenge 2026 Submission
