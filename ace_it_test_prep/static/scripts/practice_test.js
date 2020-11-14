import { clock_minutes } from "./timer.js"
import { clock_seconds } from "./timer.js"
var userAnswerSelections;
var eliminatedAnswerOptionsList;
var currentQuestionIndex;
var answerHasBeenSelected;
var numQuestions;
var test_session_id;
var isInitialSetup;
var passageDiv;
var timeSpentOnQuestions = {};
var submitSectionBtn = document.querySelector("#submit-section-btn");
var nextBtn, backBtn, question_id, nextQuestionIndex, nextQuestion, answers_divs;

 function getCookie(cname) {
   console.log("GET COOKIE")
      var name = cname + "=";
      var decodedCookie = decodeURIComponent(document.cookie);
      var ca = decodedCookie.split(';');
      for(var i = 0; i <ca.length; i++) {
          var c = ca[i];
          while (c.charAt(0) == ' ') {
              c = c.substring(1);
          }
          if (c.indexOf(name) == 0) {
              return c.substring(name.length, c.length);
          }
      }
      return "";
  }

  submitSectionBtn.addEventListener("click", () => {
    checkForNewAnswerSelection(currentQuestionIndex)
      saveEliminatedOptions(currentQuestionIndex);
      if (answerHasBeenSelected) {
        userAnswerSelections[currentQuestionIndex] = document.querySelector(".selected_answer").id
        saveAnswer(currentQuestionIndex);
      }
  })

  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']]
    },
    svg: {
      fontCache: 'global'
    }
  };

  (function () {
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js';
    script.async = true;
    document.head.appendChild(script);
  })();

  function setupPage() {
    console.log("SETUP")

    // ----------- VARIABLE ASSIGNMENT -----------------

    isInitialSetup = true;

    // var pauseSession = document.querySelector("#pause-session");

    // test and session meta data
    var testId = document.getElementById("test_id");
    var test_section = document.getElementById("section");
    // var sessionId = document.querySelector("#session_id");
    test_session_id = document.querySelector("#test_session_id").value

    // question metadata
    // var questionNums = document.getElementById("question-nums");
    numQuestions = Number(document.querySelector("#question_nums").value)
    question_id = Number(document.querySelector("#question_id").value)
    var questionNumber = 1;
    currentQuestionIndex = 0;

    // next, back, and submit direction buttons - bottom of page
    nextBtn = document.getElementById("next-btn");
    backBtn = document.getElementById("back-btn");
    var submit_test = document.querySelector("#submit_test");

    // question number, text, and answers
    var num = document.getElementById("num");
    var questionDiv = document.getElementById("question");
    // var answers_divs = document.querySelectorAll(".answer_choice")
    

    // not used for SSAT (quantitative comparisons)
    // var columnA = document.getElementById("option_column_a");
    // var columnB = document.getElementById("option_column_b");

    // initialize array of length of number of questions.
    // each index contains an array of length of answers options each of which is set to 'false'.
    // this is used to monitor options user has 'eliminated' for each question
    
    // eliminatedListInitialSingle = [false, false, false, false, false]
    eliminatedAnswerOptionsList = []

    console.log("NUM QUESTIONS: ", numQuestions)

    for (i = 0; i < numQuestions; i++) {
      timeSpentOnQuestions[i + 1] = [{
        "start_time": null,
        "end_time": null
      }]
      eliminatedAnswerOptionsList[i] = new Array(false, false, false, false, false)
      // eliminatedListInitialSingle.forEach(function(el, index) {
      //   eliminatedAnswerOptionsList[i][index] = el
      // })
    }
    timeSpentOnQuestions[1][0]["start_time"] = "30:00"

    // var eliminateOptionBtnGroup = Array.from(document.querySelectorAll(".eliminate_option_btn"))
    userAnswerSelections = Array.from({length: numQuestions})
    answerHasBeenSelected = false;

    // set first pagination button to active
    var paginationBtns = Array.from(document.querySelectorAll(".page-item"))

    


    // setEliminatedAnswers(eliminateOptionBtnGroup, answers_divs)
    setEliminatedAnswers()
    resetPaginationBtns(currentQuestionIndex)
    // getQuestions();
    console.log("userAnswerSelections5: ", userAnswerSelections)
    setQuestionNumBtns()
    // activateAnswerBtns(answers_divs)
    activateAnswerBtns()
    activateDirectionalBtns()
    // activateDirectionalBtns(currentQuestionIndex, answerHasBeenSelected, numQuestions, userAnswerSelections)
    reset()

    var questions = "QUESTIONS";
    var currentQuestionNum = 1;
    // var currentQuestionIndex = 0;
    var answer_options_container = document.querySelector(".answer_options_container");
    // var userAnswerSelections;
    
    var answerSelectionIsNew = false;
    var testHasBeenLoaded = false;
    var question_data;
    var passages;
    var passageDiv;
  
    var test_id;
    var question_id;
    var test_session;
    var section;
    var context;
    var answerSelection;
    var currentAnswerSelection;
    var answerSelectionHasChanged = false;
    var timeExpired = false;
    var paginationBtns;
    
    isInitialSetup = false;
  }

  // function setEliminatedAnswers(eliminateOptionBtnGroup, answers_divs){
  function setEliminatedAnswers(){
    answers_divs = document.querySelectorAll(".answer_choice")
    var eliminateOptionBtnGroup = Array.from(document.querySelectorAll(".eliminate_option_btn"))
    
    eliminateOptionBtnGroup.forEach(function(el, index) {
      el.addEventListener("click", function() {
        if (answers_divs[index].classList.contains("eliminated")) {
          answers_divs[index].classList.remove("eliminated")
        } else {
          answers_divs[index].classList.add("eliminated")
        }
      })
    })
  }

  function resetPaginationBtns(currentQuestionIndex) {
    var paginationBtns = Array.from(document.querySelectorAll(".page-item"))
    paginationBtns.forEach(function(el){
      el.classList.remove("active")
    })
    paginationBtns[currentQuestionIndex].classList.add("active")
  }


  function setReadingPassage(passage_index) {
    passageDiv.innerHTML = passages[passage_index]['text']
    console.log("passageDiv: ", passageDiv)
  }

  function setQuestionNumBtns() {
    if (!isInitialSetup) {
      console.log("isInitialSetup: ", isInitialSetup)
      saveAnswer(currentQuestionIndex)
    }
    var questionNumBtns = document.querySelectorAll(".question_num_btn")
    questionNumBtns.forEach((btn, index) => {
      btn.addEventListener("click", function() {
        getNextQuestion(index)
        reset()
      })
    });
  }

  function getNextQuestion(questionIndex) {
    // nextQuestion = data[questionIndex]
    nextQuestion = q_and_a[questionIndex]
    currentQuestionIndex = questionIndex
    setNextQuestion(nextQuestion, currentQuestionIndex, questionIndex)
  }

  function reset() {
    MathJax.texReset();
    MathJax.typesetClear();
    MathJax.typeset();
  }

  function setNextQuestion(nextQuestion, currentQuestionIndex, nextQuestionIndex) {
    var answerOptionsGroup = Array.from(document.querySelectorAll(".eliminate_option_btn"))
    answers_divs = document.querySelectorAll(".answer_choice")
    var eliminatedAnswerOptions = answerOptionsGroup.map(function(el, index) {
      if (answers_divs[index].classList.contains("eliminated")) { return true }
      else { return false }
    })

    // eliminatedAnswerOptionsList[currentQuestionIndex] = eliminatedAnswerOptions

    resetPaginationBtns(nextQuestion.question.number - 1)
    answerHasBeenSelected = false;
    document.querySelector("#question").innerHTML = nextQuestion.question.question_text

    question_id = nextQuestion.question.id
    document.querySelector("#num").innerHTML = nextQuestion.question.number + ". "
    var answersData = nextQuestion.answers

    if (nextQuestion.question.passage) {
      passage_index = nextQuestion.question.passage
      setReadingPassage(passage_index)
    }
    setNextAnswers(answersData, currentQuestionIndex);
    updateTimeSpentOnQuestions(currentQuestionIndex, nextQuestionIndex)
  }

  function setNextAnswers(answersData, currentQuestionIndex) {
    resetAnswerColors(answers_divs)
    answersData.forEach(setAnswerDivs);
    return
  }

  function setAnswerDivs(answer, index) {
    answers_divs[index].innerHTML = String.fromCharCode(65 + index) + ". " + answer.option
    //Possible bug: Does not add fifth choice if previous question had only four choices. Will this be an issue?

    //***Previsouly selected answer needs to be highlighted when answers are loaded***///
    var previousAnswerSelection = userAnswerSelections[currentQuestionIndex]
    if (previousAnswerSelection == answers_divs[index].id) {
      answers_divs[index].classList.add("selected_answer");
    }
   if (eliminatedAnswerOptionsList[currentQuestionIndex][index]) {
      answers_divs[index].classList.add("eliminated")
      // eliminatedAnswerOptionsList[currentQuestionIndex][index] = true
    } else {
      answers_divs[index].classList.remove("eliminated")
      // eliminatedAnswerOptionsList[currentQuestionIndex][index] = false
    }
  }

  window.onload = function () {
    setupPage();
    if (current_section == 'reading') {
      this.console.log("reading")
      passageDiv = document.querySelector("#passage")
      setReadingPassage(passage_index)
    }
  }
  
  // function activateAnswerBtns(answerOptions) {
  function activateAnswerBtns() {
    var answerOptions = document.querySelectorAll(".answer_choice")
    answerOptions.forEach(function(answerOption) {
      answerOption.addEventListener("click", function(e) {
        if (answerOption.classList.contains("selected_answer")) {
          // selectAnswer(e);
          answerOption.classList.remove("selected_answer")
          answerHasBeenSelected = false;
          userAnswerSelections[currentQuestionIndex] = -1
        } else {
          resetAnswerColors(answerOptions);
          // currentAnswerSelection = getCurrentAnswerSelection(questionNumber);
          answerOption.classList.add("selected_answer")
          answerHasBeenSelected = true;
          userAnswerSelections[currentQuestionIndex] = answerOption.id
        }
      })
    });
  }

  function resetAnswerColors(answerOptions) {
    answerOptions.forEach(function(answerOption, i) {
      answerOption.classList.remove("selected_answer");
    });
  }

  function activateDirectionalBtns() {
  // function activateDirectionalBtns(currentQuestionIndex, answerHasBeenSelected, numQuestions, userAnswerSelections) {
    // nextBtn = document.getElementById("next-btn");
    // backBtn = document.getElementById("back-btn");
    nextBtn.addEventListener("click", function() {
      checkForNewAnswerSelection(currentQuestionIndex)
      saveEliminatedOptions(currentQuestionIndex);
      if (answerHasBeenSelected) {
        userAnswerSelections[currentQuestionIndex] = document.querySelector(".selected_answer").id
        saveAnswer(currentQuestionIndex);
      }
      nextQuestionIndex = currentQuestionIndex + 1
      if (nextQuestionIndex == numQuestions) {
        nextQuestionIndex = 0;
      }
      updateTimeSpentOnQuestions(currentQuestionIndex, nextQuestionIndex)
      getNextQuestion(nextQuestionIndex)
      reset();
    })
  
    backBtn.addEventListener("click", function() {
      checkForNewAnswerSelection(currentQuestionIndex)
      saveEliminatedOptions(currentQuestionIndex);
      if (answerHasBeenSelected) {
        saveAnswer(currentQuestionIndex);
      }
      nextQuestionIndex = currentQuestionIndex - 1
      if (nextQuestionIndex == -1) {
        nextQuestionIndex = numQuestions - 1;
      }
      getNextQuestion(nextQuestionIndex)
      updateTimeSpentOnQuestions(currentQuestionIndex, nextQuestionIndex)
      reset();
    })
  }

  function updateTimeSpentOnQuestions(currentQuestionIndex, nextQuestionIndex) {
    var currentQuestionNumber = currentQuestionIndex + 1
    var nextQuestionNumber = nextQuestionIndex + 1
    var currentQuestionIndexLength = timeSpentOnQuestions[currentQuestionNumber].length
    var nextQuestionIndexLength = timeSpentOnQuestions[nextQuestionNumber].length
    timeSpentOnQuestions[currentQuestionNumber][currentQuestionIndexLength - 1].end_time = clock_minutes + ":" + clock_seconds
    timeSpentOnQuestions[nextQuestionNumber][nextQuestionIndexLength - 1].start_time = clock_minutes + ":" + clock_seconds
  }

  function saveEliminatedOptions(currentQuestionIndex) {
    var answers_divs = Array.from(document.querySelectorAll(".answer_choice"))
    answers_divs.forEach(function(el, index) {
      if (el.classList.contains("eliminated")) {
        eliminatedAnswerOptionsList[currentQuestionIndex][index] = true
      } else {
        eliminatedAnswerOptionsList[currentQuestionIndex][index] = false
      }
    })
  }

  function saveAnswer(index) {
    console.log("SAVE ANSWER")
    var xhr = new XMLHttpRequest();
    var csrftoken = getCookie('csrftoken');
    var method = "POST";
    var url = "save_test_response"
    question_id = q_and_a[index]['question']['id']
    var request_data = JSON.stringify({
      "index" : index,
      "response": userAnswerSelections[index],
      "session_id": test_session_id,
      "question_id": question_id
     });

     console.log("request_data: ", request_data)

    xhr.open(method, url);

    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader("X-CSRFToken", csrftoken);

    xhr.send(request_data);

    xhr.onload = function() {

      if (xhr.readyState == 4 && xhr.status == 200) {
        console.log(xhr.response)
      }
    }
  }

  function checkForNewAnswerSelection(currentQuestionIndex) {
    try {
      answerSelection = document.querySelector(".selected_answer").id;
      if (answerSelection) {
        if (answerSelection != userAnswerSelections[currentQuestionIndex]) {
          userAnswerSelections[currentQuestionIndex] = answerSelection
        }
      }
    } catch {
      return
    }
  }

  function saveFinalAnswer() {
    var submitBtn = document.getElementById("submit-section-btn-form");
    console.log("save final answer: ", submitBtn);
    checkForNewAnswerSelection(currentQuestionIndex)
      saveEliminatedOptions(currentQuestionIndex);
      if (answerHasBeenSelected) {
        userAnswerSelections[currentQuestionIndex] = document.querySelector(".selected_answer").id
        saveAnswer(currentQuestionIndex);
      }
    submitBtn.submit();
  }

  export { saveFinalAnswer }