import pytest
import requests
"""
Test Scenario:
1. Step1
By using requests lib, get pages URL and validate that code status 200
(which stands for valid condition)is displayed
"""
def test():
  response = requests.get("https://sevenbridges.com")
  assert response.status_code == 200

