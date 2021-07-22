function solution(n) {
    var answer = '';
    let i = 0;
    if(n === 1){
        return answer ="수";
    }
    while(i++ < Math.floor(n/2)){
        answer += "수박";
    }
    if(n%2 === 1){
        answer += "수";
    }else{
        answer;
    }   
    
    return answer;
}