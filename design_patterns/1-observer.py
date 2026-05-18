#!/usr/bin/env python3
from __future__ import annotations
from typing import Protocol


class Observer(Protocol):
    """
    Protocol defining the observer interface.
    Any class with an update(topic, data) method is a valid observer.
    """
    def update(self, topic: str, data: str) -> None: ...


class NewsSubject:
    """
    Subject that maintains a list of observers and notifies them of events.
    Observers can subscribe to specific topics or receive all events.
    """
    def __init__(self) -> None:
        self._subs: dict[Observer, set[str] | None] = {}

    def subscribe(
        self, observer: Observer, topics: set[str] | None = None
    ) -> None:
        """
        Subscribe an observer to this subject.

        Args:
            observer: The observer to subscribe
            topics: Set of topics to listen to, or None for all topics
        """
        if observer in self._subs:
            return  # ignore duplicate subscribe for same instance
        self._subs[observer] = topics

    def unsubscribe(self, observer: Observer) -> None:
        """Remove an observer from the subscription list"""
        self._subs.pop(observer, None)

    def notify(self, topic: str, data: str) -> None:
        """
        Notify all interested observers about an event.

        Args:
            topic: The event topic
            data: The event data
        """
        for observer, interests in list(self._subs.items()):
            if interests is not None and topic not in interests:
                continue
            observer.update(topic, data)


class LogObserver:
    """Observer that logs events to console"""
    def update(self, topic: str, data: str) -> None:
        print(f"log: {topic}={data}")


class EmailObserver:
    """Observer that sends email notifications"""
    def update(self, topic: str, data: str) -> None:
        print(f"email: {topic}={data}")


class SmsObserver:
    """Observer that sends SMS notifications"""
    def update(self, topic: str, data: str) -> None:
        print(f"sms: {topic}={data}")


def main() -> None:
    subject = NewsSubject()
    log = LogObserver()
    email = EmailObserver()

    subject.subscribe(log, topics={"sports", "breaking"})
    subject.subscribe(email)  # None = receives all topics

    # Subscribe SmsObserver to breaking news only
    sms = SmsObserver()
    subject.subscribe(sms, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
