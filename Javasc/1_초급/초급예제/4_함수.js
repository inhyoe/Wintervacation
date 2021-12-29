function process(game1){
    if (game1 == true) {
        alert("좋습니다. 게임을 시작합니다.");
    } else {
        alert("네, 나중에 하시죠.");
    }
}

var game = confirm("게임 한판 하실래요?"); // confirm을 써서 true // false를 사용했다.
process(game);