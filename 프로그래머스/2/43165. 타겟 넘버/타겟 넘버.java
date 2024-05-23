public class Solution {

    // 주어진 numbers 배열과 target 값을 사용하여 target을 만들 수 있는 경우의 수를 계산하는 메서드
    public int solution(int[] numbers, int target) {
        // 재귀적으로 깊이 우선 탐색(DFS)를 시작합니다. 초기 인덱스는 0, 초기 합은 0으로 설정합니다.
        return dfs(numbers, target, 0, 0);
    }

    // 깊이 우선 탐색(DFS)을 수행하는 재귀 메서드
    // numbers: 사용할 숫자 배열
    // target: 목표 숫자
    // index: 현재 탐색 중인 numbers 배열의 인덱스
    // sum: 현재까지의 합계
    private int dfs(int[] numbers, int target, int index, int sum) {
        // 기저 사례: 배열의 끝에 도달한 경우
        if (index == numbers.length) {
            // 현재까지의 합이 목표 숫자와 같다면 1을 반환 (경우의 수를 의미)
            return sum == target ? 1 : 0;
        }

        // 현재 인덱스에서 숫자를 더하거나 뺀 두 가지 경우를 모두 탐색
        int count = 0;
        // 현재 숫자를 더하는 경우
        count += dfs(numbers, target, index + 1, sum + numbers[index]);
        // 현재 숫자를 빼는 경우
        count += dfs(numbers, target, index + 1, sum - numbers[index]);

        // 두 가지 경우의 수를 합산하여 반환
        return count;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] numbers = {1, 1, 1, 1, 1};
        int target = 3;
        System.out.println(sol.solution(numbers, target));  // 결과: 5
    }
}
