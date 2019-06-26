(function() {
	try {
		let url = location.href.match('#(.*)')[1];
		console.log(url);
		let sik = document.getElementById(url);
		sik.style.display = 'block';
	} catch (e) {
		return true;
	}
})();
