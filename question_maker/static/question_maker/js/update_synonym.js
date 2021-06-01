var synonym_word = document.querySelector("#synonym_word");
var update_synonym_buttons = document.querySelectorAll(".update_synonym_button");
var synonym_update_form = document.querySelectorAll(".synonym_update_form");
var option_values = document.querySelectorAll('[id^="option_"]');
var selected_answer_options = document.querySelectorAll('[id^="selected-answer-option_"]');
var definition_alternates = document.querySelectorAll('[name^="definition-alternates_"]')
var custom_word_inputs = document.querySelectorAll('[name^="custom_word_input"]')
var random_word_buttons = document.querySelectorAll('[id^="random-word-btn"]')
var random_word_options = document.querySelectorAll('[name^="random-word-option_"]')

console.log("update_synonym_buttons: ", update_synonym_buttons)

random_word_buttons.forEach((btn, i) => {
  btn.addEventListener("click", function(event) {
    event.preventDefault();
    httpRequest = new XMLHttpRequest();

    if (!httpRequest) {
      alert('Giving up :( Cannot create an XMLHTTP instance');
      return false;
    }

    httpRequest.onreadystatechange = function(){ updateWord(btn.id); };
    httpRequest.open('GET', '/question_maker/get_random_word');
    httpRequest.send();
  });
});

function updateWord(btn_id) {
  if (httpRequest.readyState === XMLHttpRequest.DONE) {
      if (httpRequest.status === 200) {
        random_word = JSON.parse(httpRequest.responseText).random_word
        setNewRandomWord(random_word, btn_id)
      } else {
        alert('There was a problem with the request.');
      }
    }
}

function setNewRandomWord(newRandomWord, btn_id) {
  random_word_id_tag = btn_id.split("_")[1]
  document.querySelector("#random_word_text_" + random_word_id_tag).innerHTML = newRandomWord
  document.querySelector("#random-word-option_" + random_word_id_tag).value = newRandomWord
  document.querySelector("#random_word_input_" + random_word_id_tag).value = newRandomWord
}


// random_word_options.forEach((option, i) => {
//   option.addEventListener("change", function() {
//     console.log("option: ", option)
//     word_input_index = option.name.split("_")[1]
//     // random-word-option_
//     var option_text = document.querySelector("#random_word_text_"+word_input_index).innerHTML;
//     console.log("option_text: ", option_text)
//     console.log("option: ", option)
//     option.value = option_text
//     option.checked = true;
//   });
// });


custom_word_inputs.forEach((item, i) => {
  item.addEventListener("change", function() {
    word_input_index = item.name.split("_")[0]
    var option_radio = document.querySelector("#"+item.name);
    option_radio.value = item.value
    option_radio.checked = true;
  });
});

definition_alternates.forEach((item, i) => {
  item.addEventListener("change", function() {
    def_alt_index = item.name.split("_")[0]
    var option_radio = document.querySelector("#"+item.name);
    option_radio.value = item.value
    option_radio.checked = true;
  });
});

update_synonym_buttons.forEach((btn, i) => {
  console.log("btn: ", btn)
  btn.addEventListener("click", function(event){
    event.preventDefault();
    form_index = btn.id.split("_")[1]

    option_index = "option_" + form_index
    console.log("option_index: ", option_index)
    var option_radios = document.getElementsByName(option_index)
    console.log("option_radios: ", option_radios)
    var selected_option = document.querySelector('input[name='+ option_index +']:checked').value
    console.log("selected_option: ", selected_option)
    option_values[form_index].innerHTML = selected_option
    selected_answer_options[form_index].value = selected_option

    // var selected_alternate = definition_alternates.options[definition_alternates.selectedIndex].value;
    // option_values[form.id.split("_")[1]].innerHTML = selected_alternate
  });
});
