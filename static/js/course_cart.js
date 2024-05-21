function quantityUpdate(operation,courseId)
{
	const inputBox=	document.getElementById("quantity"+courseId)
	let quantity=parseInt(inputBox.value);
	inputBox.value=quantity+operation
}