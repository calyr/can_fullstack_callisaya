class StrategyNotification:
    def send(self, processId: str):
        raise NotImplementedError

class Notificator:
    def __init__(self, strategy: StrategyNotification ):
        self.strategy = strategy
    def send(self, processId: str):
        self.strategy.send(processId)

class SMSNotificator(StrategyNotification):
    def send(self, processId: str):
        print(f"Enviando SMS del proceso {processId}")

class EMAILNotificator(StrategyNotification):
    def send(self, processId: str):
        print(f"Enviando email del proceso {processId}")