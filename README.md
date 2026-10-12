# LabAPI Connect (Stateless REST API Engine)

An advanced, corporate-grade backend re-engineering milestone that completely decouples the identity and credential verification core from layout-dependent user interfaces. By incorporating the **Django REST Framework (DRF)**, this application transforms relational model constraints into platform-agnostic, high-performance **REST API Endpoints**. The subsystem operates entirely out-of-band from standard visual presentation layers, communicating across network channels using stateless **JSON (JavaScript Object Notation)** payload strings.

---

## Architectural Overview: Decoupling the Presentation Layer

Within enterprise architectures—and specifically for my **Honors Software Engineering Final Year Project ("Digital Vault")**—the core backend must exist as a pure, headless data utility. 

Traditional application controllers rely on the server rendering heavy visual HTML pages (`login.html` / `register.html`). However, standalone frontend frameworks (such as React or Angular) and mobile runtime targets (Android / iOS applications) cannot consume or render raw server HTML files. They require clean, uniform, structured text arrays. **LabAPI Connect** resolves this by opening programmatic network windows that ingest and broadcast structured data over standard HTTP request protocols.

```text
  [ Client UI: React / Android Mobile App ]
                     │
        Streams Inbound JSON Payload
                     │
                     ▼
    ┌─────────────────────────────────┐
    │     Django REST Framework       │ ◄── [ Serializer Sanitization Layer ]
    └─────────────────────────────────┘
                     │
       Programmatic ORM Database Write
                     │
                     ▼
           [ SQLite Database Core ]
```

---

## System Architectural Layout & API Pipeline

The backend runtime ecosystem manages data transit across a two-tier transformation layer:

### 1. The Serialization Translation Engine 
Because databases only comprehend complex relational structures, while external clients only process raw text strings, a **Serializer** serves as a bidirectional network translator:
* **Inbound (Deserialization):** Captures incoming raw JSON data parameters, checks inputs for type safety, enforces structural rules, and transforms strings into model objects.
* **Outbound (Serialization):** Flattens database model objects down into universal JSON text strings to be streamed across the wire back to the client interface.
* **Security Matrix Hardening:** The serializer embeds an explicit `write_only: True` configuration on password attributes. This architecture permits users to securely submit passwords for account creation, but permanently seals the endpoint from ever leaking or printing cryptographic password hash signatures on outbound data queries.

### 2. Stateless view Controllers 
Eradicates stateful tracking loops and session cookie overhead by employing strict REST guidelines:
* **Explicit HTTP Request Binding:** Implements explicit `@api_view(['POST'])` decorator gates to force strict operational controls, instantly intercepting and dropping unauthorized request methods (such as invalid `GET` queries) with standard `HTTP 405 Method Not Allowed` rejections.
* **Standardized Status Matrix Envelopes:** Returns pure dictionary responses inside `Response()` wrappers that automatically transform into optimized JSON text data payloads matching exact corporate server response parameters:
  * `201 Created` — Emitted upon a successful data ingestion and cryptographic account hashing cycle.
  * `200 OK` — Issued upon successful verification of matching password hashes via `check_password`.
  * `400 Bad Request` — Returned if validation constraints break down, keys are missing, or unique account emails clash.

---

## System Production API Endpoint Matrix

The application opens explicit programmatic channels to process network identity verification transactions:

| API Route | HTTP Method | Inbound Payload Requirements | Outbound Network Response | Primary Security Purpose |
| :--- | :--- | :--- | :--- | :--- |
| `/api/auth/register/` | **POST** | `{ "name": "", "email": "", "password": "" }` | `201 Created` with serialization payload OR `400 Bad Request` | Processes parameters, runs unique constraint lookups, hashes passwords, and writes data to disk. |
| `/api/auth/login/` | **POST** | `{ "email": "", "password": "" }` | `200 OK` with profile confirmation OR `400 Bad Request` | Targets specific SQLite tables via email lookups and cryptographically verifies credentials without tracking UI state. |

---

## Technical Stack & Engineering Skill Profile
* **Framework Core:** Django 5.x / Python 3.x
* **API Toolkit Core:** Django REST Framework (DRF Architecture)
* **Data Transit Format:** JSON (JavaScript Object Notation)
* **Core Concepts Practiced:** ModelSerializer Design, Stateless API Architecture, Inbound Data Streaming Deserialization, HTTP Option Metadata Interception, Explicit Network Status Enum Mapping.

---
*Developed as part of an Advanced Software Engineering portfolio, proving capability in designing headless backend infrastructure and secure stateless authentication gateways.*
