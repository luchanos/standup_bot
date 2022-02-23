from clients import TelegramSupportClient
import responses


def test_cli() -> TelegramSupportClient:
    test_url = "https://test_url"
    token = "test_token"
    admin_chat_id = 12345
    client = TelegramSupportClient(base_url=test_url, token=token, admin_chat_id=admin_chat_id)
    return client


@responses.activate
def test_telegram_support_client_success_sending_admin(telegram_send_message_response_success):
    client = test_cli()
    test_message = "test_message_for_sending"
    url = client.create_admin_send_msg_url(test_message)
    responses.add(responses.GET, url,
                  json=telegram_send_message_response_success, status=200)
    resp = client.send_message_to_admin_chat(test_message)
    assert resp.status_code == 200
    assert resp.json() == telegram_send_message_response_success


@responses.activate
def test_telegram_support_client_success_sending_user(telegram_send_message_response_success):
    client = test_cli()
    test_message = "test_message_for_sending"
    chat_id = telegram_send_message_response_success["result"]["chat"]["id"]
    url = client.create_send_msg_url(chat_id=chat_id, message=test_message)
    responses.add(responses.GET, url,
                  json=telegram_send_message_response_success, status=200)
    resp = client.send_message_to_chat(chat_id=chat_id, message=test_message)
    assert resp.status_code == 200
    assert resp.json() == telegram_send_message_response_success
