#  LabAPI Connect (Headless REST API Core)

This is a standalone, decoupled backend engine designed to move my **Digital Vault Final Year Project (FYP)** away from traditional, heavy server-rendered HTML pages. By incorporating **Django REST Framework (DRF)**, I have transformed my underlying database tables into a series of stateless, platform-agnostic **REST API Endpoints** that communicate purely via compressed **JSON** strings. 

This means the security core can sit on a cloud server while simultaneously powering a web app built in React, or a mobile app running on Android or iOS.

---

##  System Architectural Layout & Operations

The application isolates network data transit across two distinct pipelines:

1. **`labapi_model` (Identity Layer):** Processes user signup and login verification streams. Outbound reads utilize strict `write_only: True` parameters on password rows to ensure cryptographic signatures never leak across the public wire.
2. **`asset_record_model` (Vault Asset Ledger):** Tracks structural meta-information for secure vault documents. It maps strings containing document titles, text descriptions, and classification tags.

---

##  API Endpoint Matrix

| API Route | HTTP Method | Inbound JSON Payload | Outbound Status Code | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| `/api/auth/register/` | **POST** | `{ "name": "", "email": "", "password": "" }` | `201 Created` | Creates a new user profile and cryptographically salts the password string via `make_password`. |
| `/api/auth/login/` | **POST** | `{ "email": "", "password": "" }` | `200 OK` | Verifies matching hashes using `check_password` out-of-band without session state binding. |
| `/api/assets/create/` | **POST** | `{ "title": "", "description": "", "category": "" }` | `201 Created` | Ingests metadata parameters for a secure vault document. |
| `/api/assets/all/` | **GET** | *None (Blank Payload)* | `200 OK` | Uses `many=True` looping parameters to return an aggregate list array of all logged items. |

---

##  Developer Implementation Log & Debugging Notebook

To maintain strong conceptual clarity, I document the exact live-testing obstacles and architectural bug fixes encountered during development:

### ⚡ Case Study 1: Resolving the Login `IntegrityError` Loop
* **The Bug:** During live testing at `/api/auth/login/`, the server crashed with an `IntegrityError: UNIQUE constraint failed: email`. 
* **The Diagnosis:** The application-level `urls.py` matrix was misconfigured, accidentally directing login requests to the registration view controller. The server mistook a sign-in query for a new sign-up attempt. Because the email was already locked down with a `unique=True` field rule, SQLite rejected the operation.
* **The Fix:** Isolated the routes cleanly, binding the login path exclusively to a view logic flow that handles object retrieval (`.objects.get`) and cryptographic string matching instead of calling `.save()`.

### ⚡ Case Study 2: Eradicating the Serializer `AttributeError`
* **The Bug:** Testing the asset creator view initially outputted an `AttributeError: 'list' object has no attribute 'values'`.
* **The Diagnosis:** This was an input payload structure mismatch. The client browser cache transmitted a bracket-enclosed list array (`[...]`) instead of a raw key-value dictionary object (`{...}`). Furthermore, a slight typo in the serializer where `category_tag` was utilized instead of the true database field `category` disrupted parsing.
* **The Fix:** Reconfigured `serializers.py` with explicit assignment operators mapping fields exactly to the schema columns, executed a hard browser cache refresh (`Ctrl + F5`), and locked input structures to single JSON objects.

---

## Tech Stack & Engineering Profile
* **Framework Core:** Django 5.x / Django REST Framework (DRF)
* **Data Transfer Protocol:** Stateless JSON (JavaScript Object Notation)
* **Key Skills Cultivated:** Bidirectional Serializer Mapping, Out-of-band View Architecture, QuerySet Array Manipulation (`many=True`), Forensic Terminal Exception Diagnostics.
