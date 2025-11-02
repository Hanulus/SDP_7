"""
Observer Pattern Implementation - YouTube Channel Notification System
Clean Code Principles Applied:
- Single Responsibility Principle
- Open/Closed Principle
- Clear naming conventions
- Proper encapsulation
"""

from abc import ABC, abstractmethod
from typing import List
from datetime import datetime


# Observer Interface (Abstract Base Class)
class Observer(ABC):
    """
    Abstract Observer class that defines the update interface.
    All concrete observers must implement this method.
    """
    
    @abstractmethod
    def update(self, video_title: str, channel_name: str) -> None:
        """
        Called by Subject when state changes.
        
        Args:
            video_title: Title of the new video
            channel_name: Name of the channel that posted
        """
        pass


# Subject Interface
class Subject(ABC):
    """
    Abstract Subject class that manages observers.
    Provides methods to attach, detach, and notify observers.
    """
    
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Add an observer to the subscription list."""
        pass
    
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Remove an observer from the subscription list."""
        pass
    
    @abstractmethod
    def notify(self) -> None:
        """Notify all observers about state change."""
        pass


# Concrete Subject
class YouTubeChannel(Subject):
    """
    Concrete Subject - represents a YouTube channel.
    Maintains list of subscribers and notifies them when new video is uploaded.
    """
    
    def __init__(self, channel_name: str):
        """
        Initialize YouTube channel.
        
        Args:
            channel_name: Name of the channel
        """
        self._channel_name: str = channel_name
        self._subscribers: List[Observer] = []
        self._latest_video: str = ""
    
    def attach(self, observer: Observer) -> None:
        """
        Subscribe a user to the channel.
        
        Args:
            observer: Subscriber to add
        """
        if observer not in self._subscribers:
            self._subscribers.append(observer)
            print(f"✓ {observer} subscribed to {self._channel_name}")
    
    def detach(self, observer: Observer) -> None:
        """
        Unsubscribe a user from the channel.
        
        Args:
            observer: Subscriber to remove
        """
        if observer in self._subscribers:
            self._subscribers.remove(observer)
            print(f"✗ {observer} unsubscribed from {self._channel_name}")
    
    def notify(self) -> None:
        """
        Notify all subscribers about the new video.
        This is the core of Observer pattern.
        """
        print(f"\n🔔 Notifying {len(self._subscribers)} subscribers...")
        for subscriber in self._subscribers:
            subscriber.update(self._latest_video, self._channel_name)
    
    def upload_video(self, video_title: str) -> None:
        """
        Upload new video - triggers notification to all subscribers.
        
        Args:
            video_title: Title of the uploaded video
        """
        print(f"\n📹 {self._channel_name} uploaded: '{video_title}'")
        self._latest_video = video_title
        self.notify()
    
    @property
    def channel_name(self) -> str:
        """Get channel name."""
        return self._channel_name


# Concrete Observer 1
class EmailSubscriber(Observer):
    """
    Concrete Observer - receives email notifications.
    """
    
    def __init__(self, email: str):
        """
        Initialize email subscriber.
        
        Args:
            email: Email address of the subscriber
        """
        self._email: str = email
    
    def update(self, video_title: str, channel_name: str) -> None:
        """
        Receive notification and send email.
        
        Args:
            video_title: Title of the new video
            channel_name: Name of the channel
        """
        print(f"📧 Email sent to {self._email}:")
        print(f"   '{channel_name}' uploaded '{video_title}'")
    
    def __str__(self) -> str:
        return f"EmailSubscriber({self._email})"


# Concrete Observer 2
class MobileAppSubscriber(Observer):
    """
    Concrete Observer - receives push notifications on mobile app.
    """
    
    def __init__(self, username: str):
        """
        Initialize mobile app subscriber.
        
        Args:
            username: Username of the subscriber
        """
        self._username: str = username
    
    def update(self, video_title: str, channel_name: str) -> None:
        """
        Receive notification and show push notification.
        
        Args:
            video_title: Title of the new video
            channel_name: Name of the channel
        """
        print(f"📱 Push notification to @{self._username}:")
        print(f"   New video from {channel_name}: '{video_title}'")
    
    def __str__(self) -> str:
        return f"MobileAppSubscriber(@{self._username})"


# Concrete Observer 3
class SMSSubscriber(Observer):
    """
    Concrete Observer - receives SMS notifications.
    """
    
    def __init__(self, phone_number: str):
        """
        Initialize SMS subscriber.
        
        Args:
            phone_number: Phone number of the subscriber
        """
        self._phone_number: str = phone_number
    
    def update(self, video_title: str, channel_name: str) -> None:
        """
        Receive notification and send SMS.
        
        Args:
            video_title: Title of the new video
            channel_name: Name of the channel
        """
        print(f"💬 SMS to {self._phone_number}:")
        print(f"   {channel_name}: '{video_title}'")
    
    def __str__(self) -> str:
        return f"SMSSubscriber({self._phone_number})"


# Demo Application
def main():
    """
    Demonstration of Observer Pattern implementation.
    Shows how the pattern enables loose coupling between Subject and Observers.
    """
    
    print("=" * 60)
    print("OBSERVER PATTERN DEMO - YouTube Notification System")
    print("=" * 60)
    
    # Create Subject (YouTube Channel)
    tech_channel = YouTubeChannel("TechMaster")
    
    # Create Observers (Subscribers)
    subscriber1 = EmailSubscriber("alice@example.com")
    subscriber2 = MobileAppSubscriber("bob_dev")
    subscriber3 = SMSSubscriber("+7-777-123-4567")
    
    print("\n--- Subscribing Users ---")
    # Attach observers to subject
    tech_channel.attach(subscriber1)
    tech_channel.attach(subscriber2)
    tech_channel.attach(subscriber3)
    
    # Upload first video - all subscribers get notified
    tech_channel.upload_video("Python Design Patterns Tutorial")
    
    print("\n--- Unsubscribing One User ---")
    # One subscriber unsubscribes
    tech_channel.detach(subscriber2)
    
    # Upload second video - only remaining subscribers get notified
    tech_channel.upload_video("Advanced Observer Pattern Explained")
    
    print("\n--- Adding New Subscriber ---")
    # New subscriber joins
    subscriber4 = EmailSubscriber("charlie@example.com")
    tech_channel.attach(subscriber4)
    
    # Upload third video
    tech_channel.upload_video("Clean Code Principles in Python")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
