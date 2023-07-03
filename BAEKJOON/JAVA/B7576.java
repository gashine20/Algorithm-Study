import java.io.*;
import java.util.*;

public class B7576 {
    public static int[][] MakeRipe(int[][] box, int x, int y){
        // box.length = N, box[0].length = M

        if(x-1 >= 0){ //위
            if(box[x-1][y] == 0)
                box[x-1][y] =1; //1로 변경
        }
        if(x+1 < box.length){ //아래
            if(box[x+1][y] == 0)
                box[x+1][y] = 1;
        }
        if(y-1 >= 0){ //왼
            if(box[x][y-1] == 0)
                box[x][y-1] = 1;
        }
        if(y+1 < box[0].length){ //오른쪽
            if(box[x][y+1] == 0)
                box[x][y+1] = 1;
        }

        return box;
    }

    public static int CheckRipe(int[][] box){
        int count =0;
        for(int i=0;i<box.length;i++){
            for(int j=0;j<box[0].length;j++){
                if(box[i][j] ==1 || box[i][j] ==-1) count++;
            }
            //System.out.println();
        }

        if(count == box.length*box[0].length) return 1;
        else return -1;
    }

    public static int CanRipe(int[][] box,int x, int y){
        Boolean cant = true;

        if(x-1 >= 0){ //위
            if(box[x-1][y] == 0) //주변에 0이 있으면
                cant = false;
        }
        if(x+1 < box.length){ //아래
            if(box[x+1][y] == 0)
                cant = false;
        }
        if(y-1 >= 0){ //왼
            if(box[x][y-1] == 0)
                cant = false;
        }
        if(y+1 < box[0].length){ //오른쪽
            if(box[x][y+1] == 0)
                cant = false;
        }

        if(cant == false) return 1; //주변에 0이 있음
        else return 0; //주변에 0 없음

    }


    //토마토
    public static void main(String[] args) throws IOException {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st1 = new StringTokenizer(br.readLine());

        int M = Integer.parseInt(st1.nextToken());
        int N = Integer.parseInt(st1.nextToken());

        int[][] box = new int[N][M];
        int[][] ripe = new int[N*M][2];


        for(int i=0;i<N;i++){
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            for(int j=0;j<M;j++){
                box[i][j] =Integer.parseInt(st2.nextToken());
            }
        }

        if (CheckRipe(box) ==1) System.out.println("0"); //처음부터 다 익었으면

        else {
            int count = 0;
            while (true) {
                //ripe 초기화
                for (int i = 0; i < ripe.length; i++) {
                    ripe[i][0] = -1;
                    ripe[i][1] = -1;
                }

                //익은거 저장
                int idx = 0;
                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < M; j++) {
                        if (box[i][j] == 1) {
                            ripe[idx][0] = i;
                            ripe[idx][1] = j;
                            idx++;
                        }
                    }
                }

                //ripe 출력
//                for (int i = 0; i < ripe.length; i++) {
//                    if (ripe[i][0] != -1 && ripe[i][0] != -1) {
//                        System.out.println("(" + ripe[i][0] + "," + ripe[i][1] + ")");
//                    }
//                }

                int pass=0;
                int cnt=0; //1 개수 세기
                //ripe 1로 만들
                for (int i = 0; i < ripe.length; i++) {
                    if (ripe[i][0] != -1 && ripe[i][1] != -1) {
                        cnt++;
                        if(CanRipe(box, ripe[i][0], ripe[i][1])==1){
                            MakeRipe(box, ripe[i][0], ripe[i][1]);
                        }
                        else{
                            pass++;
                        }
                    }
                }
                if(cnt==pass) {
                    count =-1;
                    break; //더이상 없다
                }

                count++;
                if (CheckRipe(box) == 1) break; // 다 익음

                //box 출력
//                for (int i = 0; i < N; i++) {
//                    for (int j = 0; j < M; j++) {
//                        System.out.print(box[i][j] + " ");
//                    }
//                    System.out.println();
//                }
            }

            System.out.println(count);
        }

    }
}
