import java.util.Stack;

class Solution {
    public boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        
        // 문자열을 순회하면서 괄호를 확인
        for (char c : s.toCharArray()) {
            // 열린 괄호일 경우 스택에 추가
            if (c == '(') {
                stack.push(c);
            } else { // 닫힌 괄호일 경우
                // 스택이 비어있거나 괄호의 짝이 맞지 않을 경우 false 반환
                if (stack.isEmpty() || stack.peek() != '(') {
                    return false;
                }
                stack.pop(); // 스택에서 열린 괄호 제거
            }
        }
        
        // 모든 문자열을 확인한 후 스택이 비어있으면 올바른 괄호
        return stack.isEmpty();
    }
}
