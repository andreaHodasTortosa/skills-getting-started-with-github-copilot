from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module

BASELINE_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset mutable in-memory activity state for deterministic tests."""
    app_module.activities.clear()
    app_module.activities.update(deepcopy(BASELINE_ACTIVITIES))
    yield
    app_module.activities.clear()
    app_module.activities.update(deepcopy(BASELINE_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture
def baseline_activities():
    return deepcopy(BASELINE_ACTIVITIES)
