class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        
        for(int i=left; i<=right; i++) {
            int num = 1;
            for(int j=1; j<=i/2; j++) {
                if(i % j == 0)
                    num++;
            }//for j
            if(num % 2 == 0)
                answer += i;
            else 
                answer -= i;
        }//for i
        return answer;
    }
}