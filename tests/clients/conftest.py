import pytest


@pytest.fixture
def telegram_send_message_response_success() -> dict:
    return {
  'ok': True,
  'result': {
    'message_id': 612,
    'from': {
      'id': 2104221180,
      'is_bot': True,
      'first_name': 'python_intensive',
      'username': 'pythonintensivebot'
    },
    'chat': {
      'id': 362857450,
      'first_name': 'Nikolas',
      'last_name': 'Luchanos',
      'username': 'Luchanos',
      'type': 'private'
    },
    'date': 1645574799,
    'text': 'Restartingbotduetoanerror: Noactiveexceptiontoreraise'
  }
}
