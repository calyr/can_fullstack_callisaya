from typing import Callable, Generator
from pytest_mock import MockerFixture
from strategy import EMAILNotificator, Notificator, SMSNotificator

def test_notificator_uses_sms_strategy_correctly(mocker: Callable[..., Generator[MockerFixture, None, None]]):
    """
    Verifica que el Notificator llama correctamente al método 'send' de la estrategia SMSNotificator.
    """
    # Configuración del mock para SMSNotificator
    sms_strategy = SMSNotificator()
    mock_send = mocker.patch.object(sms_strategy, 'send')
    
    # Ejecución
    notificator = Notificator(sms_strategy)
    process_id = "5298377"
    notificator.send(process_id)
    
    # Verificación
    mock_send.assert_called_once_with(process_id)

def test_notificator_uses_email_strategy_correctly(mocker: Callable[..., Generator[MockerFixture, None, None]]):
    """
    Verifica que el Notificator llama correctamente al método 'send' de la estrategia EMAILNotificator.
    """
    # Configuración del mock para EMAILNotificator
    email_strategy = EMAILNotificator()
    mock_send = mocker.patch.object(email_strategy, 'send')
    
    # Ejecución
    notificator = Notificator(email_strategy)
    process_id = "67890"
    notificator.send(process_id)
    
    # Verificación
    mock_send.assert_called_once_with(process_id)

def test_sms_notificator_sends_message_correctly(capsys):
    """
    Verifica que la estrategia SMSNotificator envía el mensaje correctamente.
    """
    sms_strategy = SMSNotificator()
    
    # Ejecución
    sms_strategy.send("12345")
    
    # Verificación
    captured = capsys.readouterr()
    assert captured.out == "Enviando SMS del proceso 12345\n"

def test_email_notificator_sends_message_correctly(capsys):
    """
    Verifica que la estrategia EMAILNotificator envía el mensaje correctamente.
    """
    email_strategy = EMAILNotificator()
    
    # Ejecución
    email_strategy.send("67890")
    
    # Verificación
    captured = capsys.readouterr()
    assert captured.out == "Enviando email del proceso 67890\n"