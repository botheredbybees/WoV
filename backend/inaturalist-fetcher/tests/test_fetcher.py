import pytest
from unittest.mock import MagicMock, patch
from fetcher import fetch_observations_without_images, get_inaturalist_image_url, upload_image_to_supabase, save_image_reference

@patch('fetcher.get_db_connection')
def test_fetch_observations_without_images(mock_get_db_connection):
    # Mock the connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db_connection.return_value = mock_conn
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

    # Define the return value for fetchall
    mock_cursor.fetchall.return_value = [
        {'observation_id': 1, 'inaturalist_observation_id': 123},
        {'observation_id': 2, 'inaturalist_observation_id': 456},
    ]

    # Call the function
    observations = fetch_observations_without_images()

    # Assert the results
    assert len(observations) == 2
    assert observations[0]['observation_id'] == 1
    mock_cursor.execute.assert_called_once()

@patch('fetcher.requests.get')
def test_get_inaturalist_image_url(mock_get):
    # Mock the requests.get call
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "results": [{
            "photos": [{"url": "http://example.com/image.jpg"}]
        }]
    }
    mock_get.return_value = mock_response

    # Call the function
    image_url = get_inaturalist_image_url(123)

    # Assert the results
    assert image_url == "http://example.com/image.jpg"
    mock_get.assert_called_once_with("https://api.inaturalist.org/v1/observations/123")

@patch('fetcher.supabase')
@patch('fetcher.requests.get')
def test_upload_image_to_supabase(mock_requests_get, mock_supabase):
    # Mock the requests.get call for the image
    mock_image_response = MagicMock()
    mock_image_response.status_code = 200
    mock_image_response.content = b'imagedata'
    mock_requests_get.return_value = mock_image_response

    # Mock the supabase storage upload
    mock_storage_from = MagicMock()
    mock_supabase.storage.from_.return_value = mock_storage_from

    # Call the function
    file_path = upload_image_to_supabase("http://example.com/image.jpg", 1)

    # Assert the results
    assert file_path is not None
    mock_storage_from.upload.assert_called_once()

@patch('fetcher.get_db_connection')
def test_save_image_reference(mock_get_db_connection):
    # Mock the connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db_connection.return_value = mock_conn
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

    # Call the function
    save_image_reference(1, "path/to/image.jpg")

    # Assert that execute and commit were called
    mock_cursor.execute.assert_called_once()
    mock_conn.commit.assert_called_once()
