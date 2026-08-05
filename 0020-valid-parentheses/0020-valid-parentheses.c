bool isValid(char* s) {
        char stack[strlen(s)];
    int top = -1;

    for (int i = 0; s[i] != '\0'; i++) {
        char ch = s[i];

        // If opening bracket, push to stack
        if (ch == '(' || ch == '{' || ch == '[') {
            stack[++top] = ch;
        } 
        else {
            // If stack is empty when closing bracket appears
            if (top == -1) return false;

            char topChar = stack[top--];
            if ((ch == ')' && topChar != '(') ||
                (ch == '}' && topChar != '{') ||
                (ch == ']' && topChar != '[')) {
                return false;
            }
        }
    }
    // Stack must be empty for a valid string
    return top == -1;


}