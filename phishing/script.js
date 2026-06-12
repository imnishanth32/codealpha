let score = 0;

function checkAnswer(button, correct) {
    if (correct) {
        score++;
        button.style.backgroundColor = "green";
    } else {
        button.style.backgroundColor = "red";
    }

    document.getElementById("result").innerText = 
        "Score: " + score;
}
