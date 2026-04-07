public class Solution {
    public bool IsValid(string s) {
        Stack<char> stack = new Stack<char>();

        foreach(char c in s)
        {
            // Push opening brackets
            if(c == '(' || c == '{' || c == '[')
            {
                stack.Push(c);
            }
            else
            {
                // If stack empty then invalid
                if(stack.Count == 0) return false;

                char top = stack.Pop();

                // Check matching
                if( (c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[') )
                {
                    return false;
                }
            }
        }

        // Stack should be empty at end
        return stack.Count == 0;
    }
}