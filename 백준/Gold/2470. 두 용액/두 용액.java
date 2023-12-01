import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

import static java.lang.Math.abs;
import static java.lang.Math.min;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int minValue = Integer.MAX_VALUE;

        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        int s = 0;
        int e = N-1;

        int ans_s = 0;
        int ans_e = 0;

        while (s < e){
            if (minValue > abs(arr[s] + arr[e])){
                minValue = abs(arr[s] + arr[e]);
                ans_s = s;
                ans_e = e;
            }

            if (arr[s] + arr[e] < 0){
                s++;
            } else if (arr[s] + arr[e] > 0) {
                e--;
            }
            else{
                ans_s = s;
                ans_e = e;
                break;
            }
        }
        System.out.println(arr[ans_s] + " " + arr[ans_e]);
    }
}