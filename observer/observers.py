"""
Concrete Observer implementations.
Different types of subscribers with different notification methods.
"""

from .interfaces import Observer


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
