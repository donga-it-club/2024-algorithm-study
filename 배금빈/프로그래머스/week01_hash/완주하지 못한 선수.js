// 완주하지 못한 선수

function solution(participant, completion) {
  const participantMap = new Map();

  // 참가자 목록을 Map에 추가
  // key는 요소, value는 요소가 등장한 횟수
  participant.forEach((name) => {
    if (participantMap.has(name)) {
      participantMap.set(name, participantMap.get(name) + 1);
    } else {
      participantMap.set(name, 1);
    }
  });
  console.log(participantMap);

  // 완주자 목록을 Map에서 빼기
  completion.forEach((name) => {
    if (participantMap.has(name)) {
      participantMap.set(name, participantMap.get(name) - 1);
    }
  });

  // 남은 참가자 찾기
  for (const [name, count] of participantMap.entries()) {
    if (count > 0) {
      console.log(participantMap);
      return name; // 남은 참가자 반환
    }
  }

  return ""; // 만약 남은 참가자가 없다면 빈 문자열 반환
}

const participant = ["mislav", "stanko", "mislav", "ana"];
const completion = ["stanko", "ana", "mislav"];
const answer = solution(participant, completion);
console.log("완주하지 못한 선수:", answer);
