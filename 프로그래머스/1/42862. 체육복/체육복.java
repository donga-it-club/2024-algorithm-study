import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        //여벌 체육복을 가진 학생이 도난당한 경우를 제거
        Set<Integer> actualLost = new HashSet<>();
        Set<Integer> actualReserve = new HashSet<>();
        
        // Initialize actualLost and actualReserve sets
        for (int l : lost) {
            actualLost.add(l);
        }
        for (int r : reserve) {
            if (actualLost.contains(r)) {
                // If a student has lost a uniform but also has a reserve, remove from lost set
                actualLost.remove(r);
            } else {
                actualReserve.add(r);
            }
        }
        
        //체육복을 빌려줄 수 있는지 확인
        for (int r : actualReserve) {
            if (actualLost.contains(r - 1)) {
                actualLost.remove(r - 1); // 앞번호 학생에게 빌려줌
            } else if (actualLost.contains(r + 1)) {
                actualLost.remove(r + 1); // 뒷번호 학생에게 빌려줌
            }
        }
        
        //체육수업을 들을 수 있는 학생 수 계산
        int answer = n - actualLost.size();
        return answer;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(5, new int[]{2, 4}, new int[]{1, 3, 5})); // Should print 5
        System.out.println(sol.solution(5, new int[]{2, 4}, new int[]{3})); // Should print 4
        System.out.println(sol.solution(3, new int[]{3}, new int[]{1})); // Should print 2
    }
}
