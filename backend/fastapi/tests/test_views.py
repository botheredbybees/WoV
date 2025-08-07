import pytest
from main import get_db_cursor

def setup_test_data(cursor):
    # Insert test data
    cursor.execute("""
        INSERT INTO wov.wov_voyages (voyage_id, name) VALUES ('test_voyage', 'Test Voyage');
        INSERT INTO wov.wov_users (user_id, username, email) VALUES ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 'tester', 'tester@example.com');
        INSERT INTO wov.wov_taxa (taxa_id, scientific_name, common_name, inaturalist_taxa_id) VALUES (999, 'Testus maximus', 'Test Species', 12345);
        INSERT INTO wov.wov_observations (observation_id, voyage_id, user_id, wov_taxa_id, latitude, longitude, observed_on)
        VALUES (999, 'test_voyage', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 999, -50.0, 100.0, '2025-01-01');
    """)

def test_darwin_core_export_view(mocker):
    with get_db_cursor() as cursor:
        setup_test_data(cursor)

        # Query the view
        cursor.execute("SELECT * FROM wov.darwin_core_export WHERE \"occurrenceID\" = 'obs-999'")
        result = cursor.fetchone()
        columns = [desc[0] for desc in cursor.description]
        result_dict = dict(zip(columns, result))

        # Assert the result
        assert result_dict['scientificName'] == 'Testus maximus'
        assert result_dict['decimalLatitude'] == -50.0

def test_inaturalist_csv_export_view(mocker):
    with get_db_cursor() as cursor:
        setup_test_data(cursor)

        # Query the view
        cursor.execute("SELECT * FROM wov.inaturalist_csv_export WHERE latitude = -50.0")
        result = cursor.fetchone()
        columns = [desc[0] for desc in cursor.description]
        result_dict = dict(zip(columns, result))

        # Assert the result
        assert result_dict['scientific_name'] == 'Testus maximus'
        assert result_dict['latitude'] == -50.0

def test_ebird_checklist_export_view(mocker):
    with get_db_cursor() as cursor:
        setup_test_data(cursor)

        # Query the view
        cursor.execute("SELECT * FROM wov.ebird_checklist_export WHERE \"Latitude\" = -50.0")
        result = cursor.fetchone()
        columns = [desc[0] for desc in cursor.description]
        result_dict = dict(zip(columns, result))

        # Assert the result
        assert result_dict['Species'] == 'Testus maximus'
        assert result_dict['Latitude'] == -50.0
