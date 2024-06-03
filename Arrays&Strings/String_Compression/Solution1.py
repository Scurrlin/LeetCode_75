class Solution:
    def compress(self, chars: List[str]) -> int:
        final_str, i = 0, 0

        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            chars[final_str] = letter
            final_str += 1
            if count > 1:
                for c in str(count):
                    chars[final_str] = c
                    final_str += 1

        return final_str