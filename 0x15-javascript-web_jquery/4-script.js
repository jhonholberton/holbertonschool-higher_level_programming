document.querySelector('DIV#toggle_header').onclick = () => {
	const list = document.querySelector('header').classList
	list.toggle("green");
	list.toggle("red");

}
