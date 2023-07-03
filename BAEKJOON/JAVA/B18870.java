import java.util.*;
import java.io.*;

public class B18870 {
    //좌표 압축
    //자기보다 작은 개수
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] X = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            X[i] = Integer.parseInt(st.nextToken());
        }

        int[] X2 = X.clone(); //O(n)
        Arrays.sort(X2); //nlogn

        int idx = 0;
        HashMap<Integer,Integer> hmap = new HashMap<>();
        for(int x:X2){ //O(n)
            if(!hmap.containsKey(x)) //O(1)
                hmap.put(x,idx++);
        }

        //O(n^2)
//        for (int i = 0; i < N; i++) {
//            for (int j = 0; j < N; j++) {
//                if (X[i] > X[j])
//                    count[i]++;
//            }
//        }

        StringBuilder sb = new StringBuilder(); //이거까지.... ㅏ

        for (int x :X) {
            sb.append(hmap.get(x) + " ");
        }

        System.out.println(sb.toString());

    }

}
