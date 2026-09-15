from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = ""
        for s in strs:
            # Format: <length>#<string>
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        
        while i < len(s):
            # Find the delimiter tracking the end of the length integer
            j = s.find("#", i)
            # Extract the length of the upcoming string
            length = int(s[i:j])
            
            # The actual string starts right after '#'
            start = j + 1
            end = start + length
            
            # Append the extracted substring
            decoded.append(s[start:end])
            
            # Move the pointer to the start of the next encoded block
            i = end
            
        return decoded
