"""
Demo application for Observer Pattern.
Shows YouTube Channel notification system in action.
"""

from observer import (
    YouTubeChannel,
    EmailSubscriber,
    MobileAppSubscriber,
    SMSSubscriber
)


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
