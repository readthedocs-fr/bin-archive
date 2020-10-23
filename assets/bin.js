window.onload = function() {
	const selectElm = document.getElementById('select');
	const hlcodeElm = document.getElementById('hlcode');

	for (let lang of hljs.listLanguages()) {
		let optionElm = document.createElement('option');
		optionElm.value = lang;
		if (lang == currentLang) {
			optionElm.setAttribute('selected', true);
		}
		optionElm.appendChild(document.createTextNode(lang));
		selectElm.appendChild(optionElm);
	}

	selectElm.onchange = function() {
		let www = window.location.origin;
		let lang = selectElm.options[selectElm.selectedIndex].value;
		let hexhash = window.location.pathname.split('/').pop().split('.')[0];
		window.location.href = `${www}/${hexhash}?lang=${lang}`;
	}
}