import java.io.*;
import java.util.*;

public class B1764 {
    //집합과 맵
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine()); //띄어쓰기
        int notlistenCount = Integer.parseInt(st.nextToken());
        int notlookCount = Integer.parseInt(st.nextToken());

        HashSet<String> notlisten = new HashSet<String>();
        HashSet<String> notlook = new HashSet<String>();

        for(int i=0;i<notlistenCount;i++){
            notlisten.add(br.readLine());
        }

        for(int j=0;j<notlookCount;j++){
            notlook.add(br.readLine());
        }

        notlisten.retainAll(notlook); //교집합

        //개수
        System.out.println(notlisten.size());

        //set -> list화
        List notlistenList = new ArrayList(notlisten);
        Collections.sort(notlistenList);
        //사전순으로
        for(Object n :notlistenList) System.out.println(n);

    }
}
