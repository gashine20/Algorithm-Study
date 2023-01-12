import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.StringTokenizer;

public class B1269 {
    //대칭 차집합
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashSet<String> A = new HashSet<>();
        HashSet<String> A2 = new HashSet<>(); //A 복제
        HashSet<String> B = new HashSet<>();

        StringTokenizer s1 = new StringTokenizer(br.readLine());
        StringTokenizer s2 = new StringTokenizer(br.readLine());

        for(int i=0;i<N;i++)
            A.add(s1.nextToken());
        for(int i=0;i<M;i++)
            B.add(s2.nextToken());

        for(String s : A) A2.add(s);

        //A-B => A = {1}
        A.removeAll(B);
        //B-A => B = {3,5,6}
        B.removeAll(A2);
        //A-B 합집합 B-A
        A.addAll(B);

        //출력
//        List AB = new ArrayList(A);
//        for(Object n : AB) System.out.println(n + " ");
        System.out.println(A.size());

    }
}
