function solution(n)
{
    var answer = 0;

    answer = n.toString().split('').reduce((a,b) => a + Number(b) ,0);

    return answer;
}