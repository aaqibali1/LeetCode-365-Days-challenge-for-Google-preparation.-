class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_codes = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]
        transformations = set()
        for word in words:
            morse_word = ''.join(morse_codes[ord(char) - ord('a')] 
            for char in word)
            transformations.add(morse_word)
        return len(transformations)
