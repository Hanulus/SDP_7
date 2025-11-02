"""
Concrete Subject implementation - YouTubeChannel.
Manages subscribers and notifies them when new video is uploaded.
"""

from typing import List
from .interfaces import Subject, Observer


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
