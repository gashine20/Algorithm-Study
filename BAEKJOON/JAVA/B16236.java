import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;



public class B16236 {
    //아기상어
    public static int checkdist(int[][] aquarium, int x, int y, int bx, int by, int level){
        //최단거리를 리턴해주는
        //큰 물고기 있으면 안됨
        //어떤걸 우선순위로 줄건지............. zzz
        int move =0;
        while(bx!=x && by!=y) {
            if (x == bx) { //같은 - 줄에 있음
                if (y - by > 0) { //오른쪽에 있음
                    if (aquarium[bx][by + 1] > level) return -1;
                    else if (aquarium[bx][by + 1] <= level){ //지나가도 돼
                        by+=1;
                        move++;
                    }
                }
                else if (y - by < 0) { //왼쪽에 있음
                    if (aquarium[bx][by - 1] > level) return -1;
                    else if (aquarium[bx][by - 1] <= level){ //지나가도 돼
                        by-=1;
                        move++;
                    }
                }
            }
            else if (y == by) { //같은 | 줄에 있음
                if (x - bx > 0) { //아래에 있음
                    if (aquarium[bx+1][by] > level) return -1;
                    else if (aquarium[bx+1][by] <= level){ //지나가도 돼
                        bx+=1;
                        move++;
                    }
                }
                else if (x - bx < 0) { //위에 있음
                    if (aquarium[bx-1][by] > level) return -1;
                    else if (aquarium[bx-1][by] <= level){ //지나가도 돼
                        bx-=1;
                        move++;
                    }
                }
            }
            else if (x - bx > 0) { //아래에 있음
                if (y - by > 0) { //오른쪽에 있음

                }
            }

        }
        return move;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] aquarium = new int[N][N];

        int bx=-1,by=-1; //아기 상어 좌표

        for(int i=0;i<N;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++){
                aquarium[i][j] = Integer.parseInt(st.nextToken());
                if(aquarium[i][j]==9){
                    bx=i;by=j;
                }
            }

        }

        int move=0; //움직임
        int level =2;
        int eat =0; // 레벨이 바뀔 때마다 0으로 바꿔
        int[][] can = new int[N*N][2];
        for(int i=0;i<can.length;i++){ //-1로 초기화
            can[i][0] =-1;
            can[i][1] =-1;
        }

        //아기 상어 : 9 , 레벨 2부터 시작
        while(true){
            System.out.println("아기상어 level은 " + level);
            System.out.println("아기상어 위치는 " + "("+bx+","+by+")");
            //아기상어 level보다 작은 물고기 위치 저장
            int k=0;
            int count=-1;
            for(int i=0;i<can.length;i++){ //can 배열 -1로 초기화
                can[i][0] =-1;
                can[i][1] =-1;
            }
            for(int i=0;i<N;i++){
                for(int j=0;j<N;j++){
                    if(aquarium[i][j]<level && aquarium[i][j]!=0){ //아기상어 level보다 작은 물고기
                        System.out.println("("+i+","+j+")");
                        can[k][0] = i;
                        can[k][1] = j;
                        k++;
                        count++;
                    }
                }
            }

            if(count==-1) break; //아기상어 level보다 낮은 level 물고기 없음

            //아기상어와 자리 비교 후 정렬
            Map<Integer,Integer> dist = new HashMap<>();
            for(int i=0;i<can.length;i++){
                if(can[i][0] ==-1 && can[i][1] ==-1)break; //물고기 없는 경우
                //가는 길 계산 !
                int len =checkdist(aquarium,can[i][0],can[i][1],bx,by,level);
                if(len!=-1){
                    System.out.println("len = " + len);
                    dist.put(i,len); // (0,2) (1,2) i가 can의 x좌표
                }

//                int x_len = can[i][0]-bx;
//                int y_len = can[i][1]-by;
//                int len  = Math.abs(x_len) + Math.abs(y_len); //길이
//                System.out.println("len = " + len);
//                dist.put(i,len); // (0,2) (1,2) i가 can의 x좌표
            }

            //잡아먹을 수 있는 물고기가 있어도 갈 수 있는 방법이 없으면
            if(dist.isEmpty()) break;
            //key값으로 정렬
            if(!dist.isEmpty()){
                List<Integer> keylist = new ArrayList<>(dist.keySet());
                keylist.sort((o1,o2)->dist.get(o1)-dist.get(o2));

                //Map 출력
                for(int xx: keylist){
                    System.out.println("key: " + xx + ", value: " + dist.get(xx));
                }

                //움직임
                move += dist.get(keylist.get(0)); //움직인 거리
                System.out.println("move = "+ move);
                int xx = can[keylist.get(0)][0]; //물고기 좌표 x
                int yy = can[keylist.get(0)][1]; //물고기 좌표 y
                System.out.println("잡아먹을 물고기 위치는 " + "("+xx+","+yy+")");
                aquarium[bx][by] =0; //아기 상어가 있었던 곳 9로
                aquarium[xx][yy] =9; //물고기 잡은 곳에 아기상어 있다
                bx = xx; //아기상어 위치 바꿔주ㅁ
                by = yy;
                eat +=1;
                count=-1; //카운트 초기화
                if(eat == level){
                    level++; //level up
                    eat=0; //다시 0으로 초기화
                }
            }



        }
        System.out.println("move = "+ move);


    }

}
