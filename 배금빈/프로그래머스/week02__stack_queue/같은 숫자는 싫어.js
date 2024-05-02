// 1. 같은 숫자는 싫어

function solution(arr) {
  let answer = [];
  for (let num of arr) {
    // answer가 비어있거나 또는 현재 숫자가 answer의 마지막 숫자와 다르면 배열 끝에 요소 추가
    if (answer.length === 0 || num !== answer[answer.length - 1]) {
      answer.push(num);
    }
  }
  return answer;
}

// 예시 입력에 대한 테스트
console.log(solution([1, 1, 3, 3, 0, 1, 1])); // [1, 3, 0, 1]
console.log(solution([4, 4, 4, 3, 3])); // [4, 3]

// 2. 다른 풀이
function solutions(arr) {
  // filter 메서드: 주어진 함수의 조건을 만족하는 모든 요소를 가진 새로운 배열을 생성
  // filter 메서드의 콜백 함수는 2개의 인수를 받음
  // 1번째 인수: 배열의 현재 요소
  // 2번째 인수(선택): 해당 요소의 인덱스
  return arr.filter((val, index) => val != arr[index + 1]);
}

// 예시 입력에 대한 테스트
console.log(solutions([1, 1, 3, 3, 0, 1, 1])); // [1, 3, 0, 1]
console.log(solutions([4, 4, 4, 3, 3])); // [4, 3]
