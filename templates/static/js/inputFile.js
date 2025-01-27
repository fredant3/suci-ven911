function displayFileName(input) {
	const files = input.files;
	const fileNames = Array.from(files).map(file => file.name).join(', ');
	input.dataset.text = fileNames;
}