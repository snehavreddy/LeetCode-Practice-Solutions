class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert knowledge to a dictionary for O(1) lookups
        knowledge_dict = {k: v for k, v in knowledge}
        
        result = []
        current_key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key_str = "".join(current_key)
                # Append the known value or "?" if not found
                result.append(knowledge_dict.get(key_str, "?"))
                # Reset the key buffer
                current_key = []
            elif in_bracket:
                current_key.append(char)
            else:
                result.append(char)
                
        return "".join(result)