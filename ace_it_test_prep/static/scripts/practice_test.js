  var nextBtn = document.getElementById("next-btn");
  var backBtn = document.getElementById("back-btn");
  var num = document.getElementById("num");
  var questionDiv = document.getElementById("question");
  var questionNums = document.getElementById("question-nums");
  var testId = document.getElementById("test_id");
  // var pauseSession = document.querySelector("#pause-session");
  var test_section = document.getElementById("section");
  var columnA = document.getElementById("option_column_a");
  var columnB = document.getElementById("option_column_b");
  var sessionId = document.querySelector("#session_id");
  var submit_test = document.querySelector("#submit_test");

  var numQuestions;
  var questions = "QUESTIONS";
  var currentQuestionNum = 1;
  var currentQuestionIndex = 0;
  var answer_options_container = document.querySelector(".answer_options_container");
  var userAnswerSelections;
  var answerHasBeenSelected = false;
  var answerSelectionIsNew = false;
  var test_session_id;
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


  function getCookie(cname) {
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


  window.onload = function () {
    console.log("BIBUYBGVYCYTFYCYTVYTV")
    test_session_id = document.querySelector("#test_session_id").value
    numQuestions = document.querySelector("#question_nums").value
    answers_divs = document.querySelectorAll(".answer_choice")
    passageDiv = document.querySelector("#passage")
    question_id = document.querySelector("#question_id").value
    console.log("QUESTION_ID: ", question_id)
    questionNumber = 1;
    currentQuestionIndex = 0;
    userAnswerSelections = Array.from({length: numQuestions})
    getQuestions();
    setQuestionNumBtns()
    activateAnswerBtns(answers_divs)
    reset()
  }

  function getQuestions() {
    var xhr = new XMLHttpRequest();
    var csrftoken = getCookie('csrftoken');
    var method = "POST";
    var url = "../../get_questions"
    var section = document.querySelector("#section")
    console.log("section: ", section)

    post_data = JSON.stringify({
      test_session_id: test_session_id,
      section: section.value
    })

    xhr.open(method, url);

    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(post_data);

    xhr.onload = function() {

      if (xhr.readyState == 4 && xhr.status == 200) {
        // console.log("response: ", xhr.response)
        data = JSON.parse(xhr.response)
        question_data = data.data
        // if (!testHasBeenLoaded) {
        //   userAnswerSelections = Array.apply(null, Array(numQuestions)).map(function () {})
        //   testHasBeenLoaded = true
        // }
        console.log("data: ", data)
        passages = JSON.parse(data.passages)
        console.log("passages: ", JSON.parse(passages))
        reset()
      }
    }
  }

  function setQuestionNumBtns() {
    questionNumBtns = document.querySelectorAll(".question_num_btn")
    questionNumBtns.forEach((btn, index) => {
      btn.addEventListener("click", function() {
        getNextQuestion(index)
        reset()
      })
    });
  }

  function getNextQuestion(questionIndex) {
    nextQuestion = question_data[questionIndex]
    currentQuestionIndex = questionIndex
    setNextQuestion(nextQuestion, currentQuestionIndex)
  }

  function setNextQuestion(nextQuestion, currentQuestionIndex) {
    answerHasBeenSelected = false;
    questionDiv.innerHTML = nextQuestion.question.question_text
    question_id = nextQuestion.question.id
    num.innerHTML = nextQuestion.question.number + ". "
    answersData = nextQuestion.answers
    console.log("nextQuestionID****: ", question_id)

    if (nextQuestion.question.passage) {
      console.log("TRUE")
      console.log(passages)
      console.log(passages[0])
      passageDiv.innerHTML = passages[nextQuestion.question.passage - 1]["fields"]["text"]
    }
    setNextAnswers(answersData, currentQuestionIndex);
    console.log("userAnswerSelections: ", userAnswerSelections)
  }

  function setNextAnswers(answersData, currentQuestionIndex) {
    resetAnswerColors(answers_divs)
    answersData.forEach((answer, index) => {
      answers_divs[index].innerHTML = String.fromCharCode(65 + index) + ". " + answer.option
      //Possible bug: Does not add fifth choice if previous question had only four choices. Will this be an issue?

      //***Previsouly selected answer needs to be highlighted when answers are loaded***///
      var previousAnswerSelection = userAnswerSelections[currentQuestionIndex]
      console.log("userAnswerSelections: ", userAnswerSelections)
      console.log("currentQuestionIndex: ", currentQuestionIndex, "previousAnswerSelection: ", previousAnswerSelection)
      console.log("answers_divs[index].id: ", answers_divs[index].id)
      if (previousAnswerSelection == answers_divs[index].id) {
        console.log("TRUE")
        answers_divs[index].classList.add("selected_answer");
      }
    });
    return
  }

  function activateAnswerBtns(answerOptions) {
    answerOptions.forEach(function(answerOption) {
      answerOption.addEventListener("click", function(e) {
        if (answerOption.classList.contains("selected_answer")) {
          console.log("IF")
          // selectAnswer(e);
          answerOption.classList.remove("selected_answer")
          answerHasBeenSelected = false;
          userAnswerSelections[currentQuestionIndex] = -1
        } else {
          console.log("ELSE")
          resetAnswerColors(answerOptions);
          // currentAnswerSelection = getCurrentAnswerSelection(questionNumber);
          answerOption.classList.add("selected_answer")
          answerHasBeenSelected = true;
          console.log("answerHasBeenSelected: ", answerHasBeenSelected)
          userAnswerSelections[currentQuestionIndex] = answerOption.id
        }
      })
      // console.log("userAnswerSelections!!!!: ", userAnswerSelections)
      // console.log("questionNumber - 1!!!!: ", questionNumber - 1)
      // var previousAnswerSelection = userAnswerSelections[questionNumber - 1]
      // if (previousAnswerSelection == answerOption.id) {
      //   console.log("ADD_selected_answer")
      //   answerOption.classList.add("selected_answer");
      // }
    });
  }

  function resetAnswerColors(answerOptions) {
    console.log("RESET COLORS")
    answerOptions.forEach(function(answerOption, i) {
      answerOption.classList.remove("selected_answer");
      console.log("answerOption: ", answerOption)
    });
    console.log("answerOptions: ", answerOptions)
  }

  nextBtn.addEventListener("click", function() {
    checkForNewAnswerSelection(currentQuestionIndex)
    console.log("answerHasBeenSelected: ", answerHasBeenSelected)
    if (answerHasBeenSelected) {
      console.log("SELECTED")
      userAnswerSelections[currentQuestionIndex] = document.querySelector(".selected_answer").id
      saveAnswer(currentQuestionIndex);
    }
    nextQuestionIndex = currentQuestionIndex + 1
    console.log("numQuestions: ", numQuestions)
    console.log("nextQuestionIndex: ", nextQuestionIndex)
    console.log("(nextQuestionIndex == numQuestions - 1): ", (nextQuestionIndex == numQuestions - 1))
    if (nextQuestionIndex == numQuestions) {
      nextQuestionIndex = 0;
    }
    console.log("nextQuestionIndex: ", nextQuestionIndex)
    getNextQuestion(nextQuestionIndex)
    reset();
  })

  backBtn.addEventListener("click", function() {
    checkForNewAnswerSelection(currentQuestionIndex)
    if (answerHasBeenSelected) {
      saveAnswer(Number(currentQuestionNum) - 1);
    }
    nextQuestionIndex = currentQuestionIndex - 1
    if (nextQuestionIndex == -1) {
      nextQuestionIndex = numQuestions - 1;
    }
    console.log("nextQuestionIndex: ", nextQuestionIndex)
    getNextQuestion(nextQuestionIndex)
    reset();
  })

  function saveAnswer(index) {
    var xhr = new XMLHttpRequest();
    var csrftoken = getCookie('csrftoken');
    var method = "POST";
    var url = "save_test_response"
    console.log("SAVEuserAnswerSelections[index]: ", userAnswerSelections[index])
    console.log("SAVEuserAnswerSelections: ", userAnswerSelections)
    console.log("test_session_id: ", test_session_id)
    console.log("URL: ", url)
    // debugger;
    var data = JSON.stringify({
      "index" : index,
      "response": userAnswerSelections[index],
      "session_id": test_session_id,
      "question_id": question_id
     });

     console.log("data: ", data)

    xhr.open(method, url);

    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader("X-CSRFToken", csrftoken);

    xhr.send(data);

    xhr.onload = function() {

      if (xhr.readyState == 4 && xhr.status == 200) {
        console.log(xhr.response)
      }
    }
  }

  function checkForNewAnswerSelection(currentQuestionIndex) {
    console.log("checkForPriorAnswerSelection")
    try {
      answerSelection = document.querySelector(".selected_answer").id;
      if (answerSelection) {
        if (answerSelection != userAnswerSelections[currentQuestionIndex]) {
          userAnswerSelections[currentQuestionIndex] = answerSelection
        }
      }
      console.log("userAnswerSelections: ", userAnswerSelections)
    } catch {
      return
    }

  }







  function setQuestion(question_data, answers_data) {
    if (question.number > numQuestions) {
      questionNumber = 1;
    } else if (question.number == 0) {
      questionNumber = numQuestions;
    }
    currentQuestionNum = question_data.number
    // index = questionNumber - 1;
    questionDiv.innerHTML = question_data.question
    num.innerHTML = currentQuestionNum + ". "
    setAnswers(answers_data);
    reset();
  }



  function setAnswers(answers_data) {
    // questionNumber = question_data.number
    answerHasBeenSelected = false;
    answer_options_container.innerHTML = ""
    // index = questionNumber - 1;
    letter_index = 0;
    console.log(typeof(answers_data))
    // for (answer of answers_data) {
    //   console.log("answer.fields: ", answer)
    //   letter = String.fromCharCode(65 + letter_index)
    //   answer_options_container.innerHTML += "<div id=" + answer.fields.value + " class='answer_choice'>" + letter + ". " + answer.fields.option + "</div>"
    //   letter_index += 1;
    // }

    answerOptions = document.querySelectorAll(".answer_choice");
    answerOptions.forEach(function(answerOption) {
      answerOption.addEventListener("click", function(e) {
        if (answerOption.classList.contains("selected_answer")) {
          // selectAnswer(e);
          answerOption.classList.remove("selected_answer")
          answerHasBeenSelected = false;
          userAnswerSelections[questionNumber - 1] = -1
        } else {
          resetAnswerColors(answerOptions);
          currentAnswerSelection = getCurrentAnswerSelection(questionNumber);
          answerOption.classList.add("selected_answer")
          answerHasBeenSelected = true;
          console.log("answerHasBeenSelected: ", answerHasBeenSelected)
          userAnswerSelections[questionNumber - 1] = answerOption.id
        }
      })
      // var previousAnswerSelection = userAnswerSelections[questionNumber - 1]
      // if (previousAnswerSelection == answerOption.id) {
      //   console.log("ADD_selected_answer")
      //   answerOption.classList.add("selected_answer");
      // }
    });
  }



  function getCurrentAnswerSelection(number) {
    console.log("getCurrentAnswerSelection")
  }

  // function selectAnswer(option) {
  //   console.log("option.target.classListA: ", option.target.classList)
  //   testing = option.target.classList.contains("selected_answer")
  //   console.log(testing)
  //   console.log(option.target)
  //   console.log(option.target.classList.contains("selected_answer"))
  //   if (option.target.classList.contains("selected_answer")) {
  //     option.target.classList.remove("selected_answer")
  //   } else {
  //     option.target.classList.add("selected_answer")
  //     console.log("option.target.classListB: ", option.target.classList)
  //   }
  // }





// //////
//   function start() {
//     alert("starting")
//     // var answerOptions = document.getElementsByClassName("answer-option");
//     // context = JSON.parse('{{ context_arr | escapejs }}');
//     console.log("context: ", context);
//     // Array.from(answerOptions).forEach(function(value, i) {
//     // 	answerOptions[i].innerHTML = String.fromCharCode(i+65) + ". " + context[0]['answers'][i]['option'];
//     // });
//
//     console.log("sessionId: " + sessionId);
//     console.log("context.0.test_response.session_id: " + context[0]['test_response']['session_id']);
//     sessionId.value = context[0]['test_response']['session_id'];
//     testId.value = context[0]['test_response']['test_id'];
//     currentAnswerSelection = getCurrentAnswerSelection(0);
//     setNextQuestion(0);
//     setAnswers(0, currentAnswerSelection);
//
//     console.log("KLKAM");
//     context.forEach(function(q, i) {
//       console.log("q: " + q['question']);
//       question_num_div = document.createElement("div");
//       question_num_div.className = "question_num";
//       question_num_div.innerHTML = "<div class='question_num_div_number'>" + q['question']['num'] + "</div>";
//       questionNums.appendChild(question_num_div);
//       question_num_div.classList.add('question_num_div');
//       question_num_div.addEventListener("click", function() {
//         nextNum = Number(this.textContent) - 1;
//         setNextQuestion(nextNum);
//         currentAnswerSelection = getCurrentAnswerSelection(nextNum);
//         setAnswers(nextNum, currentAnswerSelection);
//       });
//     });
//   }
//
//   function getCurrentAnswerSelection(number) {
//     console.log("number!!!!: ", number);
//     // console.log("(context[number]['test_response'][0]['response']: ", context[number]['test_response'][0]['response']);
//     console.log("current answer: ", context[number]['test_response']['response'])
//     return Number(context[number]['test_response']['response']);
//   }
//
//   function checkForPriorAnswerSelection(context, index) {
//     priorAnswerSelection = context[index]['test_response'][index]['response'];
//
//     if (priorAnswerSelection != -1) {
//       console.log("Answer Selected: ", context[index]['test_response'][index]['response']);
//       setAnswers(number, priorAnswerSelection);
//     }
//   }
//
//   function setNextQuestion(number) {
//     console.log("context[number]['question']['diagram']: ", context[number]['question']['diagram']);
//     columnA.innerHTML = context[number]['question']['option_column_a'];
//     columnB.innerHTML = context[number]['question']['option_column_b'];
//     // sessionId.value = Number(context[number]['question']['test_id_id']);
//     // test_section.value = context[number]['question']['section'];
//     num.innerHTML = context[number]['question']['num'] + ". ";
//     question.innerHTML = context[number]['question']['question_detail_text'];
//     correctAnswer = context[number]['question']['correct_answer'];
//     // setAnswers(number, correctAnswer);
//     var diagram = document.querySelector("#diagram");
//     if (context[number]['question']['diagram'] != 'None') {
//       diagram.src = static_url+context[number]['question']['diagram'];
//     } else {
//       diagram.src = '';
//     }
//     reset();
//   }
//
//   function setAnswers(number, currentAnswerSelection) {
//     console.log("currentAnswerSelection***: ", currentAnswerSelection);
//     answerSelectionHasChanged = false;
//     var explanations = document.getElementsByClassName("explanation");
//     // var answerOptions = document.getElementsByClassName("answer-option");
//     var answerOptions = document.querySelectorAll(".answer_choice");
//     console.log("answerOptions: ", answerOptions);
//     Array.from(answerOptions).forEach(function(answerOption, i) {
//       console.log("answerOption: ", answerOption);
//       answerOption.style.color = "black";
//       answerOption.classList.remove("answer-choice");
//       console.log("Number(answerOption.innerHTML): ", Number(answerOption.id))
//       if (currentAnswerSelection == Number(answerOption.id)) {
//         answerOption.style.color = "orange";
//         answerOption.classList.add("answer-choice");
//       }
//       // answerOption.innerHTML = String.fromCharCode(i+65) + ". " + context[number]['answers'][i]['option'];
//       answerOption.addEventListener("click", function() {
//         // alert("click");
//         resetAnswerColors(answerOptions);
//         currentAnswerSelection = getCurrentAnswerSelection(number);
//         selectAnswer(answerOption, currentAnswerSelection, number);
//         answerOption.classList.add("answer-choice");
//     });
//   });
// }
//
// function selectAnswer(answerOption, currentAnswerSelection, number) {
//
//   answerSelection = Number(answerOption.innerHTML);
//   if (answerOption.id != currentAnswerSelection) {
//     answerSelectionHasChanged = true;
//     answerOption.style.color = "orange";
//   } else {
//     answerOption.style.color = "black";
//   }
//   context[number]['test_response']['response'] = Number(answerOption.id);
// }
//
//   function resetAnswerColors(answerOptions) {
//     Array.from(answerOptions).forEach(function(answerOption, i) {
//       answerOption.style.color = "black";
//       answerOption.classList.remove("answer-choice");
//     });
//   }
//
// function saveFinalAnswer() {
//   alert("Saving final answer");
//   submit_test.click();
//   // console.log("context: ", context);
//   // number = Number(num.innerHTML)
//   // if (number == context.length) {
//   //   number = 0;
//   // }
//   //
//   // currentAnswerSelection = getCurrentAnswerSelection(number);
//   // timeExpired = true;
//   //
//   // if (answerSelectionHasChanged) {
//   //   selectedAnswer = Number(document.getElementsByClassName("answer-choice")[0].id);
//   //   console.log("selectedAnswer***: ", selectedAnswer);
//   //   console.log("number***: ", number);
//   //   console.log("context[number]['test_response'][0]['response']***: " + context[number]['test_response']['response']);
//   //   console.log("context[number]['test_response'][number]***: " + context[number]['test_response'][number]);
//   //   saveAnswer(selectedAnswer, context[number]['test_response']['response'], timeExpired);
//   // }
// }
//
//   function saveAnswer(currentAnswerSelection, contextNumber, timeExpired) {
//     console.log("context: ", context);
//
//     index_positon = number - 1;
//
//     test_response_id = context[index_positon]['test_response']['id'];
//     test_id = context[index_positon]['test_response']['test_id_id'];
//     test_session = context[index_positon]['test_response']['session_id_id'];
//     // section = context[index_positon]['test_response'][0]['section'];
//
//     var xmlhttp = new XMLHttpRequest();
//     var csrftoken = getCookie('csrftoken');
//
//     xmlhttp.open("POST", "../save_test_response/");
//
//     xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
//     xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
//     console.log("num: " + number);
//     console.log("test_response: " + contextNumber);
//     console.log("test_id: " + test_id);
//     console.log("test_session: " + test_session);
//     console.log("section: " + section);
//     console.log("answer_selection: " + currentAnswerSelection);
//
//     xmlhttp.send(JSON.stringify({ "test_response_id": test_response_id, "num": number, "test_response": contextNumber, "test_id": test_id, "test_session": test_session, "section": section, "answer_selection": currentAnswerSelection }));
//     xmlhttp.onload = function() {
//       if (xmlhttp.readyState === XMLHttpRequest.DONE) {
//         if (xmlhttp.status === 200) {
//           console.log("context[number]['test_response'][0]['response']!!!!: " + context[number]['test_response']['response']);
//           console.log("contextNumber!!!: " + contextNumber);
//           console.log("currentAnswerSelection: ", currentAnswerSelection);
//           // context[index_positon]['test_response']['response'] = currentAnswerSelection;
//           console.log("context[number]: " + context[index_positon]['test_response']);
//           console.log("response: ", xmlhttp.responseText);
//           if (timeExpired) {
//             console.log("timeExpired: ", timeExpired);
//             console.log("sessionId.value: ", sessionId.value);
//             window.location.href = "../submit_practice_test_section?session_id="+sessionId.value;
//           }
//         }
//       } else {
//           alert("There was a problem: " + xmlhttp.statusText);
//       }
//       xmlhttp.open
//     }
//   }
//
//
//
//
//
//
//   // nextBtn.addEventListener("click", function() {
//   //   console.log("context: ", context);
//   //   number = Number(num.innerHTML)
//   //   if (number == context.length) {
//   //     number = 0;
//   //   }
//   //
//   //   currentAnswerSelection = getCurrentAnswerSelection(number);
//   //
//   //   if (answerSelectionHasChanged) {
//   //     selectedAnswer = Number(document.getElementsByClassName("answer-choice")[0].id);
//   //     console.log("selectedAnswer***: ", selectedAnswer);
//   //     console.log("number***: ", number);
//   //     console.log("context[number]['test_response'][0]['response']***: " + context[number]['test_response']['response']);
//   //     console.log("context[number]['test_response'][number]***: " + context[number]['test_response'][number]);
//   //     saveAnswer(selectedAnswer, context[number]['test_response']['response'], timeExpired);
//   //   }
//   //
//   //   setNextQuestion(number);
//   //   console.log("currentAnswerSelection: ", currentAnswerSelection)
//   //   setAnswers(number, currentAnswerSelection);
//   //   reset();
//   // });
//
//   backBtn.addEventListener("click", function() {
//     nextNum = Number(num.innerHTML) - 2;
//     if (nextNum == -1) {
//       nextNum = context.length - 1;
//     }
//
//     currentAnswerSelection = getCurrentAnswerSelection(nextNum);
//     if (answerSelectionHasChanged) {
//       selectedAnswer = Number(document.getElementsByClassName("answer-choice")[0].innerHTML)
//       saveAnswer(selectedAnswer, context[number]['test_response'][0]['response'], timeExpired);
//     }
//
//     setNextQuestion(nextNum);
//
//     setAnswers(nextNum, currentAnswerSelection);
//     reset();
//   });
//
//   // pauseSession.addEventListener("click", function() {
//   //   pauseTimer();
//   //
//   // });
//
  function reset() {
    MathJax.texReset();
    MathJax.typesetClear();
    MathJax.typeset();
  }
