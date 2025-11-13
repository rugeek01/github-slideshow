#!/usr/bin/env python3

"""Simple command line chatbot."""

def main():
    response = input("How was your day? ")
    positive_keywords = ["good", "great", "fantastic", "well", "awesome", "nice", "amazing", "wonderful"]
    negative_keywords = ["bad", "terrible", "awful", "horrible", "sad", "not good", "rough", "hard"]
    response_lower = response.lower()
    if any(word in response_lower for word in positive_keywords):
        print("That's wonderful to hear! I'm glad you had a good day.")
    elif any(word in response_lower for word in negative_keywords):
        print("I'm sorry to hear that. I hope tomorrow is better for you.")
    else:
        print("Thanks for sharing. I hope the rest of your day goes well!")

if __name__ == "__main__":
    main()
