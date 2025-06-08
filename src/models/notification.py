class Notification:
    def __init__(self):
        self._notifications:list[Notification] = list()

    def add_notification(self, notification: Notification):
        self._notifications.append(notification)

    def get_notifications(self):
        return self._notifications