
window.onload = function() {
  var nextBtn = document.getElementById("next-btn")
  var backBtn = document.querySelector("#back-btn")
  var returnToOverviewBtn = document.querySelector("#return_to_overview_btn")

  nextBtn.addEventListener("click", function() {
    alert("next Q")
    // checkForPriorAnswerSelection()
    // console.log("answerHasBeenSelected: ", answerHasBeenSelected)
    // if (answerHasBeenSelected) {
    //   saveAnswer(Number(currentQuestionNum) - 1);
    // }
    // nextQuestionNumber = Number(currentQuestionNum) + 1
    // console.log("numQuestions: ", numQuestions)
    // if (nextQuestionNumber > numQuestions) {
    //   nextQuestionNumber = 1;
    // }
    // console.log("nextQuestionNumber: ", nextQuestionNumber)
    // getQuestion(nextQuestionNumber)
  })

  backBtn.addEventListener("click", function() {
    alert("last Q")
    // checkForPriorAnswerSelection()
    // nextQuestionNumber = Number(currentQuestionNum) - 1
    // if (nextQuestionNumber == 0) {
    //   nextQuestionNumber = numQuestions;
    // }
    // console.log("nextQuestionNumber: ", nextQuestionNumber)
    // getQuestion(nextQuestionNumber)
  })
}
