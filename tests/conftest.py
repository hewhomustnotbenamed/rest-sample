import pytest
from flask import Flask


@pytest.fixture
def app() -> Flask:
    """ Provides an instance of our Flask app """
    from rest_sample import create_app

    return create_app()
