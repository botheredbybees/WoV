# Testing Guide

This document provides an overview of the tests in this project and instructions on how to run them.

## Backend Tests

The backend consists of two main services with tests: the `fastapi` service and the `inaturalist-fetcher` service. The tests are written using the `pytest` framework and utilize mocking to isolate the services from their external dependencies (database, APIs, etc.).

### FastAPI Service Tests

The tests for the FastAPI service are located in `backend/fastapi/tests`.

**File:** `backend/fastapi/tests/test_main.py`

This file contains unit tests for the API endpoints in `main.py`. The tests use `fastapi.testclient.TestClient` to make requests to the endpoints and `pytest-mock` to mock the database interactions.

**Tests:**
- `test_get_taxa`: Tests the `/taxa` GET endpoint.
- `test_get_voyages`: Tests the `/voyages` GET endpoint.
- `test_get_observations`: Tests the `/observations` GET endpoint.
- `test_create_observation`: Tests the `/observations` POST endpoint.

**How to run the tests:**

1.  Make sure you have the dependencies installed. From the root of the project, run:
    ```bash
    pip install -r backend/fastapi/requirements.txt
    ```

2.  Run the tests using `pytest`:
    ```bash
    pytest backend/fastapi/tests/
    ```

### iNaturalist Fetcher Service Tests

The tests for the iNaturalist fetcher service are located in `backend/inaturalist-fetcher/tests`.

**File:** `backend/inaturalist-fetcher/tests/test_fetcher.py`

This file contains unit tests for the functions in `fetcher.py`. The tests use `pytest-mock` to mock the database connection, the iNaturalist API calls, and the Supabase Storage client.

**Tests:**
- `test_fetch_observations_without_images`: Tests the function that fetches observations from the database.
- `test_get_inaturalist_image_url`: Tests the function that gets the image URL from the iNaturalist API.
- `test_upload_image_to_supabase`: Tests the function that uploads an image to Supabase Storage.
- `test_save_image_reference`: Tests the function that saves the image reference to the database.

**How to run the tests:**

1.  Make sure you have the dependencies installed. From the root of the project, run:
    ```bash
    pip install -r backend/inaturalist-fetcher/requirements.txt
    ```

2.  Run the tests using `pytest`:
    ```bash
    pytest backend/inaturalist-fetcher/tests/
    ```

### Database View Tests

The tests for the database views are located in `backend/fastapi/tests`.

**File:** `backend/fastapi/tests/test_views.py`

This file contains unit tests for the database views that are used for exporting data. The tests work by inserting test data into the database, querying the view, and then asserting that the view returns the expected data.

**Tests:**
- `test_darwin_core_export_view`: Tests the `wov.darwin_core_export` view.
- `test_inaturalist_csv_export_view`: Tests the `wov.inaturalist_csv_export` view.
- `test_ebird_checklist_export_view`: Tests the `wov.ebird_checklist_export` view.

**How to run the tests:**

These tests require a running database.

1.  Make sure you have the dependencies installed. From the root of the project, run:
    ```bash
    pip install -r backend/fastapi/requirements.txt
    ```

2.  Run the tests using `pytest`:
    ```bash
    pytest backend/fastapi/tests/test_views.py
    ```

## Frontend Tests

The frontend tests are located in the `frontend/tests` directory. They are written using `vitest` and `@testing-library/svelte`.

**How to run the tests:**

1.  Make sure you have the dependencies installed. From the `frontend` directory, run:
    ```bash
    npm install
    ```

2.  Run the tests using `vitest`:
    ```bash
    npm test
    ```
