var answer_btn_group = document.getElementsByClassName('answer-option');
var submit_answer_input = document.getElementsByName("answer_response");
//alert(submit_answer_input[0]);
// console.log(submit_answer_input[0]);

for (i = 0; i < answer_btn_group.length; i++) {
	answer_btn_group[i].addEventListener('click', select_option, false);
}

function select_option() {
	if (this.classList.contains("selected")) {
		this.classList.toggle('selected');
	} else {
		clear_selection();
		this.classList.toggle('selected');
	}

	submit_answer_input[0].value = this.id;

}

function clear_selection() {
	for (i = 0; i < answer_btn_group.length; i++) {
		answer_btn_group[i].className = 'answer-option';
		console.log(answer_btn_group[i].classList);
	}
}

//Need to figure out how to strike through the entire answer option not just the "X"

var eliminate_choice_btn_group = document.getElementsByClassName("eliminate-choice");

var eliminate_choice_btn_group_array = [];

for (let i = 0; i < eliminate_choice_btn_group.length; i++) {
	eliminate_choice_btn_group_array[i] = eliminate_choice_btn_group[i];
	eliminate_choice_btn_group_array[i].addEventListener('click', eliminate_option, false);
}

function eliminate_option() {
	answer_btn_group[eliminate_choice_btn_group_array.indexOf(this)].classList.toggle("cross-out-choice");
}
