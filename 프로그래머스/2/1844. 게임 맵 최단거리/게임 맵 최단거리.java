import java.util.LinkedList;
import java.util.Queue;

public class Solution {
    // 4가지 방향을 위한 배열 선언 (상, 하, 좌, 우)
    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        // BFS를 위한 큐 선언 및 초기 위치 삽입
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0});
        
        // 방문 여부를 체크하기 위한 배열 선언
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;
        
        // 시작 위치의 거리는 1로 설정
        int distance = 1;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            
            // 현재 큐에 있는 모든 위치에 대해 탐색
            for (int i = 0; i < size; i++) {
                int[] current = queue.poll();
                int x = current[0];
                int y = current[1];
                
                // 목적지에 도달했을 경우 거리 반환
                if (x == n - 1 && y == m - 1) {
                    return distance;
                }
                
                // 4가지 방향으로 이동하면서 유효한 위치를 큐에 삽입
                for (int j = 0; j < 4; j++) {
                    int nx = x + dx[j];
                    int ny = y + dy[j];
                    
                    // 이동한 위치가 맵 내부이고, 벽이 아니며, 방문하지 않은 경우
                    if (nx >= 0 && ny >= 0 && nx < n && ny < m && maps[nx][ny] == 1 && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        queue.add(new int[]{nx, ny});
                    }
                }
            }
            // 이동 거리를 증가
            distance++;
        }
        
        // 목적지에 도달할 수 없을 경우 -1 반환
        return -1;
    }
}
