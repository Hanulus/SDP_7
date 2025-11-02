"""
Abstract interfaces for Observer Pattern.
Defines contracts for Subject and Observer.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    Abstract Observer interface.
    All concrete observers must implement the update method.
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


class Subject(ABC):
    """
    Abstract Subject interface.
    Manages observers and notifies them about state changes.
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
