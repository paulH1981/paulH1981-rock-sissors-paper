function play(userChoice) {
    fetch('/play', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ choice: userChoice })
    })
    .then(response => response.json())
    .then(data => {
        let resultColor;
        switch(data.result) {
            case 'You lose!':
                resultColor = 'red';
                break;
            case 'It\'s a tie!':
                resultColor = 'black';
                break;
            case 'You win!':
                resultColor = 'green';
                break;
            default:
                resultColor = 'black';
        }
        document.getElementById('result').innerHTML = `You chose: <b>${data.user_choice}</b> &nbsp;&nbsp;&nbsp; Computer chose: <b>${data.computer_choice}</b> &nbsp;&nbsp;&nbsp; Result: <b style="color: ${resultColor};">${data.result}</b>`;
    });
}
