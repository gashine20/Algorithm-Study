import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class B2477 {
    //기하1 - 참외밭
    //(가로 max * 세로 max) - (가로 min * 세로 min) .. 틀림

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int K = Integer.parseInt(br.readLine()); //1m^2에 자라는 참외 수

        int wmax, wmin, hmax, hmin;
        int area;
        int last =-1; //앞에꺼 저장
        ArrayList<Integer> width = new ArrayList<Integer>();
        ArrayList<Integer> height = new ArrayList<Integer>();


        for (int i = 0; i < 6; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int direct = Integer.parseInt(st.nextToken()); //방향
            // 1:동쪽, 2:서쪽, 3:남쪽, 4:북쪽
            int len = Integer.parseInt(st.nextToken()); //최대 최소

            if(direct ==1 || direct == 2){ //가로
                if(last == direct) {
                    int end = width.get(width.size()-1); //끝에 있는 값 가지고 와서
                    width.remove(width.size()-1);
                    width.add(end+len); //더한 값
                }
                else{
                    width.add(len);
                }
                last = direct;
            }
            else if(direct == 3 || direct == 4){ //세로
                if(last == direct) {
                    int end = height.get(height.size()-1); //끝에 있는 값 가지고 와서
                    //System.out.println("end= " + end);
                    height.remove(height.size()-1);
                    height.add(end+len); //더한 값
                }
                else{
                    height.add(len);
                }
                last = direct;
            }
        }
        
        //내림차순 - 최대
        Collections.sort(width, Collections.reverseOrder());
        wmax = width.get(0);
        Collections.sort(height, Collections.reverseOrder());
        hmax = height.get(0);

        //오름차순 - 최소
        Collections.sort(width);
        wmin = width.get(0);
        Collections.sort(height);
        hmin = height.get(0);

        if (wmax == wmin || hmax == hmin)
            area = wmax * hmax * K;
        else
            area = ((wmax * hmax) - (wmin * hmin)) * K;
        System.out.println(area);
    }
}
