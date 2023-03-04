import java.io.*;
import java.util.*;

class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class B7576_1 {
    //토마토토토토
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st1 = new StringTokenizer(br.readLine());

        int M = Integer.parseInt(st1.nextToken());
        int N = Integer.parseInt(st1.nextToken());

        int[][] box = new int[N][M];


        for (int i = 0; i < N; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                box[i][j] = Integer.parseInt(st2.nextToken());
            }
        }

        BFS(box, N, M);

    }

    public static void BFS(int[][] box, int N, int M) {
        Queue<Point> q = new LinkedList<>();

        //1. 토마토가 익은 점들을 큐에 넣어준다.
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (box[i][j] == 1) {
                    q.add(new Point(i, j));
                }
            }
        }

        //큐가 빌때까지 계속
        while (!q.isEmpty()) {
            // 익은 토마토 상하좌우를 탐색하며 익지 않은 토마토가 있으면 그 위치를 큐에 넣어준다.
            Point p = q.poll();
            for (int i = 0; i < 4; i++) {
                int nextX = p.x + dx[i]; //방향대로
                int nextY = p.y + dy[i];

                //범위 밖 패스
                if (nextX < 0 || nextY < 0 || nextX >= N || nextY >= M) {
                    continue;
                }
                //다음 위치가 익지 않은 토마토가 아니면 패스
                if (box[nextX][nextY] != 0) { //-1이거나 1
                    continue;
                }
                box[nextX][nextY] = box[p.x][p.y] + 1;
                q.add(new Point(nextX, nextY));

            }
            //print(box, N, M); //확인용

        }
        //전체 토마토들을 탐색하여  익지않은 토마토(0 값) 하나라도 있으면 -1를 출력한다.
        //그 외는 최대 일수를 출력한다.
        int max = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (box[i][j] == 0) {
                    System.out.println(-1);
                    return;
                } else if (box[i][j] >= max) max = box[i][j];
            }
        }
        System.out.println(max - 1);
    }

    public static void print(int[][] box, int N, int M) {
        //box 출력
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(box[i][j] + " ");
            }
            System.out.println();
        }
    }
}
