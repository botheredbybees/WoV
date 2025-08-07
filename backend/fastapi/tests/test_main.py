import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_taxa(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchall.return_value = [
        (1, 'Pygoscelis adeliae', 'Adelie Penguin'),
        (2, 'Aptenodytes forsteri', 'Emperor Penguin'),
    ]
    mock_cursor.description = [('taxa_id',), ('scientific_name',), ('common_name',)]

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Make the request
    response = client.get("/taxa")

    # Assert the response
    assert response.status_code == 200
    assert response.json() == [
        {'taxa_id': 1, 'scientific_name': 'Pygoscelis adeliae', 'common_name': 'Adelie Penguin'},
        {'taxa_id': 2, 'scientific_name': 'Aptenodytes forsteri', 'common_name': 'Emperor Penguin'},
    ]
    mock_cursor.execute.assert_called_once_with("SELECT * FROM wov.wov_taxa")

def test_get_voyages(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchall.return_value = [
        ('VOY001', 'Antarctic Expedition 2025'),
        ('VOY002', 'Southern Ocean Transect'),
    ]
    mock_cursor.description = [('voyage_id',), ('name',)]

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Make the request
    response = client.get("/voyages")

    # Assert the response
    assert response.status_code == 200
    assert response.json() == [
        {'voyage_id': 'VOY001', 'name': 'Antarctic Expedition 2025'},
        {'voyage_id': 'VOY002', 'name': 'Southern Ocean Transect'},
    ]
    mock_cursor.execute.assert_called_once_with("SELECT * FROM wov.wov_voyages")

def test_get_observations(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchall.return_value = [
        (1, 'Emperor Penguin'),
        (2, 'Orca'),
    ]
    mock_cursor.description = [('observation_id',), ('species_guess',)]

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Make the request
    response = client.get("/observations")

    # Assert the response
    assert response.status_code == 200
    assert response.json() == [
        {'observation_id': 1, 'species_guess': 'Emperor Penguin'},
        {'observation_id': 2, 'species_guess': 'Orca'},
    ]
    mock_cursor.execute.assert_called_once_with("SELECT * FROM wov.wov_observations")

def test_create_observation(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchone.return_value = (123,)  # New observation ID

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Observation data
    observation_data = {
        "species_guess": "New Species",
        "latitude": 0.0,
        "longitude": 0.0,
    }

    # Make the request
    response = client.post("/observations", json=observation_data)

    # Assert the response
    assert response.status_code == 200
    assert response.json() == {"observation_id": 123}

    # Assert that execute was called
    mock_cursor.execute.assert_called_once()

def test_get_users(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchall.return_value = [
        ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 'tester', 'tester@example.com', 'scientist'),
    ]
    mock_cursor.description = [('user_id',), ('username',), ('email',), ('role',)]

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Make the request
    response = client.get("/users")

    # Assert the response
    assert response.status_code == 200
    assert response.json()[0]['username'] == 'tester'
    mock_cursor.execute.assert_called_once_with("SELECT * FROM wov.wov_users")

def test_get_user(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchone.return_value = ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 'tester', 'tester@example.com', 'scientist')
    mock_cursor.description = [('user_id',), ('username',), ('email',), ('role',)]

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Make the request
    response = client.get("/users/a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13")

    # Assert the response
    assert response.status_code == 200
    assert response.json()['username'] == 'tester'

def test_update_user(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Make the request
    response = client.put("/users/a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13", json={"username": "new_tester"})

    # Assert the response
    assert response.status_code == 200
    mock_cursor.execute.assert_called_once()

def test_get_voyage(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchone.return_value = ('VOY001', 'Antarctic Expedition 2025')
    mock_cursor.description = [('voyage_id',), ('name',)]

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Make the request
    response = client.get("/voyages/VOY001")

    # Assert the response
    assert response.status_code == 200
    assert response.json()['name'] == 'Antarctic Expedition 2025'

def test_update_voyage(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Make the request
    response = client.put("/voyages/VOY001", json={"name": "New Voyage Name"})

    # Assert the response
    assert response.status_code == 200
    mock_cursor.execute.assert_called_once()

def test_get_observation(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchone.return_value = (1, 'Emperor Penguin')
    mock_cursor.description = [('observation_id',), ('species_guess',)]

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Make the request
    response = client.get("/observations/1")

    # Assert the response
    assert response.status_code == 200
    assert response.json()['species_guess'] == 'Emperor Penguin'

def test_update_observation(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Make the request
    response = client.put("/observations/1", json={"species_guess": "New Species"})

    # Assert the response
    assert response.status_code == 200
    mock_cursor.execute.assert_called_once()

def test_get_images(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchall.return_value = [
        ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a14', 'path/to/image.jpg', 1),
    ]
    mock_cursor.description = [('image_id',), ('file_path',), ('observation_id',)]

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Make the request
    response = client.get("/images")

    # Assert the response
    assert response.status_code == 200
    assert response.json()[0]['file_path'] == 'path/to/image.jpg'

def test_delete_image(mocker):
    # Mock the database cursor
    mock_cursor = mocker.MagicMock()

    # Mock the get_db_cursor context manager
    mock_context_manager = mocker.patch('main.get_db_cursor')
    mock_context_manager.return_value.__enter__.return_value = mock_cursor

    # Make the request
    response = client.delete("/images/a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a14")

    # Assert the response
    assert response.status_code == 200
    mock_cursor.execute.assert_called_once()
