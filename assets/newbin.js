window.onload = function() {
	const codeElm = document.getElementById('code');
	const submitElm = document.getElementById('submit');
	
	codeElm.oninput = function() {
		if (codeElm.value.length) {
			submitElm.removeAttribute('hidden');
		} else {
			submitElm.setAttribute('hidden', true);
		}
	}
	codeElm.oninput();
}